package com.publiccms.views.directive.tools;

import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.publiccms.common.base.AbstractTemplateDirective;
import com.publiccms.common.handler.RenderHandler;
import com.publiccms.common.tools.CmsFileUtils;
import com.publiccms.common.tools.CommonUtils;
import com.publiccms.entities.sys.SysSite;
import com.publiccms.logic.component.template.MetadataComponent;
import com.publiccms.logic.component.template.TemplateComponent;
import com.publiccms.views.pojo.entities.CmsPlaceMetadata;

/**
 *
 * IncludePlaceDirective
 * 
 */
@Component
public class IncludePlaceDirective extends AbstractTemplateDirective {

    @Override
    public void execute(RenderHandler handler) throws IOException, Exception {
        String path = handler.getString("path");
        if (CommonUtils.notEmpty(path)) {
            SysSite site = getSite(handler);
            CmsPlaceMetadata metadata = metadataComponent
                    .getPlaceMetadata(siteComponent.getWebTemplateFilePath(site, TemplateComponent.INCLUDE_DIRECTORY + path));
            if (site.isUseSsi()) {
                handler.print(new StringBuilder("<!--#include virtual=\"/").append(TemplateComponent.INCLUDE_DIRECTORY)
                        .append(path).append("\"-->").toString());
            } else {
                String filePath = siteComponent.getWebFilePath(site, TemplateComponent.INCLUDE_DIRECTORY + path);
                if (CmsFileUtils.exists(filePath)) {
                    handler.print(CmsFileUtils.getFileContent(filePath));
                } else {
                    templateComponent.printPlace(handler.getWriter(), site, path, metadata);
                }
            }
        }
    }

    @Override
    public boolean needAppToken() {
        return true;
    }

    @Autowired
    private TemplateComponent templateComponent;
    @Autowired
    private MetadataComponent metadataComponent;

}
