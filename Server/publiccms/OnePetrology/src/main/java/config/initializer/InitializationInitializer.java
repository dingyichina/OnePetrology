package config.initializer;

import java.io.File;
import java.io.IOException;
import java.lang.reflect.Field;
import java.net.Authenticator;
import java.nio.charset.Charset;
import java.util.Properties;

import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.ServletRegistration.Dynamic;

import org.apache.commons.io.FileUtils;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.core.io.support.PropertiesLoaderUtils;
import org.springframework.web.HttpRequestHandler;
import org.springframework.web.WebApplicationInitializer;
import org.springframework.web.util.IntrospectorCleanupListener;

import com.publiccms.common.constants.CmsVersion;
import com.publiccms.common.constants.CommonConstants;
import com.publiccms.common.database.CmsDataSource;
import com.publiccms.common.proxy.UsernamePasswordAuthenticator;
import com.publiccms.common.servlet.InstallHttpRequestHandler;
import com.publiccms.common.servlet.InstallServlet;

/**
 *
 * InstallationInitializer
 *
 */
public class InitializationInitializer implements WebApplicationInitializer {
    protected static final Log log = LogFactory.getLog(InitializationInitializer.class);
    /**
     * 安装Servlet映射路径
     */
    public final static String INSTALL_SERVLET_MAPPING = "/install/";
    /**
     * 安装跳转处理器
     */
    public final static HttpRequestHandler INSTALL_HTTPREQUEST_HANDLER = new InstallHttpRequestHandler(INSTALL_SERVLET_MAPPING);

    @Override
    public void onStartup(ServletContext servletcontext) throws ServletException {
        initEncoding();
        try {
            Properties config = PropertiesLoaderUtils.loadAllProperties(CommonConstants.CMS_CONFIG_FILE);
            initProxy(config);
            if (null == CommonConstants.CMS_FILEPATH) {
                initFilePath(config.getProperty("cms.filePath"), System.getProperty("user.dir"));
            }
            File file = new File(CommonConstants.CMS_FILEPATH + CommonConstants.INSTALL_LOCK_FILENAME);
            if (file.exists()) {
                String version = FileUtils.readFileToString(file, CommonConstants.DEFAULT_CHARSET_NAME);
                if (CmsVersion.getVersion().equals(version)) {
                    CmsVersion.setInitialized(true);
                    CmsDataSource.initDefaultDataSource();
                    log.info(String.format("PublicCMS %s will start normally in %s", CmsVersion.getVersion(),
                            CommonConstants.CMS_FILEPATH));
                } else {
                    createInstallServlet(servletcontext, config, InstallServlet.STEP_CHECKDATABASE, version);
                    log.warn(String.format("PublicCMS %s installer will start in %s, please upgrade your database!",
                            CmsVersion.getVersion(), CommonConstants.CMS_FILEPATH));
                }
            } else {
                createInstallServlet(servletcontext, config, null, null);
                log.warn(String.format(
                        "PublicCMS %s installer will start in %s, please configure your database information and initialize the database!",
                        CmsVersion.getVersion(), CommonConstants.CMS_FILEPATH));
            }
        } catch (IOException e) {
            throw new ServletException(e);
        }
        servletcontext.addListener(IntrospectorCleanupListener.class);
    }

    /**
     * 检查CMS路径变量
     * 
     * @param filePath
     * @param defaultPath
     * 
     */
    public static void initFilePath(String filePath, String defaultPath) {
        File file = new File(System.getProperty("cms.filePath", filePath));
        try {
            file.mkdirs();
        } catch (Exception e) {
        }
        if (!file.exists()) {
            log.warn(String.format("PublicCMS %s the cms.filePath parameter is invalid , try to use the temporary directory.",
                    CmsVersion.getVersion()));
            file = new File(defaultPath, "data/publiccms");
        }
        CommonConstants.CMS_FILEPATH = file.getAbsolutePath();
    }

    private static void createInstallServlet(ServletContext servletcontext, Properties config, String startStep, String version) {
        Dynamic registration = servletcontext.addServlet("install", new InstallServlet(config, startStep, version));
        registration.setLoadOnStartup(1);
        registration.addMapping(new String[] { INSTALL_SERVLET_MAPPING });
    }

    /**
     * 字符集配置
     * 
     * @param config
     * @throws IOException
     */
    public static void initEncoding() {
        Charset old = Charset.defaultCharset();
        if (!old.equals(CommonConstants.DEFAULT_CHARSET)) {
            log.info(String.format("old file.encoding = %s", old));
            try {
                Field field = Charset.class.getDeclaredField("defaultCharset");
                field.setAccessible(true);
                System.setProperty("file.encoding", CommonConstants.DEFAULT_CHARSET_NAME);
                field.set(null, null);
            } catch (NoSuchFieldException | SecurityException | IllegalArgumentException | IllegalAccessException e) {
            }
            log.info(String.format("new file.encoding = %s" ,Charset.defaultCharset()));
        }
    }

    /**
     * 代理配置
     * 
     * @param config
     * @throws IOException
     */
    private static void initProxy(Properties config) throws IOException {
        if ("true".equalsIgnoreCase(System.getProperty("cms.proxy.enable", config.getProperty("cms.proxy.enable", "false")))) {
            Properties proxyProperties = PropertiesLoaderUtils.loadAllProperties(
                    System.getProperty("cms.proxy.configFilePath", config.getProperty("cms.proxy.configFilePath")));
            for (String key : proxyProperties.stringPropertyNames()) {
                System.setProperty(key, proxyProperties.getProperty(key));
            }
            Authenticator.setDefault(new UsernamePasswordAuthenticator(config.getProperty("cms.proxy.userName"),
                    config.getProperty("cms.proxy.password")));
        }
    }
}
