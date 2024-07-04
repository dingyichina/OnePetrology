package com.publiccms.views.directive.tools;

import java.io.IOException;

import org.springframework.stereotype.Component;

import com.publiccms.common.base.AbstractTemplateDirective;
import com.publiccms.common.handler.RenderHandler;
import com.publiccms.common.tools.CmsFileUtils;
import com.publiccms.common.tools.CommonUtils;

/**
 *
 * TemplateContentDirective
 * 
 */
@Component
public class TemplateContentDirective extends AbstractTemplateDirective {

    @Override
    public void execute(RenderHandler handler) throws IOException, Exception {
        String path = handler.getString("path");
        if (CommonUtils.notEmpty(path)) {
            handler.put("object", CmsFileUtils.getFileContent(siteComponent.getWebTemplateFilePath(getSite(handler), path)))
                    .render();
        }
    }
    
    @Override
    public boolean needAppToken() {
        return true;
    }

}
