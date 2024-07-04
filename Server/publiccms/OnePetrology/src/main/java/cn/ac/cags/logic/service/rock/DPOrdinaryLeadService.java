package cn.ac.cags.logic.service.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import cn.ac.cags.entities.rock.DPOrdinaryLead;
import cn.ac.cags.logic.dao.rock.DPOrdinaryLeadDao;
import com.publiccms.common.base.BaseService;
import com.publiccms.common.handler.PageHandler;

/**
 *
 * DPOrdinaryLeadService
 * 
 */
@Service
@Transactional
public class DPOrdinaryLeadService extends BaseService<DPOrdinaryLead> {

    /**
     * @param pageIndex
     * @param pageSize
     * @return results page
     */
    @Transactional(readOnly = true)
    public PageHandler getPage(
                Integer pageIndex, Integer pageSize) {
        return dao.getPage(
                pageIndex, pageSize);
    }
    
    @Autowired
    private DPOrdinaryLeadDao dao;
    
}