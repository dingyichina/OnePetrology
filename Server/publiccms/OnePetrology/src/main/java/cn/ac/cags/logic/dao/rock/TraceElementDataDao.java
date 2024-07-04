package cn.ac.cags.logic.dao.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator

import org.springframework.stereotype.Repository;

import com.publiccms.common.base.BaseDao;
import com.publiccms.common.constants.CommonConstants;
import com.publiccms.common.handler.PageHandler;
import com.publiccms.common.handler.QueryHandler;
import com.publiccms.common.tools.CommonUtils;
import cn.ac.cags.entities.rock.TraceElementData;
/**
 *
 * TraceElementDataDao
 * 
 */
@Repository
public class TraceElementDataDao extends BaseDao<TraceElementData> {
    
    /**
     * @param sampleId
     * @param orderType
     * @param pageIndex
     * @param pageSize
     * @return results page
     */
    public PageHandler getPage(Integer sampleId, 
                String orderType, Integer pageIndex, Integer pageSize) {
        QueryHandler queryHandler = getQueryHandler("from TraceElementData bean");
        if (CommonUtils.notEmpty(sampleId)) {
            queryHandler.condition("bean.sampleId = :sampleId").setParameter("sampleId", sampleId);
        }
        if(!ORDERTYPE_ASC.equalsIgnoreCase(orderType)){
            orderType = ORDERTYPE_DESC;
        }
        queryHandler.order("bean.sampleId " + orderType);
        return getPage(queryHandler, pageIndex, pageSize);
    }

    @Override
    protected TraceElementData init(TraceElementData entity) {
        return entity;
    }

}