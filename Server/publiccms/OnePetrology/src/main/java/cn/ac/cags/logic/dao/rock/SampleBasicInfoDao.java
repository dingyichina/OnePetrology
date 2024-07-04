package cn.ac.cags.logic.dao.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator

import org.springframework.stereotype.Repository;

import com.publiccms.common.base.BaseDao;
import com.publiccms.common.constants.CommonConstants;
import com.publiccms.common.handler.PageHandler;
import com.publiccms.common.handler.QueryHandler;
import com.publiccms.common.tools.CommonUtils;
import cn.ac.cags.entities.rock.SampleBasicInfo;
/**
 *
 * SampleBasicInfoDao
 * 
 */
@Repository
public class SampleBasicInfoDao extends BaseDao<SampleBasicInfo> {
    
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
        QueryHandler queryHandler = getQueryHandler("from SampleBasicInfo bean");
        if (CommonUtils.notEmpty(sampleId)) {
            queryHandler.condition("bean.sampleId = :sampleId").setParameter("sampleId", sampleId);
        }
        if (CommonUtils.notEmpty(originalSampleId)) {
            queryHandler.condition("bean.originalSampleId = :originalSampleId").setParameter("originalSampleId", originalSampleId);
        }
        if (CommonUtils.notEmpty(countryCode)) {
            queryHandler.condition("bean.countryCode = :countryCode").setParameter("countryCode", countryCode);
        }
        if (CommonUtils.notEmpty(location)) {
            queryHandler.condition("bean.location like :location").setParameter("location", like(location));
        }
        if (CommonUtils.notEmpty(lithology)) {
            queryHandler.condition("bean.lithology = :lithology").setParameter("lithology", lithology);
        }
        if (CommonUtils.notEmpty(rockName)) {
            queryHandler.condition("bean.rockName = :rockName").setParameter("rockName", rockName);
        }
        if (CommonUtils.notEmpty(rockCode)) {
            queryHandler.condition("bean.rockCode = :rockCode").setParameter("rockCode", rockCode);
        }
        if (CommonUtils.notEmpty(era)) {
            queryHandler.condition("bean.era = :era").setParameter("era", era);
        }
        if (CommonUtils.notEmpty(geobodyName)) {
            queryHandler.condition("bean.geobodyName = :geobodyName").setParameter("geobodyName", geobodyName);
        }
        if (CommonUtils.notEmpty(geobodyCode)) {
            queryHandler.condition("bean.geobodyCode = :geobodyCode").setParameter("geobodyCode", geobodyCode);
        }
        if (CommonUtils.notEmpty(tectonicLocation)) {
            queryHandler.condition("bean.tectonicLocation like :tectonicLocation").setParameter("tectonicLocation", like(tectonicLocation));
        }
        if (CommonUtils.notEmpty(primaryStructuralUnit)) {
            queryHandler.condition("bean.primaryStructuralUnit like :primaryStructuralUnit").setParameter("primaryStructuralUnit", like(primaryStructuralUnit));
        }
        if (CommonUtils.notEmpty(secondaryStructuralUnit)) {
            queryHandler.condition("bean.secondaryStructuralUnit like :secondaryStructuralUnit").setParameter("secondaryStructuralUnit", like(secondaryStructuralUnit));
        }
        if (CommonUtils.notEmpty(tertiarySturcturalUnit)) {
            queryHandler.condition("bean.tertiarySturcturalUnit like :tertiarySturcturalUnit").setParameter("tertiarySturcturalUnit", like(tertiarySturcturalUnit));
        }
        if (CommonUtils.notEmpty(surroundingRockAge)) {
            queryHandler.condition("bean.surroundingRockAge like :surroundingRockAge").setParameter("surroundingRockAge", like(surroundingRockAge));
        }
        if (CommonUtils.notEmpty(surroundingRockLithology)) {
            queryHandler.condition("bean.surroundingRockLithology like :surroundingRockLithology").setParameter("surroundingRockLithology", like(surroundingRockLithology));
        }
        if (CommonUtils.notEmpty(relationshipWithSurroundingRock)) {
            queryHandler.condition("bean.relationshipWithSurroundingRock like :relationshipWithSurroundingRock").setParameter("relationshipWithSurroundingRock", like(relationshipWithSurroundingRock));
        }
        if (CommonUtils.notEmpty(form)) {
            queryHandler.condition("bean.form like :form").setParameter("form", like(form));
        }
        if (null != isCutAreaConstructionLine) {
            queryHandler.condition("bean.isCutAreaConstructionLine = :isCutAreaConstructionLine").setParameter("isCutAreaConstructionLine", isCutAreaConstructionLine);
        }
        if (CommonUtils.notEmpty(degreeOfDeformation)) {
            queryHandler.condition("bean.degreeOfDeformation like :degreeOfDeformation").setParameter("degreeOfDeformation", like(degreeOfDeformation));
        }
        if (CommonUtils.notEmpty(characteristicMinerals)) {
            queryHandler.condition("bean.characteristicMinerals like :characteristicMinerals").setParameter("characteristicMinerals", like(characteristicMinerals));
        }
        if (CommonUtils.notEmpty(geneticType)) {
            queryHandler.condition("bean.geneticType like :geneticType").setParameter("geneticType", like(geneticType));
        }
        if (CommonUtils.notEmpty(tectonicType)) {
            queryHandler.condition("bean.tectonicType like :tectonicType").setParameter("tectonicType", like(tectonicType));
        }
        if (CommonUtils.notEmpty(sourceOfStructuralTypeDiscrimination)) {
            queryHandler.condition("bean.sourceOfStructuralTypeDiscrimination like :sourceOfStructuralTypeDiscrimination").setParameter("sourceOfStructuralTypeDiscrimination", like(sourceOfStructuralTypeDiscrimination));
        }
        if (CommonUtils.notEmpty(alkalinity)) {
            queryHandler.condition("bean.alkalinity like :alkalinity").setParameter("alkalinity", like(alkalinity));
        }
        if (CommonUtils.notEmpty(aluminumQuality)) {
            queryHandler.condition("bean.aluminumQuality like :aluminumQuality").setParameter("aluminumQuality", like(aluminumQuality));
        }
        if (CommonUtils.notEmpty(collector)) {
            queryHandler.condition("bean.collector like :collector").setParameter("collector", like(collector));
        }
        if (CommonUtils.notEmpty(collectorOrg)) {
            queryHandler.condition("bean.collectorOrg like :collectorOrg").setParameter("collectorOrg", like(collectorOrg));
        }
        if (CommonUtils.notEmpty(reviewer)) {
            queryHandler.condition("bean.reviewer like :reviewer").setParameter("reviewer", like(reviewer));
        }
        if (CommonUtils.notEmpty(analyzeOrg)) {
            queryHandler.condition("bean.analyzeOrg like :analyzeOrg").setParameter("analyzeOrg", like(analyzeOrg));
        }
        if (CommonUtils.notEmpty(analyzePerson)) {
            queryHandler.condition("bean.analyzePerson like :analyzePerson").setParameter("analyzePerson", like(analyzePerson));
        }
        if (CommonUtils.notEmpty(testObject)) {
            queryHandler.condition("bean.testObject like :testObject").setParameter("testObject", like(testObject));
        }
        if (CommonUtils.notEmpty(testDate)) {
            queryHandler.condition("bean.testDate like :testDate").setParameter("testDate", like(testDate));
        }
        if (CommonUtils.notEmpty(testMethod)) {
            queryHandler.condition("bean.testMethod like :testMethod").setParameter("testMethod", like(testMethod));
        }
        if (CommonUtils.notEmpty(articleDoi)) {
            queryHandler.condition("bean.articleDoi like :articleDoi").setParameter("articleDoi", like(articleDoi));
        }
        if (null != hasChecked) {
            queryHandler.condition("bean.hasChecked = :hasChecked").setParameter("hasChecked", hasChecked);
        }
        if(!ORDERTYPE_ASC.equalsIgnoreCase(orderType)){
            orderType = ORDERTYPE_DESC;
        }
        if(null == orderField){
            orderField = CommonConstants.BLANK;
        }
        switch(orderField) {
            case "sampleId" : queryHandler.order("bean.sampleId " + orderType); break;
            case "originalSampleId" : queryHandler.order("bean.originalSampleId " + orderType); break;
            case "longitude" : queryHandler.order("bean.longitude " + orderType); break;
            case "latitude" : queryHandler.order("bean.latitude " + orderType); break;
            case "countryCode" : queryHandler.order("bean.countryCode " + orderType); break;
            case "location" : queryHandler.order("bean.location " + orderType); break;
            case "lithology" : queryHandler.order("bean.lithology " + orderType); break;
            case "rockName" : queryHandler.order("bean.rockName " + orderType); break;
            case "rockCode" : queryHandler.order("bean.rockCode " + orderType); break;
            case "era" : queryHandler.order("bean.era " + orderType); break;
            case "geobodyName" : queryHandler.order("bean.geobodyName " + orderType); break;
            case "geobodyCode" : queryHandler.order("bean.geobodyCode " + orderType); break;
            case "tectonicLocation" : queryHandler.order("bean.tectonicLocation " + orderType); break;
            case "primaryStructuralUnit" : queryHandler.order("bean.primaryStructuralUnit " + orderType); break;
            case "secondaryStructuralUnit" : queryHandler.order("bean.secondaryStructuralUnit " + orderType); break;
            case "tertiarySturcturalUnit" : queryHandler.order("bean.tertiarySturcturalUnit " + orderType); break;
            case "surroundingRockAge" : queryHandler.order("bean.surroundingRockAge " + orderType); break;
            case "surroundingRockLithology" : queryHandler.order("bean.surroundingRockLithology " + orderType); break;
            case "relationshipWithSurroundingRock" : queryHandler.order("bean.relationshipWithSurroundingRock " + orderType); break;
            case "form" : queryHandler.order("bean.form " + orderType); break;
            case "isCutAreaConstructionLine" : queryHandler.order("bean.isCutAreaConstructionLine " + orderType); break;
            case "degreeOfDeformation" : queryHandler.order("bean.degreeOfDeformation " + orderType); break;
            case "characteristicMinerals" : queryHandler.order("bean.characteristicMinerals " + orderType); break;
            case "geneticType" : queryHandler.order("bean.geneticType " + orderType); break;
            case "tectonicType" : queryHandler.order("bean.tectonicType " + orderType); break;
            case "sourceOfStructuralTypeDiscrimination" : queryHandler.order("bean.sourceOfStructuralTypeDiscrimination " + orderType); break;
            case "alkalinity" : queryHandler.order("bean.alkalinity " + orderType); break;
            case "aluminumQuality" : queryHandler.order("bean.aluminumQuality " + orderType); break;
            case "age" : queryHandler.order("bean.age " + orderType); break;
            case "ageError" : queryHandler.order("bean.ageError " + orderType); break;
            case "photo" : queryHandler.order("bean.photo " + orderType); break;
            case "collector" : queryHandler.order("bean.collector " + orderType); break;
            case "collectorOrg" : queryHandler.order("bean.collectorOrg " + orderType); break;
            case "reviewer" : queryHandler.order("bean.reviewer " + orderType); break;
            case "analyzeOrg" : queryHandler.order("bean.analyzeOrg " + orderType); break;
            case "analyzePerson" : queryHandler.order("bean.analyzePerson " + orderType); break;
            case "testObject" : queryHandler.order("bean.testObject " + orderType); break;
            case "testDate" : queryHandler.order("bean.testDate " + orderType); break;
            case "testMethod" : queryHandler.order("bean.testMethod " + orderType); break;
            case "ageSelected" : queryHandler.order("bean.ageSelected " + orderType); break;
            case "ageSelectedError" : queryHandler.order("bean.ageSelectedError " + orderType); break;
            case "articleId" : queryHandler.order("bean.articleId " + orderType); break;
            case "articleDoi" : queryHandler.order("bean.articleDoi " + orderType); break;
            case "hasChecked" : queryHandler.order("bean.hasChecked " + orderType); break;
            default : queryHandler.order("bean.id " + orderType);
        }
        return getPage(queryHandler, pageIndex, pageSize);
    }

    @Override
    protected SampleBasicInfo init(SampleBasicInfo entity) {
        return entity;
    }

}