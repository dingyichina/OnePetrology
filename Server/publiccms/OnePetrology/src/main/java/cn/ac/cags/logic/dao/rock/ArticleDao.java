package cn.ac.cags.logic.dao.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator

import org.springframework.stereotype.Repository;

import com.publiccms.common.base.BaseDao;
import com.publiccms.common.constants.CommonConstants;
import com.publiccms.common.handler.PageHandler;
import com.publiccms.common.handler.QueryHandler;
import com.publiccms.common.tools.CommonUtils;
import cn.ac.cags.entities.rock.Article;
/**
 *
 * ArticleDao
 * 
 */
@Repository
public class ArticleDao extends BaseDao<Article> {
    
    /**
     * @param articleName
     * @param orderType
     * @param pageIndex
     * @param pageSize
     * @return results page
     */
    public PageHandler getPage(String articleName, 
                String orderType, Integer pageIndex, Integer pageSize) {
        QueryHandler queryHandler = getQueryHandler("from Article bean");
        if (CommonUtils.notEmpty(articleName)) {
            queryHandler.condition("bean.articleName like :articleName").setParameter("articleName", like(articleName));
        }
        if(!ORDERTYPE_ASC.equalsIgnoreCase(orderType)){
            orderType = ORDERTYPE_DESC;
        }
        queryHandler.order("bean.articleName " + orderType);
        return getPage(queryHandler, pageIndex, pageSize);
    }

    @Override
    protected Article init(Article entity) {
        return entity;
    }

}