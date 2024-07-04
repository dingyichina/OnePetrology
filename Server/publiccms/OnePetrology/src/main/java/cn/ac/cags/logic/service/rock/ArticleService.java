package cn.ac.cags.logic.service.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import cn.ac.cags.entities.rock.Article;
import cn.ac.cags.logic.dao.rock.ArticleDao;
import com.publiccms.common.base.BaseService;
import com.publiccms.common.handler.PageHandler;

/**
 *
 * ArticleService
 * 
 */
@Service
@Transactional
public class ArticleService extends BaseService<Article> {

    /**
     * @param articleName
     * @param orderType
     * @param pageIndex
     * @param pageSize
     * @return results page
     */
    @Transactional(readOnly = true)
    public PageHandler getPage(String articleName, 
                String orderType, Integer pageIndex, Integer pageSize) {
        return dao.getPage(articleName, 
                orderType, pageIndex, pageSize);
    }
    
    @Autowired
    private ArticleDao dao;

    
}