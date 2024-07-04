package com.publiccms.controller.admin;

import java.util.Date;
import java.util.Map;
import java.util.UUID;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.apache.commons.lang3.StringUtils;
import org.apache.commons.lang3.time.DateUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.SessionAttribute;
import org.springframework.web.servlet.view.UrlBasedViewResolver;

import com.publiccms.common.annotation.Csrf;
import com.publiccms.common.api.Config;
import com.publiccms.common.constants.CommonConstants;
import com.publiccms.common.tools.CommonUtils;
import com.publiccms.common.tools.ControllerUtils;
import com.publiccms.common.tools.RequestUtils;
import com.publiccms.common.tools.UserPasswordUtils;
import com.publiccms.entities.log.LogLogin;
import com.publiccms.entities.log.LogOperate;
import com.publiccms.entities.sys.SysSite;
import com.publiccms.entities.sys.SysUser;
import com.publiccms.entities.sys.SysUserToken;
import com.publiccms.logic.component.cache.CacheComponent;
import com.publiccms.logic.component.config.ConfigComponent;
import com.publiccms.logic.component.config.LoginConfigComponent;
import com.publiccms.logic.component.site.SiteComponent;
import com.publiccms.logic.service.log.LogLoginService;
import com.publiccms.logic.service.log.LogOperateService;
import com.publiccms.logic.service.sys.SysUserService;
import com.publiccms.logic.service.sys.SysUserTokenService;

import java.awt.image.BufferedImage;
import java.io.IOException;
import java.io.OutputStream;
import javax.imageio.ImageIO;
import javax.servlet.ServletException;
import com.publiccms.common.tools.*;
/**
 *
 * LoginAdminController
 *
 */
@Controller
public class LoginAdminController {
    @Autowired
    protected LogOperateService logOperateService;
    @Autowired
    private SysUserService service;
    @Autowired
    private SysUserTokenService sysUserTokenService;
    @Autowired
    private LogLoginService logLoginService;
    @Autowired
    private CacheComponent cacheComponent;
    @Autowired
    private ConfigComponent configComponent;
    @Autowired
    protected SiteComponent siteComponent;

    @RequestMapping(value = "getCode", method = RequestMethod.GET)
    @ResponseBody
    public void getCode(HttpServletRequest request, HttpServletResponse response) throws IOException {
        // 生成验证码类对象
        ImageVerificationCodeUtil codeUtil = new ImageVerificationCodeUtil();

        //获取验证码
        BufferedImage image = codeUtil.getImage();

        // 将验证码的文本存在session中
        request.getSession().setAttribute("text", codeUtil.getText());

        //将验证码图片响应给客户端
        codeUtil.outPut(image, response.getOutputStream());
    }


    /**
     * @param site
     * @param username
     * @param password
     * @param returnUrl
     * @param encoding
     * @param request
     * @param session
     * @param response
     * @param model
     * @return view name
     */
    @RequestMapping(value = "login", method = RequestMethod.POST)
    public String login(@RequestAttribute SysSite site, String username, String password, String returnUrl, String encoding,
            HttpServletRequest request, HttpSession session, HttpServletResponse response, ModelMap model, String verifyInput) {

        verifyInput = StringUtils.trim(verifyInput);
        String verifyCode = (String) session.getAttribute("text");

        // 判断验证码
//        if("".equals(verifyInput) && "".equals(verifyCode)){
//            if(!verifyInput.toLowerCase().equals(verifyCode.toLowerCase())){
//                return "login";
//            }
//        }
        if (ControllerUtils.verifyNotEmpty("verifyInput", verifyInput, model)){
            return "login";
        }else if(StringUtils.isNotEmpty(verifyInput)
                && StringUtils.isNotEmpty(verifyCode)) {
            if (!verifyInput.toLowerCase().equals(verifyCode.toLowerCase())) {
                model.addAttribute(CommonConstants.ERROR, "verify code wrong.");
                return "login";
            }
        }

        username = StringUtils.trim(username);
        password = StringUtils.trim(password);
        if (ControllerUtils.verifyNotEmpty("username", username, model)
                || ControllerUtils.verifyNotEmpty("password", password, model)) {
            model.addAttribute("username", username);
            model.addAttribute("returnUrl", returnUrl);
            return "login";
        }
        String ip = RequestUtils.getIpAddress(request);
        SysUser user = service.findByName(site.getId(), username);
        if (ControllerUtils.verifyNotExist("username", user, model)
                || ControllerUtils.verifyNotEquals("password",
                UserPasswordUtils.passwordEncode(password, user.getSalt(), encoding), user.getPassword(), model)
                || verifyNotAdmin(user, model) || verifyNotEnablie(user, model)) {
            model.addAttribute("username", username);
            model.addAttribute("returnUrl", returnUrl);
            Long userId = -1L;
            if (user != null && user.getId() != null) {
                userId = user.getId();
            }
//            logLoginService.save(new LogLogin(site.getId(), username, userId, ip, LogLoginService.CHANNEL_WEB_MANAGER, false,
//                    CommonUtils.getDate(), password));
            logLoginService.save(new LogLogin(site.getId(), username, userId, ip, LogLoginService.CHANNEL_WEB_MANAGER, false,
                    CommonUtils.getDate(), password));

            return "login";
        }

        ControllerUtils.setAdminToSession(session, user);
        if (UserPasswordUtils.needUpdate(user.getSalt())) {
            String salt = UserPasswordUtils.getSalt();
            service.updatePassword(user.getId(), UserPasswordUtils.passwordEncode(password, salt, encoding), salt);
        }
        if (!user.isWeakPassword() && UserPasswordUtils.isWeek(username, password)) {
            service.updateWeekPassword(user.getId(), true);
        }
        service.updateLoginStatus(user.getId(), ip);
        String authToken = UUID.randomUUID().toString();
        Date now = CommonUtils.getDate();
        Map<String, String> config = configComponent.getConfigData(site.getId(), Config.CONFIG_CODE_SITE);
        int expiryMinutes = ConfigComponent.getInt(config.get(LoginConfigComponent.CONFIG_EXPIRY_MINUTES_MANAGER),
                LoginConfigComponent.DEFAULT_EXPIRY_MINUTES);
        sysUserTokenService.save(new SysUserToken(authToken, site.getId(), user.getId(), LogLoginService.CHANNEL_WEB_MANAGER, now,
                DateUtils.addMinutes(now, expiryMinutes), ip));
        StringBuilder sb = new StringBuilder();
        sb.append(user.getId()).append(CommonConstants.getCookiesUserSplit()).append(authToken);
        RequestUtils.addCookie(request.getContextPath(), response, CommonConstants.getCookiesAdmin(), sb.toString(),
                expiryMinutes * 60, null);
        logLoginService.save(new LogLogin(site.getId(), username, user.getId(), ip, LogLoginService.CHANNEL_WEB_MANAGER, true,
                CommonUtils.getDate(), null));
        String safeReturnUrl = config.get(LoginConfigComponent.CONFIG_RETURN_URL);
        if (ControllerUtils.isUnSafeUrl(returnUrl, site, safeReturnUrl, request)) {
            returnUrl = CommonConstants.getDefaultPage();
        }
        return UrlBasedViewResolver.REDIRECT_URL_PREFIX + returnUrl;
    }

    /**
     * @param site
     * @param username
     * @param password
     * @param encoding 
     * @param request
     * @param session
     * @param response
     * @param model
     * @return view name
     */
    @RequestMapping(value = "loginDialog", method = RequestMethod.POST)
    public String loginDialog(@RequestAttribute SysSite site, String username, String password, String encoding,
            HttpServletRequest request, HttpServletResponse response, HttpSession session, ModelMap model, String verifyInput) {
        if ("login".equals(loginWithoutVerifyCode(site, username, password, null, encoding, request, session, response, model))) {
            return CommonConstants.TEMPLATE_ERROR;
        }
        return CommonConstants.TEMPLATE_DONE;
    }

    //下面这个逻辑和上面的login逻辑一样，但是不用验证码，用于在系统内超时登录时输入用户名和密码。
    private String loginWithoutVerifyCode(@RequestAttribute SysSite site, String username, String password, String returnUrl, String encoding,
                        HttpServletRequest request, HttpSession session, HttpServletResponse response, ModelMap model) {



        username = StringUtils.trim(username);
        password = StringUtils.trim(password);
        if (ControllerUtils.verifyNotEmpty("username", username, model)
                || ControllerUtils.verifyNotEmpty("password", password, model)) {
            model.addAttribute("username", username);
            model.addAttribute("returnUrl", returnUrl);
            return "login";
        }
        String ip = RequestUtils.getIpAddress(request);
        SysUser user = service.findByName(site.getId(), username);
        if (ControllerUtils.verifyNotExist("username", user, model)
                || ControllerUtils.verifyNotEquals("password",
                UserPasswordUtils.passwordEncode(password, user.getSalt(), encoding), user.getPassword(), model)
                || verifyNotAdmin(user, model) || verifyNotEnablie(user, model)) {
            model.addAttribute("username", username);
            model.addAttribute("returnUrl", returnUrl);
            Long userId = -1L;
            if (user != null && user.getId() != null) {
                userId = user.getId();
            }
//            logLoginService.save(new LogLogin(site.getId(), username, userId, ip, LogLoginService.CHANNEL_WEB_MANAGER, false,
//                    CommonUtils.getDate(), password));
            logLoginService.save(new LogLogin(site.getId(), username, userId, ip, LogLoginService.CHANNEL_WEB_MANAGER, false,
                    CommonUtils.getDate(), password));

            return "login";
        }

        ControllerUtils.setAdminToSession(session, user);
        if (UserPasswordUtils.needUpdate(user.getSalt())) {
            String salt = UserPasswordUtils.getSalt();
            service.updatePassword(user.getId(), UserPasswordUtils.passwordEncode(password, salt, encoding), salt);
        }
        if (!user.isWeakPassword() && UserPasswordUtils.isWeek(username, password)) {
            service.updateWeekPassword(user.getId(), true);
        }
        service.updateLoginStatus(user.getId(), ip);
        String authToken = UUID.randomUUID().toString();
        Date now = CommonUtils.getDate();
        Map<String, String> config = configComponent.getConfigData(site.getId(), Config.CONFIG_CODE_SITE);
        int expiryMinutes = ConfigComponent.getInt(config.get(LoginConfigComponent.CONFIG_EXPIRY_MINUTES_MANAGER),
                LoginConfigComponent.DEFAULT_EXPIRY_MINUTES);
        sysUserTokenService.save(new SysUserToken(authToken, site.getId(), user.getId(), LogLoginService.CHANNEL_WEB_MANAGER, now,
                DateUtils.addMinutes(now, expiryMinutes), ip));
        StringBuilder sb = new StringBuilder();
        sb.append(user.getId()).append(CommonConstants.getCookiesUserSplit()).append(authToken);
        RequestUtils.addCookie(request.getContextPath(), response, CommonConstants.getCookiesAdmin(), sb.toString(),
                expiryMinutes * 60, null);
        logLoginService.save(new LogLogin(site.getId(), username, user.getId(), ip, LogLoginService.CHANNEL_WEB_MANAGER, true,
                CommonUtils.getDate(), null));
        String safeReturnUrl = config.get(LoginConfigComponent.CONFIG_RETURN_URL);
        if (ControllerUtils.isUnSafeUrl(returnUrl, site, safeReturnUrl, request)) {
            returnUrl = CommonConstants.getDefaultPage();
        }
        return UrlBasedViewResolver.REDIRECT_URL_PREFIX + returnUrl;
    }


    /**
     * @param site
     * @param admin
     * @param oldpassword
     * @param password
     * @param repassword
     * @param encoding
     * @param request
     * @param response
     * @param model
     * @return view name
     */
    @RequestMapping(value = "changePassword", method = RequestMethod.POST)
    @Csrf
    public String changeMyselfPassword(@RequestAttribute SysSite site, @SessionAttribute SysUser admin, String oldpassword,
            String password, String repassword, String encoding, HttpServletRequest request, HttpServletResponse response,
            ModelMap model) {
        SysUser user = service.getEntity(admin.getId());
        String encodedOldPassword = UserPasswordUtils.passwordEncode(oldpassword, user.getSalt(), encoding);
        if (null != user.getPassword()
                && ControllerUtils.verifyNotEquals("password", user.getPassword(), encodedOldPassword, model)) {
            return CommonConstants.TEMPLATE_ERROR;
        } else if (ControllerUtils.verifyNotEmpty("password", password, model)
                || ControllerUtils.verifyNotEquals("repassword", password, repassword, model)) {
            return CommonConstants.TEMPLATE_ERROR;
        } else {
            ControllerUtils.clearAdminToSession(request.getContextPath(), request.getSession(), response);
            model.addAttribute(CommonConstants.MESSAGE, "message.needReLogin");
        }
        String salt = UserPasswordUtils.getSalt();
        service.updatePassword(user.getId(), UserPasswordUtils.passwordEncode(password, salt, encoding), salt);
        if (user.isWeakPassword() && !UserPasswordUtils.isWeek(user.getName(), password)) {
            service.updateWeekPassword(user.getId(), false);
        }
        sysUserTokenService.delete(user.getId());
        logOperateService.save(new LogOperate(site.getId(), user.getId(), LogLoginService.CHANNEL_WEB_MANAGER, "changepassword",
                RequestUtils.getIpAddress(request), CommonUtils.getDate(), encodedOldPassword));
        return "common/ajaxTimeout";
    }

    /**
     * @param admin
     * @param password
     * @param session
     * @return result
     */
    @RequestMapping("isWeak")
    @ResponseBody
    public boolean isWeak(@SessionAttribute SysUser admin, String password, HttpSession session) {
        return !UserPasswordUtils.isWeek(admin.getName(), password);
    }

    /**
     * @param userId
     * @param request
     * @param response
     * @return view name
     */
    @RequestMapping(value = "logout", method = RequestMethod.GET)
    public String logout(Long userId, HttpServletRequest request, HttpServletResponse response) {
        SysUser admin = ControllerUtils.getAdminFromSession(request.getSession());
        if (null != userId && null != admin && userId.equals(admin.getId())) {
            Cookie userCookie = RequestUtils.getCookie(request.getCookies(), CommonConstants.getCookiesAdmin());
            if (null != userCookie && CommonUtils.notEmpty(userCookie.getValue())) {
                String value = userCookie.getValue();
                if (null != value) {
                    String[] userData = value.split(CommonConstants.getCookiesUserSplit());
                    if (userData.length > 1) {
                        sysUserTokenService.delete(userData[1]);
                    }
                }
            }
            ControllerUtils.clearAdminToSession(request.getContextPath(), request.getSession(), response);
        }
        return UrlBasedViewResolver.REDIRECT_URL_PREFIX + CommonConstants.getDefaultPage();
    }

    /**
     * @return view name
     */
    @RequestMapping(value = "clearCache")
    public String clearCache() {
        cacheComponent.clear();
        return CommonConstants.TEMPLATE_DONE;
    }

    protected boolean verifyNotAdmin(SysUser user, ModelMap model) {
        if (!user.isDisabled() && !user.isSuperuserAccess()) {
            model.addAttribute(CommonConstants.ERROR, "verify.user.notAdmin");
            return true;
        }
        return false;
    }

    protected boolean verifyNotEnablie(SysUser user, ModelMap model) {
        if (user.isDisabled()) {
            model.addAttribute(CommonConstants.ERROR, "verify.user.notEnablie");
            return true;
        }
        return false;
    }
}
