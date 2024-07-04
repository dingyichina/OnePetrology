package com.publiccms.views.directive.trade;

// Generated 2019-6-15 18:52:24 by com.publiccms.common.generator.SourceGenerator
import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.publiccms.logic.service.trade.TradePaymentService;
import com.publiccms.common.base.AbstractTemplateDirective;
import com.publiccms.common.handler.RenderHandler;
import com.publiccms.common.handler.PageHandler;

/**
 *
 * TradePaymentListDirective
 * 
 */
@Component
public class TradePaymentListDirective extends AbstractTemplateDirective {

    @Override
    public void execute(RenderHandler handler) throws IOException, Exception {
        PageHandler page = service.getPage(getSite(handler).getId(), handler.getLong("userId"), handler.getString("tradeType"),
                handler.getString("serialNumber"), handler.getString("accountType"), handler.getString("accountSerialNumber"),
                handler.getIntegerArray("status"), handler.getDate("startCreateDate"), handler.getDate("endCreateDate"),
                handler.getString("paymentType"), handler.getInteger("pageIndex", 1), handler.getInteger("pageSize", 30));
        handler.put("page", page).render();
    }

    @Override
    public boolean needAppToken() {
        return true;
    }

    @Autowired
    private TradePaymentService service;

}