package cn.ac.cags.logic.dao.dde;

// Generated 2021-5-9 16:49:30 by com.publiccms.common.generator.SourceGenerator

import org.springframework.stereotype.Repository;

import com.publiccms.common.base.BaseDao;
import com.publiccms.common.constants.CommonConstants;
import com.publiccms.common.handler.PageHandler;
import com.publiccms.common.handler.QueryHandler;
import com.publiccms.common.tools.CommonUtils;
import cn.ac.cags.entities.dde.Zircon;
/**
 *
 * ZirconDao
 * 
 */
@Repository
public class ZirconDao extends BaseDao<Zircon> {
    
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
        QueryHandler queryHandler = getQueryHandler("from Zircon bean");
        if (CommonUtils.notEmpty(sampleId)) {
            queryHandler.condition("bean.sampleId like :sampleId").setParameter("sampleId", like(sampleId));
        }
        if (CommonUtils.notEmpty(oraginalSampleId)) {
            queryHandler.condition("bean.oraginalSampleId like :oraginalSampleId").setParameter("oraginalSampleId", like(oraginalSampleId));
        }
        if (CommonUtils.notEmpty(pointNum)) {
            queryHandler.condition("bean.pointNum like :pointNum").setParameter("pointNum", like(pointNum));
        }
        if (CommonUtils.notEmpty(hfType)) {
            queryHandler.condition("bean.hfType like :hfType").setParameter("hfType", like(hfType));
        }
        if (null != testAge) {
            queryHandler.condition("bean.testAge = :testAge").setParameter("testAge", testAge);
        }
        if (null != yb176Hf177) {
            queryHandler.condition("bean.yb176Hf177 = :yb176Hf177").setParameter("yb176Hf177", yb176Hf177);
        }
        if (null != lu176Hf177) {
            queryHandler.condition("bean.lu176Hf177 = :lu176Hf177").setParameter("lu176Hf177", lu176Hf177);
        }
        if (null != sigma2LuHf) {
            queryHandler.condition("bean.sigma2LuHf = :sigma2LuHf").setParameter("sigma2LuHf", sigma2LuHf);
        }
        if (null != hf176Hf177) {
            queryHandler.condition("bean.hf176Hf177 = :hf176Hf177").setParameter("hf176Hf177", hf176Hf177);
        }
        if (null != sigma2HfHf) {
            queryHandler.condition("bean.sigma2HfHf = :sigma2HfHf").setParameter("sigma2HfHf", sigma2HfHf);
        }
        if (null != hf176Hf177T) {
            queryHandler.condition("bean.hf176Hf177T = :hf176Hf177T").setParameter("hf176Hf177T", hf176Hf177T);
        }
        if (null != churT) {
            queryHandler.condition("bean.churT = :churT").setParameter("churT", churT);
        }
        if (null != dmT) {
            queryHandler.condition("bean.dmT = :dmT").setParameter("dmT", dmT);
        }
        if (null != epsilonHfT) {
            queryHandler.condition("bean.epsilonHfT = :epsilonHfT").setParameter("epsilonHfT", epsilonHfT);
        }
        if (null != sigma2EpsilonHfT) {
            queryHandler.condition("bean.sigma2EpsilonHfT = :sigma2EpsilonHfT").setParameter("sigma2EpsilonHfT", sigma2EpsilonHfT);
        }
        if (null != FLuHf) {
            queryHandler.condition("bean.FLuHf = :FLuHf").setParameter("FLuHf", FLuHf);
        }
        if (null != tdm1) {
            queryHandler.condition("bean.tdm1 = :tdm1").setParameter("tdm1", tdm1);
        }
        if (null != sigma2Tdm1) {
            queryHandler.condition("bean.sigma2Tdm1 = :sigma2Tdm1").setParameter("sigma2Tdm1", sigma2Tdm1);
        }
        if (null != tdm2) {
            queryHandler.condition("bean.tdm2 = :tdm2").setParameter("tdm2", tdm2);
        }
        if (null != sigma2Tdm2) {
            queryHandler.condition("bean.sigma2Tdm2 = :sigma2Tdm2").setParameter("sigma2Tdm2", sigma2Tdm2);
        }
        if (null != epsilonHf0) {
            queryHandler.condition("bean.epsilonHf0 = :epsilonHf0").setParameter("epsilonHf0", epsilonHf0);
        }
        if (null != d18o) {
            queryHandler.condition("bean.d18o = :d18o").setParameter("d18o", d18o);
        }
        if (null != epsilonD180) {
            queryHandler.condition("bean.epsilonD180 = :epsilonD180").setParameter("epsilonD180", epsilonD180);
        }
        if (null != epsilonD18oControl) {
            queryHandler.condition("bean.epsilonD18oControl = :epsilonD18oControl").setParameter("epsilonD18oControl", epsilonD18oControl);
        }
        if (null != siO2) {
            queryHandler.condition("bean.siO2 = :siO2").setParameter("siO2", siO2);
        }
        if (CommonUtils.notEmpty(lithology)) {
            queryHandler.condition("bean.lithology like :lithology").setParameter("lithology", like(lithology));
        }
        if (CommonUtils.notEmpty(mineralType)) {
            queryHandler.condition("bean.mineralType like :mineralType").setParameter("mineralType", like(mineralType));
        }
        if (null != grainsNumber) {
            queryHandler.condition("bean.grainsNumber = :grainsNumber").setParameter("grainsNumber", grainsNumber);
        }
        if (null != chiSquareProbability) {
            queryHandler.condition("bean.chiSquareProbability = :chiSquareProbability").setParameter("chiSquareProbability", chiSquareProbability);
        }
        if (null != centralAge) {
            queryHandler.condition("bean.centralAge = :centralAge").setParameter("centralAge", centralAge);
        }
        if (null != centralAgeError) {
            queryHandler.condition("bean.centralAgeError = :centralAgeError").setParameter("centralAgeError", centralAgeError);
        }
        if (null != pooledAge) {
            queryHandler.condition("bean.pooledAge = :pooledAge").setParameter("pooledAge", pooledAge);
        }
        if (null != pooledAgeError) {
            queryHandler.condition("bean.pooledAgeError = :pooledAgeError").setParameter("pooledAgeError", pooledAgeError);
        }
        if (null != meanTrackLength) {
            queryHandler.condition("bean.meanTrackLength = :meanTrackLength").setParameter("meanTrackLength", meanTrackLength);
        }
        if (null != lengthError) {
            queryHandler.condition("bean.lengthError = :lengthError").setParameter("lengthError", lengthError);
        }
        if (null != UThHeAge) {
            queryHandler.condition("bean.UThHeAge = :UThHeAge").setParameter("UThHeAge", UThHeAge);
        }
        if (null != UThHeAgeError) {
            queryHandler.condition("bean.UThHeAgeError = :UThHeAgeError").setParameter("UThHeAgeError", UThHeAgeError);
        }
        if (CommonUtils.notEmpty(articleRef)) {
            queryHandler.condition("bean.articleRef like :articleRef").setParameter("articleRef", like(articleRef));
        }
        if (CommonUtils.notEmpty(articleDoi)) {
            queryHandler.condition("bean.articleDoi like :articleDoi").setParameter("articleDoi", like(articleDoi));
        }
        if(!ORDERTYPE_ASC.equalsIgnoreCase(orderType)){
            orderType = ORDERTYPE_DESC;
        }
        if(null == orderField){
            orderField = CommonConstants.BLANK;
        }
        switch(orderField) {
            case "id" : queryHandler.order("bean.id " + orderType); break;
            case "sampleId" : queryHandler.order("bean.sampleId " + orderType); break;
            case "oraginalSampleId" : queryHandler.order("bean.oraginalSampleId " + orderType); break;
            case "pointNum" : queryHandler.order("bean.pointNum " + orderType); break;
            case "hfType" : queryHandler.order("bean.hfType " + orderType); break;
            case "testAge" : queryHandler.order("bean.testAge " + orderType); break;
            case "yb176Hf177" : queryHandler.order("bean.yb176Hf177 " + orderType); break;
            case "lu176Hf177" : queryHandler.order("bean.lu176Hf177 " + orderType); break;
            case "sigma2LuHf" : queryHandler.order("bean.sigma2LuHf " + orderType); break;
            case "hf176Hf177" : queryHandler.order("bean.hf176Hf177 " + orderType); break;
            case "sigma2HfHf" : queryHandler.order("bean.sigma2HfHf " + orderType); break;
            case "hf176Hf177T" : queryHandler.order("bean.hf176Hf177T " + orderType); break;
            case "churT" : queryHandler.order("bean.churT " + orderType); break;
            case "dmT" : queryHandler.order("bean.dmT " + orderType); break;
            case "epsilonHfT" : queryHandler.order("bean.epsilonHfT " + orderType); break;
            case "sigma2EpsilonHfT" : queryHandler.order("bean.sigma2EpsilonHfT " + orderType); break;
            case "FLuHf" : queryHandler.order("bean.FLuHf " + orderType); break;
            case "tdm1" : queryHandler.order("bean.tdm1 " + orderType); break;
            case "sigma2Tdm1" : queryHandler.order("bean.sigma2Tdm1 " + orderType); break;
            case "tdm2" : queryHandler.order("bean.tdm2 " + orderType); break;
            case "sigma2Tdm2" : queryHandler.order("bean.sigma2Tdm2 " + orderType); break;
            case "epsilonHf0" : queryHandler.order("bean.epsilonHf0 " + orderType); break;
            case "d18o" : queryHandler.order("bean.d18o " + orderType); break;
            case "epsilonD180" : queryHandler.order("bean.epsilonD180 " + orderType); break;
            case "epsilonD18oControl" : queryHandler.order("bean.epsilonD18oControl " + orderType); break;
            case "siO2" : queryHandler.order("bean.siO2 " + orderType); break;
            case "lithology" : queryHandler.order("bean.lithology " + orderType); break;
            case "mineralType" : queryHandler.order("bean.mineralType " + orderType); break;
            case "grainsNumber" : queryHandler.order("bean.grainsNumber " + orderType); break;
            case "chiSquareProbability" : queryHandler.order("bean.chiSquareProbability " + orderType); break;
            case "centralAge" : queryHandler.order("bean.centralAge " + orderType); break;
            case "centralAgeError" : queryHandler.order("bean.centralAgeError " + orderType); break;
            case "pooledAge" : queryHandler.order("bean.pooledAge " + orderType); break;
            case "pooledAgeError" : queryHandler.order("bean.pooledAgeError " + orderType); break;
            case "meanTrackLength" : queryHandler.order("bean.meanTrackLength " + orderType); break;
            case "lengthError" : queryHandler.order("bean.lengthError " + orderType); break;
            case "UThHeAge" : queryHandler.order("bean.UThHeAge " + orderType); break;
            case "UThHeAgeError" : queryHandler.order("bean.UThHeAgeError " + orderType); break;
            case "articleRef" : queryHandler.order("bean.articleRef " + orderType); break;
            case "articleDoi" : queryHandler.order("bean.articleDoi " + orderType); break;
            default : queryHandler.order("bean.id " + orderType);
        }
        return getPage(queryHandler, pageIndex, pageSize);
    }

    @Override
    protected Zircon init(Zircon entity) {
        return entity;
    }

}