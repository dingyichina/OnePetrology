package com.publiccms.logic.dao.trade;

// Generated 2019-6-16 9:47:27 by com.publiccms.common.generator.SourceGenerator
import java.util.Date;

import org.springframework.stereotype.Repository;

import com.publiccms.common.base.BaseDao;
import com.publiccms.common.handler.PageHandler;
import com.publiccms.common.handler.QueryHandler;
import com.publiccms.common.tools.CommonUtils;
import com.publiccms.entities.trade.TradeAccountHistory;

/**
 *
 * TradeAccountHistoryDao
 * 
 */
@Repository
public class TradeAccountHistoryDao extends BaseDao<TradeAccountHistory> {

    /**
     * 
     * @param siteId
     * @param accountId
     * @param userId
     * @param status
     * @param startCreateDate
     * @param endCreateDate
     * @param paymentType
     * @param pageIndex
     * @param pageSize
     * @return results page
     */
    public PageHandler getPage(Short siteId, Long accountId, Long userId, Integer status, Date startCreateDate,
            Date endCreateDate, String paymentType, Integer pageIndex, Integer pageSize) {
        QueryHandler queryHandler = getQueryHandler("from TradeAccountHistory bean");
        if (null != siteId) {
            queryHandler.condition("bean.siteId = :siteId").setParameter("siteId", siteId);
        }
        if (CommonUtils.notEmpty(accountId)) {
            queryHandler.condition("bean.accountId = :accountId").setParameter("accountId", accountId);
        }
        if (CommonUtils.notEmpty(userId)) {
            queryHandler.condition("bean.userId = :userId").setParameter("userId", userId);
        }
        if (CommonUtils.notEmpty(status)) {
            queryHandler.condition("bean.status = :status").setParameter("status", status);
        }
        if (null != startCreateDate) {
            queryHandler.condition("bean.createDate > :startCreateDate").setParameter("startCreateDate", startCreateDate);
        }
        if (null != endCreateDate) {
            queryHandler.condition("bean.createDate <= :endCreateDate").setParameter("endCreateDate", endCreateDate);
        }
        if (!ORDERTYPE_ASC.equalsIgnoreCase(paymentType)) {
            paymentType = ORDERTYPE_DESC;
        }
        queryHandler.order("bean.createDate ").append(paymentType);
        return getPage(queryHandler, pageIndex, pageSize);
    }

    @Override
    protected TradeAccountHistory init(TradeAccountHistory entity) {
        if (null == entity.getCreateDate()) {
            entity.setCreateDate(CommonUtils.getDate());
        }
        return entity;
    }

}