package cn.ac.cags.logic.service.dde;

// Generated 2021-5-9 16:49:30 by com.publiccms.common.generator.SourceGenerator

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import cn.ac.cags.entities.dde.Zircon;
import cn.ac.cags.logic.dao.dde.ZirconDao;
import com.publiccms.common.base.BaseService;
import com.publiccms.common.handler.PageHandler;

/**
 *
 * ZirconService
 * 
 */
@Service
@Transactional
public class ZirconService extends BaseService<Zircon> {

    /**
     * @param sampleId
     * @param oraginalSampleId
     * @param pointNum
     * @param hfType
     * @param testAge
     * @param yb176Hf177
     * @param lu176Hf177
     * @param sigma2LuHf
     * @param hf176Hf177
     * @param sigma2HfHf
     * @param hf176Hf177T
     * @param churT
     * @param dmT
     * @param epsilonHfT
     * @param sigma2EpsilonHfT
     * @param FLuHf
     * @param tdm1
     * @param sigma2Tdm1
     * @param tdm2
     * @param sigma2Tdm2
     * @param epsilonHf0
     * @param d18o
     * @param epsilonD180
     * @param epsilonD18oControl
     * @param siO2
     * @param lithology
     * @param mineralType
     * @param grainsNumber
     * @param chiSquareProbability
     * @param centralAge
     * @param centralAgeError
     * @param pooledAge
     * @param pooledAgeError
     * @param meanTrackLength
     * @param lengthError
     * @param UThHeAge
     * @param UThHeAgeError
     * @param articleRef
     * @param articleDoi
     * @param orderField
     * @param orderType
     * @param pageIndex
     * @param pageSize
     * @return results page
     */
    @Transactional(readOnly = true)
    public PageHandler getPage(String sampleId, String oraginalSampleId, 
                String pointNum, String hfType, Double testAge, 
                Double yb176Hf177, Double lu176Hf177, Double sigma2LuHf, 
                Double hf176Hf177, Double sigma2HfHf, Double hf176Hf177T, 
                Double churT, Double dmT, Double epsilonHfT, 
                Double sigma2EpsilonHfT, Double FLuHf, Double tdm1, 
                Double sigma2Tdm1, Double tdm2, Double sigma2Tdm2, 
                Double epsilonHf0, Double d18o, Double epsilonD180, 
                Double epsilonD18oControl, Double siO2, String lithology, 
                String mineralType, Double grainsNumber, Double chiSquareProbability, 
                Double centralAge, Double centralAgeError, Double pooledAge, 
                Double pooledAgeError, Double meanTrackLength, Double lengthError, 
                Double UThHeAge, Double UThHeAgeError, String articleRef, 
                String articleDoi, 
                String orderField, String orderType, Integer pageIndex, Integer pageSize) {
        return dao.getPage(sampleId, oraginalSampleId, 
                pointNum, hfType, testAge, 
                yb176Hf177, lu176Hf177, sigma2LuHf, 
                hf176Hf177, sigma2HfHf, hf176Hf177T, 
                churT, dmT, epsilonHfT, 
                sigma2EpsilonHfT, FLuHf, tdm1, 
                sigma2Tdm1, tdm2, sigma2Tdm2, 
                epsilonHf0, d18o, epsilonD180, 
                epsilonD18oControl, siO2, lithology, 
                mineralType, grainsNumber, chiSquareProbability, 
                centralAge, centralAgeError, pooledAge, 
                pooledAgeError, meanTrackLength, lengthError, 
                UThHeAge, UThHeAgeError, articleRef, 
                articleDoi, 
                orderField, orderType, pageIndex, pageSize);
    }
    
    @Autowired
    private ZirconDao dao;
    
}