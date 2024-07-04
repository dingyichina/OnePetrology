package cn.ac.cags.logic.service.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import cn.ac.cags.entities.rock.SampleBasicInfo;
import cn.ac.cags.logic.dao.rock.SampleBasicInfoDao;
import com.publiccms.common.base.BaseService;
import com.publiccms.common.handler.PageHandler;

/**
 *
 * SampleBasicInfoService
 * 
 */
@Service
@Transactional
public class SampleBasicInfoService extends BaseService<SampleBasicInfo> {

    /**
     * @param sampleId
     * @param originalSampleId
     * @param countryCode
     * @param location
     * @param lithology
     * @param rockName
     * @param rockCode
     * @param era
     * @param geobodyName
     * @param geobodyCode
     * @param tectonicLocation
     * @param primaryStructuralUnit
     * @param secondaryStructuralUnit
     * @param tertiarySturcturalUnit
     * @param surroundingRockAge
     * @param surroundingRockLithology
     * @param relationshipWithSurroundingRock
     * @param form
     * @param isCutAreaConstructionLine
     * @param degreeOfDeformation
     * @param characteristicMinerals
     * @param geneticType
     * @param tectonicType
     * @param sourceOfStructuralTypeDiscrimination
     * @param alkalinity
     * @param aluminumQuality
     * @param collector
     * @param collectorOrg
     * @param reviewer
     * @param analyzeOrg
     * @param analyzePerson
     * @param testObject
     * @param testDate
     * @param testMethod
     * @param articleDoi
     * @param hasChecked
     * @param orderField
     * @param orderType
     * @param pageIndex
     * @param pageSize
     * @return results page
     */
    @Transactional(readOnly = true)
    public PageHandler getPage(String sampleId, String originalSampleId, 
                String countryCode, String location, String lithology, 
                String rockName, String rockCode, String era, 
                String geobodyName, String geobodyCode, String tectonicLocation, 
                String primaryStructuralUnit, String secondaryStructuralUnit, String tertiarySturcturalUnit, 
                String surroundingRockAge, String surroundingRockLithology, String relationshipWithSurroundingRock, 
                String form, Boolean isCutAreaConstructionLine, String degreeOfDeformation, 
                String characteristicMinerals, String geneticType, String tectonicType, 
                String sourceOfStructuralTypeDiscrimination, String alkalinity, String aluminumQuality, 
                String collector, String collectorOrg, String reviewer, 
                String analyzeOrg, String analyzePerson, String testObject, 
                String testDate, String testMethod, String articleDoi, 
                Boolean hasChecked, 
                String orderField, String orderType, Integer pageIndex, Integer pageSize) {
        return dao.getPage(sampleId, originalSampleId, 
                countryCode, location, lithology, 
                rockName, rockCode, era, 
                geobodyName, geobodyCode, tectonicLocation, 
                primaryStructuralUnit, secondaryStructuralUnit, tertiarySturcturalUnit, 
                surroundingRockAge, surroundingRockLithology, relationshipWithSurroundingRock, 
                form, isCutAreaConstructionLine, degreeOfDeformation, 
                characteristicMinerals, geneticType, tectonicType, 
                sourceOfStructuralTypeDiscrimination, alkalinity, aluminumQuality, 
                collector, collectorOrg, reviewer, 
                analyzeOrg, analyzePerson, testObject, 
                testDate, testMethod, articleDoi, 
                hasChecked, 
                orderField, orderType, pageIndex, pageSize);
    }
    
    @Autowired
    private SampleBasicInfoDao dao;

    /**
     * 把ids的审核结果置为true
     * @param ids
     */
    public void checked(Integer[] ids){
        for (Integer id :ids){
            SampleBasicInfo entity=this.getEntity(id);
            entity.setHasChecked(Boolean.TRUE);
            this.update(id,entity);
        }
    }
    
}