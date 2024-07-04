package com.publiccms.logic.service.cms;

// Generated 2021-6-26 17:53:08 by com.publiccms.common.generator.SourceGenerator
import java.math.BigDecimal;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Isolation;
import org.springframework.transaction.annotation.Transactional;

import com.publiccms.common.base.BaseService;
import com.publiccms.common.handler.PageHandler;
import com.publiccms.common.tools.CommonUtils;
import com.publiccms.entities.cms.CmsContentProduct;
import com.publiccms.entities.trade.TradeOrderProduct;
import com.publiccms.logic.dao.cms.CmsContentProductDao;

/**
 *
 * CmsContentProductService
 * 
 */
@Service
@Transactional
public class CmsContentProductService extends BaseService<CmsContentProduct> {

    private String[] ignoreProperties = new String[] { "id", "userId", "siteId", "contentId" };

    /**
     * @param siteId
     * @param contentId
     * @param userId
     * @param title
     * @param startPrice
     * @param endPrice
     * @param orderField
     * @param orderType
     * @param pageIndex
     * @param pageSize
     * @return results page
     */
    @Transactional(readOnly = true)
    public PageHandler getPage(Short siteId, Long contentId, Long userId, String title, BigDecimal startPrice,
            BigDecimal endPrice, String orderField, String orderType, Integer pageIndex, Integer pageSize) {
        return dao.getPage(siteId, contentId, userId, title, startPrice, endPrice, orderField, orderType, pageIndex, pageSize);
    }

    /**
     * @param siteId
     * @param contentId
     * @param userId
     * @param products
     */
    @SuppressWarnings("unchecked")
    public void update(short siteId, long contentId, Long userId, List<CmsContentProduct> products) {
        Set<Long> idList = new HashSet<>();
        if (CommonUtils.notEmpty(products)) {
            for (CmsContentProduct entity : products) {
                if (null != entity.getId()) {
                    update(entity.getId(), entity, ignoreProperties);
                } else {
                    entity.setSiteId(siteId);
                    entity.setUserId(userId);
                    entity.setContentId(contentId);
                    save(entity);
                }
                idList.add(entity.getId());
            }
        }
        for (CmsContentProduct product : (List<CmsContentProduct>) getPage(siteId, contentId, null, null, null, null, null, null,
                null, null).getList()) {
            if (!idList.contains(product.getId())) {
                delete(product.getId());
            }
        }
    }

    /**
     * @param siteId
     * @param tradeOrderProductList
     */
    @Transactional(isolation = Isolation.SERIALIZABLE)
    public void deduction(short siteId, List<TradeOrderProduct> tradeOrderProductList) {
        if (null != tradeOrderProductList) {
            for (TradeOrderProduct orderProduct : tradeOrderProductList) {
                if (siteId == orderProduct.getSiteId()) {
                    CmsContentProduct entity = getEntity(orderProduct.getProductId());
                    entity.setInventory(entity.getInventory() - orderProduct.getQuantity());
                    entity.setSales(entity.getSales() + orderProduct.getQuantity());
                }
            }
        }
    }

    @Autowired
    private CmsContentProductDao dao;

}