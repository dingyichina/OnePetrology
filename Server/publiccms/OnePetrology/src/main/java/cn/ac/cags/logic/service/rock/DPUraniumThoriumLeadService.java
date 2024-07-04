package cn.ac.cags.logic.service.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import cn.ac.cags.entities.rock.DPUraniumThoriumLead;
import cn.ac.cags.logic.dao.rock.DPUraniumThoriumLeadDao;
import com.publiccms.common.base.BaseService;
import com.publiccms.common.handler.PageHandler;

/**
 *
 * DPUraniumThoriumLeadService
 * 
 */
@Service
@Transactional
public class DPUraniumThoriumLeadService extends BaseService<DPUraniumThoriumLead> {

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
    private DPUraniumThoriumLeadDao dao;
    
}