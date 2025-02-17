package cn.ac.cags.logic.service.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import cn.ac.cags.entities.rock.RockSectionIdentify;
import cn.ac.cags.logic.dao.rock.RockSectionIdentifyDao;
import com.publiccms.common.base.BaseService;
import com.publiccms.common.handler.PageHandler;

/**
 *
 * RockSectionIdentifyService
 * 
 */
@Service
@Transactional
public class RockSectionIdentifyService extends BaseService<RockSectionIdentify> {

    /**
     * @param sampleId
     * @param orderType
     * @param pageIndex
     * @param pageSize
     * @return results page
     */
    @Transactional(readOnly = true)
    public PageHandler getPage(Integer sampleId, 
                String orderType, Integer pageIndex, Integer pageSize) {
        return dao.getPage(sampleId, 
                orderType, pageIndex, pageSize);
    }
    
    @Autowired
    private RockSectionIdentifyDao dao;
    
}