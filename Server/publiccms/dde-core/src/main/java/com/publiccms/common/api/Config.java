package com.publiccms.common.api;

import java.util.List;
import java.util.Locale;

import com.publiccms.common.constants.CommonConstants;
import com.publiccms.common.tools.LanguagesUtils;
import com.publiccms.entities.sys.SysExtendField;
import com.publiccms.entities.sys.SysSite;

/**
 *
 * Config
 * 
 */
public interface Config {
    /**
     * 
     */
    String CONFIGPREFIX = "config.";

    /**
     * 
     */
    String CONFIG_CODE_SITE = "site";

    /**
     * 
     */
    String CONFIG_CODE_DESCRIPTION = CONFIGPREFIX + CONFIG_CODE_SITE;
    /**
     * 
     */
    String CONFIG_CODE_DESCRIPTION_SUFFIX = CommonConstants.DOT + "description";
    /**
     * 
     */
    String CONFIG_CODE_SITEA_TTRIBUTE = "siteAttribute";

    /**
     * 
     */
    String INPUTTYPE_TEMPLATE = "template";

    /**
     * 
     */
    String INPUTTYPE_TEXT = "text";

    /**
     * 
     */
    String INPUTTYPE_FILE = "file";

    /**
     * 
     */
    String INPUTTYPE_IMAGE = "image";

    /**
     * 
     */
    String INPUTTYPE_TEXTAREA = "textarea";

    /**
     * 
     */
    String INPUTTYPE_DATE = "date";

    /**
     * 
     */
    String INPUTTYPE_DATETIME = "datetime";

    /**
     * 
     */
    String INPUTTYPE_USER = "user";

    /**
     * 
     */
    String INPUTTYPE_DICTIONARY = "dictionary";

    /**
     * 
     */
    String INPUTTYPE_CONTENT = "content";

    /**
     * 
     */
    String INPUTTYPE_CATEGORY = "category";

    /**
     * 
     */
    String INPUTTYPE_CATEGORYTYPE = "categoryType";

    /**
     * 
     */
    String INPUTTYPE_TAGTYPE = "tagType";

    /**
     * 
     */
    String INPUTTYPE_NUMBER = "number";

    /**
     * 
     */
    String INPUTTYPE_PASSWORD = "password";

    /**
     * 
     */
    String INPUTTYPE_BOOLEAN = "boolean";

    /**
     * 
     */
    String INPUTTYPE_EMAIL = "email";

    /**
     * @param site
     * @param locale
     * @return config extend field list
     */
    List<SysExtendField> getExtendFieldList(SysSite site, Locale locale);

    /**
     * @param site
     * @param showAll
     * @return config code or null
     */
    default String getCode(SysSite site, boolean showAll) {
        return CONFIG_CODE_SITE;
    }

    /**
     * @param locale
     * @param code
     * @param args
     * @return config code or null
     */
    default String getMessage(Locale locale, String code, Object... args) {
        return LanguagesUtils.getMessage(CommonConstants.applicationContext, locale, code, args);
    }

    /**
     * @param site
     * @return config code or null
     */
    default String getCode(SysSite site) {
        return getCode(site, false);
    }

    /**
     * @param locale
     * @return
     */
    default String getCodeDescription(Locale locale) {
        return LanguagesUtils.getMessage(CommonConstants.applicationContext, locale, CONFIG_CODE_DESCRIPTION);
    }
}