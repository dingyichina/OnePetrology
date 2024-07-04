package cn.ac.cags.logic.dao.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator

import org.springframework.stereotype.Repository;

import com.publiccms.common.base.BaseDao;
import com.publiccms.common.constants.CommonConstants;
import com.publiccms.common.handler.PageHandler;
import com.publiccms.common.handler.QueryHandler;
import com.publiccms.common.tools.CommonUtils;
import cn.ac.cags.entities.rock.DPCarbon14;
/**
 *
 * DPCarbon14Dao
 * 
 */
@Repository
public class DPCarbon14Dao extends BaseDao<DPCarbon14> {
    
    /**
     * @param pageIndex
     * @param pageSize
     * @return results page
     */
    public PageHandler getPage(
                Integer pageIndex, Integer pageSize) {
        QueryHandler queryHandler = getQueryHandler("from DPCarbon14 bean");
        queryHandler.order("bean.id desc");
        return getPage(queryHandler, pageIndex, pageSize);
    }

    @Override
    protected DPCarbon14 init(DPCarbon14 entity) {
        return entity;
    }

}