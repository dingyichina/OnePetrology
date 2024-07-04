package cn.ac.cags.logic.service.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import cn.ac.cags.entities.rock.AbbreviatedAnalysisData;
import cn.ac.cags.logic.dao.rock.AbbreviatedAnalysisDataDao;
import com.publiccms.common.base.BaseService;
import com.publiccms.common.handler.PageHandler;

/**
 *
 * AbbreviatedAnalysisDataService
 * 
 */
@Service
@Transactional
public class AbbreviatedAnalysisDataService extends BaseService<AbbreviatedAnalysisData> {

    /**
     * @param analyzeItem
     * @param orderType
     * @param pageIndex
     * @param pageSize
     * @return results page
     */
    @Transactional(readOnly = true)
    public PageHandler getPage(String analyzeItem, 
                String orderType, Integer pageIndex, Integer pageSize) {
        return dao.getPage(analyzeItem, 
                orderType, pageIndex, pageSize);
    }
    
    @Autowired
    private AbbreviatedAnalysisDataDao dao;
    
}