package com.publiccms.views.directive.trade;

// Generated 2019-6-16 9:47:27 by com.publiccms.common.generator.SourceGenerator

import java.io.IOException;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.publiccms.common.base.AbstractTemplateDirective;
import com.publiccms.common.handler.RenderHandler;
import com.publiccms.common.tools.CommonUtils;
import com.publiccms.entities.sys.SysSite;
import com.publiccms.entities.trade.TradeAccount;
import com.publiccms.logic.service.trade.TradeAccountService;

/**
 *
 * TradeAccountDirective
 * 
 */
@Component
public class TradeAccountDirective extends AbstractTemplateDirective {

    @Override
    public void execute(RenderHandler handler) throws IOException, Exception {
        Long id = handler.getLong("id");
        SysSite site = getSite(handler);
        if (CommonUtils.notEmpty(id)) {
            TradeAccount entity = service.getOrCreate(getSite(handler).getId(), id);
            if (null != entity && site.getId() == entity.getSiteId()) {
                handler.put("object", entity).render();
            }
        } else {
            Long[] ids = handler.getLongArray("ids");
            if (CommonUtils.notEmpty(ids)) {
                List<TradeAccount> entityList = service.getEntitys(ids);
                Map<String, TradeAccount> map = CommonUtils.listToMap(entityList, k -> String.valueOf(k.getId()), null, entity -> site.getId() == entity.getSiteId());
                handler.put("map", map).render();
            }
        }
    }

    @Override
    public boolean needAppToken() {
        return true;
    }

    @Autowired
    private TradeAccountService service;

}
