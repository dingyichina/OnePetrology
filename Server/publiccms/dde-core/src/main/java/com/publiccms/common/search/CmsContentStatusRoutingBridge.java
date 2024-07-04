package com.publiccms.common.search;

import org.hibernate.search.mapper.pojo.bridge.RoutingBridge;
import org.hibernate.search.mapper.pojo.bridge.runtime.RoutingBridgeRouteContext;
import org.hibernate.search.mapper.pojo.route.DocumentRoutes;

import com.publiccms.entities.cms.CmsContent;
import com.publiccms.logic.service.cms.CmsContentService;

/**
 *
 * CmsContentStatusRoutingBridge
 * 
 */
public class CmsContentStatusRoutingBridge implements RoutingBridge<CmsContent> {

    @Override
    public void route(DocumentRoutes routes, Object entityIdentifier, CmsContent indexedEntity,
            RoutingBridgeRouteContext context) {
        if (CmsContentService.STATUS_NORMAL == indexedEntity.getStatus() && null == indexedEntity.getQuoteContentId() && !indexedEntity.isDisabled()) {
            routes.addRoute();
        }else {
            routes.notIndexed();
        }

    }

    @Override
    public void previousRoutes(DocumentRoutes routes, Object entityIdentifier, CmsContent indexedEntity,
            RoutingBridgeRouteContext context) {
        route(routes, entityIdentifier, indexedEntity, context);
    }
}