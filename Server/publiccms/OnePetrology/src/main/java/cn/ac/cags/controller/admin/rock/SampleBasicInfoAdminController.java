package cn.ac.cags.controller.admin.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator

import javax.servlet.http.HttpServletRequest;

import cn.ac.cags.util.DDEUtils;
import com.publiccms.common.tools.*;
import com.publiccms.logic.component.cache.CacheComponent;
import com.publiccms.logic.component.site.SiteComponent;
import com.publiccms.logic.component.template.MetadataComponent;
import com.publiccms.logic.component.template.TemplateCacheComponent;
import com.publiccms.logic.component.template.TemplateComponent;
import com.publiccms.views.pojo.entities.CmsPageMetadata;
import org.apache.commons.lang3.StringUtils;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.SessionAttribute;

import com.publiccms.common.annotation.Csrf;
import com.publiccms.common.constants.CommonConstants;
import com.publiccms.entities.sys.SysSite;
import com.publiccms.entities.sys.SysUser;

import cn.ac.cags.entities.rock.SampleBasicInfo;
import com.publiccms.entities.log.LogOperate;
import com.publiccms.logic.service.log.LogLoginService;
import com.publiccms.logic.service.log.LogOperateService;
import cn.ac.cags.logic.service.rock.SampleBasicInfoService;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

/**
 *
 * SampleBasicInfoAdminController
 * 
 */
@Controller
@RequestMapping("sampleBasicInfo")
public class SampleBasicInfoAdminController {
    protected final Log log = LogFactory.getLog(getClass());
    private String[] ignoreProperties = new String[]{"id"};
    @Autowired
    protected SiteComponent siteComponent;
//    @Autowired
//    private MetadataComponent metadataComponent;
//    @Autowired
//    private TemplateCacheComponent templateCacheComponent;
//    @Autowired
//    private CacheComponent cacheComponent;
//    @Autowired
//    private TemplateComponent templateComponent;
    /**
     * @param site
     * @param admin
     * @param entity
     * @param request
     * @param model
     * @return operate result
     */
    @RequestMapping("save")
    @Csrf
    public String save(@RequestAttribute SysSite site, @SessionAttribute SysUser admin, SampleBasicInfo entity, HttpServletRequest request,
             ModelMap model) {
        if (null != entity.getId()) {
            entity = service.update(entity.getId(), entity, ignoreProperties);
            logOperateService.save(new LogOperate(site.getId(), admin.getId(), LogLoginService.CHANNEL_WEB_MANAGER, "update.sampleBasicInfo", 
                                RequestUtils.getIpAddress(request), CommonUtils.getDate(), JsonUtils.getString(entity)));
        } else {
            service.save(entity);
            logOperateService.save(new LogOperate(site.getId(), admin.getId(), LogLoginService.CHANNEL_WEB_MANAGER, "save.sampleBasicInfo", 
                            RequestUtils.getIpAddress(request), CommonUtils.getDate(), JsonUtils.getString(entity)));
        }
        return CommonConstants.TEMPLATE_DONE;
    }

    /**
     * @param ids
     * @param request
     * @param site
     * @param admin 
     * @param _csrf 
     * @param model
     * @return operate result
     */
    @RequestMapping("delete")
    @Csrf
    public String delete(@RequestAttribute SysSite site, @SessionAttribute SysUser admin, Integer[] ids, String _csrf, HttpServletRequest request, 
            ModelMap model) {
        if (CommonUtils.notEmpty(ids)) {
            service.delete(ids);
            logOperateService.save(new LogOperate(site.getId(), admin.getId(), LogLoginService.CHANNEL_WEB_MANAGER, "delete.sampleBasicInfo",
                            RequestUtils.getIpAddress(request), CommonUtils.getDate(), StringUtils.join(ids, ',')));
        }
        return CommonConstants.TEMPLATE_DONE;
    }
    /**
     * @param ids
     * @param request
     * @param site
     * @param admin
     * @param _csrf
     * @param model
     * @return operate result
     */
    @RequestMapping("check")
    @Csrf
    public String check(@RequestAttribute SysSite site, @SessionAttribute SysUser admin, Integer[] ids, String _csrf, HttpServletRequest request,
                         ModelMap model) {
        if (CommonUtils.notEmpty(ids)) {
            //此处修改为check，即修改为has_check=true
            service.checked(ids);
            logOperateService.save(new LogOperate(site.getId(), admin.getId(), LogLoginService.CHANNEL_WEB_MANAGER, "delete.sampleBasicInfo",
                    RequestUtils.getIpAddress(request), CommonUtils.getDate(), StringUtils.join(ids, ',')));
        }
        return CommonConstants.TEMPLATE_DONE;
    }

    /**
     *
     * @param site
     * @param admin
     * @param files
     * @param path
     * @param request
     * @param model
     * @return
     */
    @RequestMapping("doUpload")
    @Csrf
    public String upload(@RequestAttribute SysSite site, @SessionAttribute SysUser admin, MultipartFile[] files, String path,
                         HttpServletRequest request, ModelMap model) {
        if (ControllerUtils.verifyCustom("noright", null != site.getParentId(), model)) {
            return CommonConstants.TEMPLATE_ERROR;
        }
        if (null != files) {
            try {
                for (MultipartFile file : files) {
                    path="/ddedata";
                    String filePath = path + CommonConstants.SEPARATOR + file.getOriginalFilename();
                    String dstFile=CmsFileUtils.upload(file, siteComponent.getWebFilePath(site, filePath));
                    //判断解析excel文件
                    String fullPath= DDEUtils.getLocalFullPath(site,"ddedata/")+dstFile;
                    System.out.println(fullPath);



                    /**
                    CmsPageMetadata metadata = new CmsPageMetadata();
                    metadata.setUseDynamic(true);
                    metadataComponent.updateTemplateMetadata(filePath, metadata);
                    templateComponent.clearTemplateCache();
                    cacheComponent.clearViewCache();*/

                    logOperateService.save(new LogOperate(site.getId(), admin.getId(), LogLoginService.CHANNEL_WEB_MANAGER,
                            "upload.web.template", RequestUtils.getIpAddress(request), CommonUtils.getDate(), filePath));
                }
            } catch (IOException e) {
                model.addAttribute(CommonConstants.ERROR, e.getMessage());
                log.error(e.getMessage(), e);
                return CommonConstants.TEMPLATE_ERROR;
            }
        }
        return CommonConstants.TEMPLATE_DONE;
    }




    @Autowired
    private SampleBasicInfoService service;
    @Autowired
    protected LogOperateService logOperateService;
}