package cn.ac.cags.logic.dao.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator

import org.springframework.stereotype.Repository;

import com.publiccms.common.base.BaseDao;
import com.publiccms.common.constants.CommonConstants;
import com.publiccms.common.handler.PageHandler;
import com.publiccms.common.handler.QueryHandler;
import com.publiccms.common.tools.CommonUtils;
import cn.ac.cags.entities.rock.AbbreviatedAnalysisData;
/**
 *
 * AbbreviatedAnalysisDataDao
 * 
 */
@Repository
public class AbbreviatedAnalysisDataDao extends BaseDao<AbbreviatedAnalysisData> {
    
    /**
     * @param analyzeItem
     * @param orderType
     * @param pageIndex
     * @param pageSize
     * @return results page
     */
    public PageHandler getPage(String analyzeItem, 
                String orderType, Integer pageIndex, Integer pageSize) {
        QueryHandler queryHandler = getQueryHandler("from AbbreviatedAnalysisData bean");
        if (CommonUtils.notEmpty(analyzeItem)) {
            queryHandler.condition("bean.analyzeItem like :analyzeItem").setParameter("analyzeItem", like(analyzeItem));
        }
        if(!ORDERTYPE_ASC.equalsIgnoreCase(orderType)){
            orderType = ORDERTYPE_DESC;
        }
        queryHandler.order("bean.analyzeItem " + orderType);
        return getPage(queryHandler, pageIndex, pageSize);
    }

    @Override
    protected AbbreviatedAnalysisData init(AbbreviatedAnalysisData entity) {
        return entity;
    }

}