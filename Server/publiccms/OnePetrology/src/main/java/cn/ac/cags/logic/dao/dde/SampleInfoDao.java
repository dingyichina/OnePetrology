package cn.ac.cags.logic.dao.dde;

// Generated 2021-7-29 15:30:09 by com.publiccms.common.generator.SourceGenerator

import org.springframework.stereotype.Repository;

import com.publiccms.common.base.BaseDao;
import com.publiccms.common.constants.CommonConstants;
import com.publiccms.common.handler.PageHandler;
import com.publiccms.common.handler.QueryHandler;
import com.publiccms.common.tools.CommonUtils;
import cn.ac.cags.entities.dde.SampleInfo;
/**
 *
 * SampleInfoDao
 * 
 */
@Repository
public class SampleInfoDao extends BaseDao<SampleInfo> {
    
    /**
     * @param sampleId
     * @param oraginalSampleId
     * @param location
     * @param regionLocation
     * @param locationType
     * @param tectonicLocation
     * @param tectonicType
     * @param lithology
     * @param lithologyOrigin
     * @param occurrence
     * @param intrusion
     * @param pluton
     * @param plutonOrigin
     * @param rockName
     * @param rockCode
     * @param era
     * @param geobodyName
     * @param geobodyCode
     * @param surroundingRockAge
     * @param surroundingRockLithology
     * @param relationshipWithSurroundingRock
     * @param form
     * @param whetherToCutAreaConstructionLine
     * @param degreeOfDeformation
     * @param characteristicMinerals
     * @param miningArea
     * @param oreType
     * @param geneticType
     * @param age
     * @param ageError
     * @param ageSelected
     * @param ageSelectedError
     * @param testObject
     * @param testMethod
     * @param primaryStructuralUnit
     * @param secondaryStructuralUnit
     * @param tertiaryStructuralUnit
     * @param sourceOfStructuralTypeDiscrimination
     * @param alkalinity
     * @param aluminumQuality
     * @param photo
     * @param collector
     * @param collectorOrg
     * @param reviewer
     * @param analyzeOrg
     * @param analyzePerson
     * @param testDate
     * @param dataSource
     * @param articleDoi
     * @param remark
     * @param refAuthor
     * @param refYear
     * @param refMagazine
     * @param issuePage
     * @param refTitle
     * @param refOrigin
     * @param refMagazineOrigin
     * @param refTitleOrigin
     * @param sio2
     * @param tio2
     * @param al2o3
     * @param fe2o3
     * @param feo
     * @param fe2o3t
     * @param feot
     * @param tfe
     * @param mno
     * @param mgo
     * @param cao
     * @param na2o
     * @param k2o
     * @param p2o5
     * @param h2op
     * @param h2on
     * @param co2
     * @param so3
     * @param f
     * @param cl
     * @param loi
     * @param total
     * @param la
     * @param ce
     * @param pr
     * @param nd
     * @param pm
     * @param sm
     * @param eu
     * @param gd
     * @param tb
     * @param dy
     * @param ho
     * @param er
     * @param tm
     * @param yb
     * @param lu
     * @param y
     * @param sc
     * @param totalReElement
     * @param v
     * @param cr
     * @param co
     * @param ni
     * @param mn
     * @param cu
     * @param zn
     * @param ga
     * @param ge
     * @param cs
     * @param rb
     * @param ba
     * @param th
     * @param u
     * @param nb
     * @param ta
     * @param ti
     * @param p
     * @param pb
     * @param sr
     * @param zr
     * @param hf
     * @param li
     * @param be
     * @param w
     * @param pt
     * @param pd
     * @param os
     * @param ir
     * @param ru
     * @param rh
     * @param srisotope
     * @param ndisotope
     * @param rb87Sr86
     * @param sr87Sr86M
     * @param sm147Nd144
     * @param nd143Nd144
     * @param testRockMa
     * @param sr87Sr86I
     * @param nd143Nd144TChur
     * @param nd143Nd144I
     * @param FSmNdS
     * @param epsilonNd0
     * @param epsilonNdT
     * @param tdmMa
     * @param tdm2Ma
     * @param hfisotope
     * @param hfPointnum
     * @param hfNormalnum
     * @param epsilonHftMin
     * @param epsilonHftMax
     * @param epsilonHftMedian
     * @param epsilonHftAverage
     * @param tdmcMin
     * @param tdmcMax
     * @param tdmcMedian
     * @param tdmcAverage
     * @param hfoisotope
     * @param d18oMin
     * @param d18oMax
     * @param d18oAverage
     * @param d18oMedian
     * @param orderField
     * @param orderType
     * @param pageIndex
     * @param pageSize
     * @return results page
     */
    public PageHandler getPage(String sampleId, String oraginalSampleId, 
                String location, String regionLocation, String locationType, 
                String tectonicLocation, String tectonicType, String lithology, 
                String lithologyOrigin, String occurrence, String intrusion, 
                String pluton, String plutonOrigin, String rockName, 
                String rockCode, String era, String geobodyName, 
                String geobodyCode, String surroundingRockAge, String surroundingRockLithology, 
                String relationshipWithSurroundingRock, String form, String whetherToCutAreaConstructionLine, 
                String degreeOfDeformation, String characteristicMinerals, String miningArea, 
                String oreType, String geneticType, Double age, 
                Double ageError, Double ageSelected, Double ageSelectedError, 
                String testObject, String testMethod, String primaryStructuralUnit, 
                String secondaryStructuralUnit, String tertiaryStructuralUnit, String sourceOfStructuralTypeDiscrimination, 
                String alkalinity, String aluminumQuality, String photo, 
                String collector, String collectorOrg, String reviewer, 
                String analyzeOrg, String analyzePerson, String testDate, 
                String dataSource, String articleDoi, String remark, 
                String refAuthor, String refYear, String refMagazine, 
                String issuePage, String refTitle, String refOrigin, 
                String refMagazineOrigin, String refTitleOrigin, Double sio2, 
                Double tio2, Double al2o3, Double fe2o3, 
                Double feo, Double fe2o3t, Double feot, 
                Double tfe, Double mno, Double mgo, 
                Double cao, Double na2o, Double k2o, 
                Double p2o5, Double h2op, Double h2on, 
                Double co2, Double so3, Double f, 
                Double cl, Double loi, Double total, 
                Double la, Double ce, Double pr, 
                Double nd, Double pm, Double sm, 
                Double eu, Double gd, Double tb, 
                Double dy, Double ho, Double er, 
                Double tm, Double yb, Double lu, 
                Double y, Double sc, Double totalReElement, 
                Double v, Double cr, Double co, 
                Double ni, Double mn, Double cu, 
                Double zn, Double ga, Double ge, 
                Double cs, Double rb, Double ba, 
                Double th, Double u, Double nb, 
                Double ta, Double ti, Double p, 
                Double pb, Double sr, Double zr, 
                Double hf, Double li, Double be, 
                Double w, Double pt, Double pd, 
                Double os, Double ir, Double ru, 
                Double rh, String srisotope, String ndisotope, 
                Double rb87Sr86, Double sr87Sr86M, Double sm147Nd144, 
                Double nd143Nd144, Double testRockMa, Double sr87Sr86I, 
                Double nd143Nd144TChur, Double nd143Nd144I, Double FSmNdS, 
                Double epsilonNd0, Double epsilonNdT, Double tdmMa, 
                Double tdm2Ma, String hfisotope, Integer hfPointnum, 
                Double hfNormalnum, Double epsilonHftMin, Double epsilonHftMax, 
                Double epsilonHftMedian, Double epsilonHftAverage, Double tdmcMin, 
                Double tdmcMax, Double tdmcMedian, Double tdmcAverage, 
                String hfoisotope, Double d18oMin, Double d18oMax, 
                Double d18oAverage, Double d18oMedian, 
                String orderField, String orderType, Integer pageIndex, Integer pageSize) {
        QueryHandler queryHandler = getQueryHandler("from SampleInfo bean");
        if (CommonUtils.notEmpty(sampleId)) {
            queryHandler.condition("bean.sampleId = :sampleId").setParameter("sampleId", sampleId);
        }
        if (CommonUtils.notEmpty(oraginalSampleId)) {
            queryHandler.condition("bean.oraginalSampleId = :oraginalSampleId").setParameter("oraginalSampleId", oraginalSampleId);
        }
        if (CommonUtils.notEmpty(location)) {
            queryHandler.condition("bean.location like :location").setParameter("location", like(location));
        }
        if (CommonUtils.notEmpty(regionLocation)) {
            queryHandler.condition("bean.regionLocation like :regionLocation").setParameter("regionLocation", like(regionLocation));
        }
        if (CommonUtils.notEmpty(locationType)) {
            queryHandler.condition("bean.locationType like :locationType").setParameter("locationType", like(locationType));
        }
        if (CommonUtils.notEmpty(tectonicLocation)) {
            queryHandler.condition("bean.tectonicLocation like :tectonicLocation").setParameter("tectonicLocation", like(tectonicLocation));
        }
        if (CommonUtils.notEmpty(tectonicType)) {
            queryHandler.condition("bean.tectonicType like :tectonicType").setParameter("tectonicType", like(tectonicType));
        }
        if (CommonUtils.notEmpty(lithology)) {
            queryHandler.condition("bean.lithology like :lithology").setParameter("lithology", like(lithology));
        }
        if (CommonUtils.notEmpty(lithologyOrigin)) {
            queryHandler.condition("bean.lithologyOrigin like :lithologyOrigin").setParameter("lithologyOrigin", like(lithologyOrigin));
        }
        if (CommonUtils.notEmpty(occurrence)) {
            queryHandler.condition("bean.occurrence like :occurrence").setParameter("occurrence", like(occurrence));
        }
        if (CommonUtils.notEmpty(intrusion)) {
            queryHandler.condition("bean.intrusion like :intrusion").setParameter("intrusion", like(intrusion));
        }
        if (CommonUtils.notEmpty(pluton)) {
            queryHandler.condition("bean.pluton like :pluton").setParameter("pluton", like(pluton));
        }
        if (CommonUtils.notEmpty(plutonOrigin)) {
            queryHandler.condition("bean.plutonOrigin like :plutonOrigin").setParameter("plutonOrigin", like(plutonOrigin));
        }
        if (CommonUtils.notEmpty(rockName)) {
            queryHandler.condition("bean.rockName like :rockName").setParameter("rockName", like(rockName));
        }
        if (CommonUtils.notEmpty(rockCode)) {
            queryHandler.condition("bean.rockCode like :rockCode").setParameter("rockCode", like(rockCode));
        }
        if (CommonUtils.notEmpty(era)) {
            queryHandler.condition("bean.era like :era").setParameter("era", like(era));
        }
        if (CommonUtils.notEmpty(geobodyName)) {
            queryHandler.condition("bean.geobodyName like :geobodyName").setParameter("geobodyName", like(geobodyName));
        }
        if (CommonUtils.notEmpty(geobodyCode)) {
            queryHandler.condition("bean.geobodyCode like :geobodyCode").setParameter("geobodyCode", like(geobodyCode));
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
        if (CommonUtils.notEmpty(whetherToCutAreaConstructionLine)) {
            queryHandler.condition("bean.whetherToCutAreaConstructionLine like :whetherToCutAreaConstructionLine").setParameter("whetherToCutAreaConstructionLine", like(whetherToCutAreaConstructionLine));
        }
        if (CommonUtils.notEmpty(degreeOfDeformation)) {
            queryHandler.condition("bean.degreeOfDeformation like :degreeOfDeformation").setParameter("degreeOfDeformation", like(degreeOfDeformation));
        }
        if (CommonUtils.notEmpty(characteristicMinerals)) {
            queryHandler.condition("bean.characteristicMinerals like :characteristicMinerals").setParameter("characteristicMinerals", like(characteristicMinerals));
        }
        if (CommonUtils.notEmpty(miningArea)) {
            queryHandler.condition("bean.miningArea like :miningArea").setParameter("miningArea", like(miningArea));
        }
        if (CommonUtils.notEmpty(oreType)) {
            queryHandler.condition("bean.oreType like :oreType").setParameter("oreType", like(oreType));
        }
        if (CommonUtils.notEmpty(geneticType)) {
            queryHandler.condition("bean.geneticType like :geneticType").setParameter("geneticType", like(geneticType));
        }
        if (null != age) {
            queryHandler.condition("bean.age = :age").setParameter("age", age);
        }
        if (null != ageError) {
            queryHandler.condition("bean.ageError = :ageError").setParameter("ageError", ageError);
        }
        if (null != ageSelected) {
            queryHandler.condition("bean.ageSelected = :ageSelected").setParameter("ageSelected", ageSelected);
        }
        if (null != ageSelectedError) {
            queryHandler.condition("bean.ageSelectedError = :ageSelectedError").setParameter("ageSelectedError", ageSelectedError);
        }
        if (CommonUtils.notEmpty(testObject)) {
            queryHandler.condition("bean.testObject like :testObject").setParameter("testObject", like(testObject));
        }
        if (CommonUtils.notEmpty(testMethod)) {
            queryHandler.condition("bean.testMethod like :testMethod").setParameter("testMethod", like(testMethod));
        }
        if (CommonUtils.notEmpty(primaryStructuralUnit)) {
            queryHandler.condition("bean.primaryStructuralUnit like :primaryStructuralUnit").setParameter("primaryStructuralUnit", like(primaryStructuralUnit));
        }
        if (CommonUtils.notEmpty(secondaryStructuralUnit)) {
            queryHandler.condition("bean.secondaryStructuralUnit like :secondaryStructuralUnit").setParameter("secondaryStructuralUnit", like(secondaryStructuralUnit));
        }
        if (CommonUtils.notEmpty(tertiaryStructuralUnit)) {
            queryHandler.condition("bean.tertiaryStructuralUnit like :tertiaryStructuralUnit").setParameter("tertiaryStructuralUnit", like(tertiaryStructuralUnit));
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
        if (CommonUtils.notEmpty(photo)) {
            queryHandler.condition("bean.photo like :photo").setParameter("photo", like(photo));
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
        if (CommonUtils.notEmpty(testDate)) {
            queryHandler.condition("bean.testDate like :testDate").setParameter("testDate", like(testDate));
        }
        if (CommonUtils.notEmpty(dataSource)) {
            queryHandler.condition("bean.dataSource like :dataSource").setParameter("dataSource", like(dataSource));
        }
        if (CommonUtils.notEmpty(articleDoi)) {
            queryHandler.condition("bean.articleDoi like :articleDoi").setParameter("articleDoi", like(articleDoi));
        }
        if (CommonUtils.notEmpty(remark)) {
            queryHandler.condition("bean.remark like :remark").setParameter("remark", like(remark));
        }
        if (CommonUtils.notEmpty(refAuthor)) {
            queryHandler.condition("bean.refAuthor like :refAuthor").setParameter("refAuthor", like(refAuthor));
        }
        if (CommonUtils.notEmpty(refYear)) {
            queryHandler.condition("bean.refYear like :refYear").setParameter("refYear", like(refYear));
        }
        if (CommonUtils.notEmpty(refMagazine)) {
            queryHandler.condition("bean.refMagazine like :refMagazine").setParameter("refMagazine", like(refMagazine));
        }
        if (CommonUtils.notEmpty(issuePage)) {
            queryHandler.condition("bean.issuePage like :issuePage").setParameter("issuePage", like(issuePage));
        }
        if (CommonUtils.notEmpty(refTitle)) {
            queryHandler.condition("bean.refTitle like :refTitle").setParameter("refTitle", like(refTitle));
        }
        if (CommonUtils.notEmpty(refOrigin)) {
            queryHandler.condition("bean.refOrigin like :refOrigin").setParameter("refOrigin", like(refOrigin));
        }
        if (CommonUtils.notEmpty(refMagazineOrigin)) {
            queryHandler.condition("bean.refMagazineOrigin like :refMagazineOrigin").setParameter("refMagazineOrigin", like(refMagazineOrigin));
        }
        if (CommonUtils.notEmpty(refTitleOrigin)) {
            queryHandler.condition("bean.refTitleOrigin like :refTitleOrigin").setParameter("refTitleOrigin", like(refTitleOrigin));
        }
        if (null != sio2) {
            queryHandler.condition("bean.sio2 = :sio2").setParameter("sio2", sio2);
        }
        if (null != tio2) {
            queryHandler.condition("bean.tio2 = :tio2").setParameter("tio2", tio2);
        }
        if (null != al2o3) {
            queryHandler.condition("bean.al2o3 = :al2o3").setParameter("al2o3", al2o3);
        }
        if (null != fe2o3) {
            queryHandler.condition("bean.fe2o3 = :fe2o3").setParameter("fe2o3", fe2o3);
        }
        if (null != feo) {
            queryHandler.condition("bean.feo = :feo").setParameter("feo", feo);
        }
        if (null != fe2o3t) {
            queryHandler.condition("bean.fe2o3t = :fe2o3t").setParameter("fe2o3t", fe2o3t);
        }
        if (null != feot) {
            queryHandler.condition("bean.feot = :feot").setParameter("feot", feot);
        }
        if (null != tfe) {
            queryHandler.condition("bean.tfe = :tfe").setParameter("tfe", tfe);
        }
        if (null != mno) {
            queryHandler.condition("bean.mno = :mno").setParameter("mno", mno);
        }
        if (null != mgo) {
            queryHandler.condition("bean.mgo = :mgo").setParameter("mgo", mgo);
        }
        if (null != cao) {
            queryHandler.condition("bean.cao = :cao").setParameter("cao", cao);
        }
        if (null != na2o) {
            queryHandler.condition("bean.na2o = :na2o").setParameter("na2o", na2o);
        }
        if (null != k2o) {
            queryHandler.condition("bean.k2o = :k2o").setParameter("k2o", k2o);
        }
        if (null != p2o5) {
            queryHandler.condition("bean.p2o5 = :p2o5").setParameter("p2o5", p2o5);
        }
        if (null != h2op) {
            queryHandler.condition("bean.h2op = :h2op").setParameter("h2op", h2op);
        }
        if (null != h2on) {
            queryHandler.condition("bean.h2on = :h2on").setParameter("h2on", h2on);
        }
        if (null != co2) {
            queryHandler.condition("bean.co2 = :co2").setParameter("co2", co2);
        }
        if (null != so3) {
            queryHandler.condition("bean.so3 = :so3").setParameter("so3", so3);
        }
        if (null != f) {
            queryHandler.condition("bean.f = :f").setParameter("f", f);
        }
        if (null != cl) {
            queryHandler.condition("bean.cl = :cl").setParameter("cl", cl);
        }
        if (null != loi) {
            queryHandler.condition("bean.loi = :loi").setParameter("loi", loi);
        }
        if (null != total) {
            queryHandler.condition("bean.total = :total").setParameter("total", total);
        }
        if (null != la) {
            queryHandler.condition("bean.la = :la").setParameter("la", la);
        }
        if (null != ce) {
            queryHandler.condition("bean.ce = :ce").setParameter("ce", ce);
        }
        if (null != pr) {
            queryHandler.condition("bean.pr = :pr").setParameter("pr", pr);
        }
        if (null != nd) {
            queryHandler.condition("bean.nd = :nd").setParameter("nd", nd);
        }
        if (null != pm) {
            queryHandler.condition("bean.pm = :pm").setParameter("pm", pm);
        }
        if (null != sm) {
            queryHandler.condition("bean.sm = :sm").setParameter("sm", sm);
        }
        if (null != eu) {
            queryHandler.condition("bean.eu = :eu").setParameter("eu", eu);
        }
        if (null != gd) {
            queryHandler.condition("bean.gd = :gd").setParameter("gd", gd);
        }
        if (null != tb) {
            queryHandler.condition("bean.tb = :tb").setParameter("tb", tb);
        }
        if (null != dy) {
            queryHandler.condition("bean.dy = :dy").setParameter("dy", dy);
        }
        if (null != ho) {
            queryHandler.condition("bean.ho = :ho").setParameter("ho", ho);
        }
        if (null != er) {
            queryHandler.condition("bean.er = :er").setParameter("er", er);
        }
        if (null != tm) {
            queryHandler.condition("bean.tm = :tm").setParameter("tm", tm);
        }
        if (null != yb) {
            queryHandler.condition("bean.yb = :yb").setParameter("yb", yb);
        }
        if (null != lu) {
            queryHandler.condition("bean.lu = :lu").setParameter("lu", lu);
        }
        if (null != y) {
            queryHandler.condition("bean.y = :y").setParameter("y", y);
        }
        if (null != sc) {
            queryHandler.condition("bean.sc = :sc").setParameter("sc", sc);
        }
        if (null != totalReElement) {
            queryHandler.condition("bean.totalReElement = :totalReElement").setParameter("totalReElement", totalReElement);
        }
        if (null != v) {
            queryHandler.condition("bean.v = :v").setParameter("v", v);
        }
        if (null != cr) {
            queryHandler.condition("bean.cr = :cr").setParameter("cr", cr);
        }
        if (null != co) {
            queryHandler.condition("bean.co = :co").setParameter("co", co);
        }
        if (null != ni) {
            queryHandler.condition("bean.ni = :ni").setParameter("ni", ni);
        }
        if (null != mn) {
            queryHandler.condition("bean.mn = :mn").setParameter("mn", mn);
        }
        if (null != cu) {
            queryHandler.condition("bean.cu = :cu").setParameter("cu", cu);
        }
        if (null != zn) {
            queryHandler.condition("bean.zn = :zn").setParameter("zn", zn);
        }
        if (null != ga) {
            queryHandler.condition("bean.ga = :ga").setParameter("ga", ga);
        }
        if (null != ge) {
            queryHandler.condition("bean.ge = :ge").setParameter("ge", ge);
        }
        if (null != cs) {
            queryHandler.condition("bean.cs = :cs").setParameter("cs", cs);
        }
        if (null != rb) {
            queryHandler.condition("bean.rb = :rb").setParameter("rb", rb);
        }
        if (null != ba) {
            queryHandler.condition("bean.ba = :ba").setParameter("ba", ba);
        }
        if (null != th) {
            queryHandler.condition("bean.th = :th").setParameter("th", th);
        }
        if (null != u) {
            queryHandler.condition("bean.u = :u").setParameter("u", u);
        }
        if (null != nb) {
            queryHandler.condition("bean.nb = :nb").setParameter("nb", nb);
        }
        if (null != ta) {
            queryHandler.condition("bean.ta = :ta").setParameter("ta", ta);
        }
        if (null != ti) {
            queryHandler.condition("bean.ti = :ti").setParameter("ti", ti);
        }
        if (null != p) {
            queryHandler.condition("bean.p = :p").setParameter("p", p);
        }
        if (null != pb) {
            queryHandler.condition("bean.pb = :pb").setParameter("pb", pb);
        }
        if (null != sr) {
            queryHandler.condition("bean.sr = :sr").setParameter("sr", sr);
        }
        if (null != zr) {
            queryHandler.condition("bean.zr = :zr").setParameter("zr", zr);
        }
        if (null != hf) {
            queryHandler.condition("bean.hf = :hf").setParameter("hf", hf);
        }
        if (null != li) {
            queryHandler.condition("bean.li = :li").setParameter("li", li);
        }
        if (null != be) {
            queryHandler.condition("bean.be = :be").setParameter("be", be);
        }
        if (null != w) {
            queryHandler.condition("bean.w = :w").setParameter("w", w);
        }
        if (null != pt) {
            queryHandler.condition("bean.pt = :pt").setParameter("pt", pt);
        }
        if (null != pd) {
            queryHandler.condition("bean.pd = :pd").setParameter("pd", pd);
        }
        if (null != os) {
            queryHandler.condition("bean.os = :os").setParameter("os", os);
        }
        if (null != ir) {
            queryHandler.condition("bean.ir = :ir").setParameter("ir", ir);
        }
        if (null != ru) {
            queryHandler.condition("bean.ru = :ru").setParameter("ru", ru);
        }
        if (null != rh) {
            queryHandler.condition("bean.rh = :rh").setParameter("rh", rh);
        }
        if (CommonUtils.notEmpty(srisotope)) {
            queryHandler.condition("bean.srisotope like :srisotope").setParameter("srisotope", like(srisotope));
        }
        if (CommonUtils.notEmpty(ndisotope)) {
            queryHandler.condition("bean.ndisotope like :ndisotope").setParameter("ndisotope", like(ndisotope));
        }
        if (null != rb87Sr86) {
            queryHandler.condition("bean.rb87Sr86 = :rb87Sr86").setParameter("rb87Sr86", rb87Sr86);
        }
        if (null != sr87Sr86M) {
            queryHandler.condition("bean.sr87Sr86M = :sr87Sr86M").setParameter("sr87Sr86M", sr87Sr86M);
        }
        if (null != sm147Nd144) {
            queryHandler.condition("bean.sm147Nd144 = :sm147Nd144").setParameter("sm147Nd144", sm147Nd144);
        }
        if (null != nd143Nd144) {
            queryHandler.condition("bean.nd143Nd144 = :nd143Nd144").setParameter("nd143Nd144", nd143Nd144);
        }
        if (null != testRockMa) {
            queryHandler.condition("bean.testRockMa = :testRockMa").setParameter("testRockMa", testRockMa);
        }
        if (null != sr87Sr86I) {
            queryHandler.condition("bean.sr87Sr86I = :sr87Sr86I").setParameter("sr87Sr86I", sr87Sr86I);
        }
        if (null != nd143Nd144TChur) {
            queryHandler.condition("bean.nd143Nd144TChur = :nd143Nd144TChur").setParameter("nd143Nd144TChur", nd143Nd144TChur);
        }
        if (null != nd143Nd144I) {
            queryHandler.condition("bean.nd143Nd144I = :nd143Nd144I").setParameter("nd143Nd144I", nd143Nd144I);
        }
        if (null != FSmNdS) {
            queryHandler.condition("bean.FSmNdS = :FSmNdS").setParameter("FSmNdS", FSmNdS);
        }
        if (null != epsilonNd0) {
            queryHandler.condition("bean.epsilonNd0 = :epsilonNd0").setParameter("epsilonNd0", epsilonNd0);
        }
        if (null != epsilonNdT) {
            queryHandler.condition("bean.epsilonNdT = :epsilonNdT").setParameter("epsilonNdT", epsilonNdT);
        }
        if (null != tdmMa) {
            queryHandler.condition("bean.tdmMa = :tdmMa").setParameter("tdmMa", tdmMa);
        }
        if (null != tdm2Ma) {
            queryHandler.condition("bean.tdm2Ma = :tdm2Ma").setParameter("tdm2Ma", tdm2Ma);
        }
        if (CommonUtils.notEmpty(hfisotope)) {
            queryHandler.condition("bean.hfisotope like :hfisotope").setParameter("hfisotope", like(hfisotope));
        }
        if (CommonUtils.notEmpty(hfPointnum)) {
            queryHandler.condition("bean.hfPointnum = :hfPointnum").setParameter("hfPointnum", hfPointnum);
        }
        if (null != hfNormalnum) {
            queryHandler.condition("bean.hfNormalnum = :hfNormalnum").setParameter("hfNormalnum", hfNormalnum);
        }
        if (null != epsilonHftMin) {
            queryHandler.condition("bean.epsilonHftMin = :epsilonHftMin").setParameter("epsilonHftMin", epsilonHftMin);
        }
        if (null != epsilonHftMax) {
            queryHandler.condition("bean.epsilonHftMax = :epsilonHftMax").setParameter("epsilonHftMax", epsilonHftMax);
        }
        if (null != epsilonHftMedian) {
            queryHandler.condition("bean.epsilonHftMedian = :epsilonHftMedian").setParameter("epsilonHftMedian", epsilonHftMedian);
        }
        if (null != epsilonHftAverage) {
            queryHandler.condition("bean.epsilonHftAverage = :epsilonHftAverage").setParameter("epsilonHftAverage", epsilonHftAverage);
        }
        if (null != tdmcMin) {
            queryHandler.condition("bean.tdmcMin = :tdmcMin").setParameter("tdmcMin", tdmcMin);
        }
        if (null != tdmcMax) {
            queryHandler.condition("bean.tdmcMax = :tdmcMax").setParameter("tdmcMax", tdmcMax);
        }
        if (null != tdmcMedian) {
            queryHandler.condition("bean.tdmcMedian = :tdmcMedian").setParameter("tdmcMedian", tdmcMedian);
        }
        if (null != tdmcAverage) {
            queryHandler.condition("bean.tdmcAverage = :tdmcAverage").setParameter("tdmcAverage", tdmcAverage);
        }
        if (CommonUtils.notEmpty(hfoisotope)) {
            queryHandler.condition("bean.hfoisotope like :hfoisotope").setParameter("hfoisotope", like(hfoisotope));
        }
        if (null != d18oMin) {
            queryHandler.condition("bean.d18oMin = :d18oMin").setParameter("d18oMin", d18oMin);
        }
        if (null != d18oMax) {
            queryHandler.condition("bean.d18oMax = :d18oMax").setParameter("d18oMax", d18oMax);
        }
        if (null != d18oAverage) {
            queryHandler.condition("bean.d18oAverage = :d18oAverage").setParameter("d18oAverage", d18oAverage);
        }
        if (null != d18oMedian) {
            queryHandler.condition("bean.d18oMedian = :d18oMedian").setParameter("d18oMedian", d18oMedian);
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
            case "longitude" : queryHandler.order("bean.longitude " + orderType); break;
            case "latitude" : queryHandler.order("bean.latitude " + orderType); break;
            case "location" : queryHandler.order("bean.location " + orderType); break;
            case "regionLocation" : queryHandler.order("bean.regionLocation " + orderType); break;
            case "locationType" : queryHandler.order("bean.locationType " + orderType); break;
            case "tectonicLocation" : queryHandler.order("bean.tectonicLocation " + orderType); break;
            case "tectonicType" : queryHandler.order("bean.tectonicType " + orderType); break;
            case "lithology" : queryHandler.order("bean.lithology " + orderType); break;
            case "lithologyOrigin" : queryHandler.order("bean.lithologyOrigin " + orderType); break;
            case "occurrence" : queryHandler.order("bean.occurrence " + orderType); break;
            case "intrusion" : queryHandler.order("bean.intrusion " + orderType); break;
            case "pluton" : queryHandler.order("bean.pluton " + orderType); break;
            case "plutonOrigin" : queryHandler.order("bean.plutonOrigin " + orderType); break;
            case "rockName" : queryHandler.order("bean.rockName " + orderType); break;
            case "rockCode" : queryHandler.order("bean.rockCode " + orderType); break;
            case "era" : queryHandler.order("bean.era " + orderType); break;
            case "geobodyName" : queryHandler.order("bean.geobodyName " + orderType); break;
            case "geobodyCode" : queryHandler.order("bean.geobodyCode " + orderType); break;
            case "surroundingRockAge" : queryHandler.order("bean.surroundingRockAge " + orderType); break;
            case "surroundingRockLithology" : queryHandler.order("bean.surroundingRockLithology " + orderType); break;
            case "relationshipWithSurroundingRock" : queryHandler.order("bean.relationshipWithSurroundingRock " + orderType); break;
            case "form" : queryHandler.order("bean.form " + orderType); break;
            case "whetherToCutAreaConstructionLine" : queryHandler.order("bean.whetherToCutAreaConstructionLine " + orderType); break;
            case "degreeOfDeformation" : queryHandler.order("bean.degreeOfDeformation " + orderType); break;
            case "characteristicMinerals" : queryHandler.order("bean.characteristicMinerals " + orderType); break;
            case "miningArea" : queryHandler.order("bean.miningArea " + orderType); break;
            case "oreType" : queryHandler.order("bean.oreType " + orderType); break;
            case "geneticType" : queryHandler.order("bean.geneticType " + orderType); break;
            case "age" : queryHandler.order("bean.age " + orderType); break;
            case "ageError" : queryHandler.order("bean.ageError " + orderType); break;
            case "ageSelected" : queryHandler.order("bean.ageSelected " + orderType); break;
            case "ageSelectedError" : queryHandler.order("bean.ageSelectedError " + orderType); break;
            case "testObject" : queryHandler.order("bean.testObject " + orderType); break;
            case "testMethod" : queryHandler.order("bean.testMethod " + orderType); break;
            case "primaryStructuralUnit" : queryHandler.order("bean.primaryStructuralUnit " + orderType); break;
            case "secondaryStructuralUnit" : queryHandler.order("bean.secondaryStructuralUnit " + orderType); break;
            case "tertiaryStructuralUnit" : queryHandler.order("bean.tertiaryStructuralUnit " + orderType); break;
            case "sourceOfStructuralTypeDiscrimination" : queryHandler.order("bean.sourceOfStructuralTypeDiscrimination " + orderType); break;
            case "alkalinity" : queryHandler.order("bean.alkalinity " + orderType); break;
            case "aluminumQuality" : queryHandler.order("bean.aluminumQuality " + orderType); break;
            case "photo" : queryHandler.order("bean.photo " + orderType); break;
            case "collector" : queryHandler.order("bean.collector " + orderType); break;
            case "collectorOrg" : queryHandler.order("bean.collectorOrg " + orderType); break;
            case "reviewer" : queryHandler.order("bean.reviewer " + orderType); break;
            case "analyzeOrg" : queryHandler.order("bean.analyzeOrg " + orderType); break;
            case "analyzePerson" : queryHandler.order("bean.analyzePerson " + orderType); break;
            case "testDate" : queryHandler.order("bean.testDate " + orderType); break;
            case "dataSource" : queryHandler.order("bean.dataSource " + orderType); break;
            case "articleDoi" : queryHandler.order("bean.articleDoi " + orderType); break;
            case "remark" : queryHandler.order("bean.remark " + orderType); break;
            case "refAuthor" : queryHandler.order("bean.refAuthor " + orderType); break;
            case "refYear" : queryHandler.order("bean.refYear " + orderType); break;
            case "refMagazine" : queryHandler.order("bean.refMagazine " + orderType); break;
            case "issuePage" : queryHandler.order("bean.issuePage " + orderType); break;
            case "refTitle" : queryHandler.order("bean.refTitle " + orderType); break;
            case "refOrigin" : queryHandler.order("bean.refOrigin " + orderType); break;
            case "refMagazineOrigin" : queryHandler.order("bean.refMagazineOrigin " + orderType); break;
            case "refTitleOrigin" : queryHandler.order("bean.refTitleOrigin " + orderType); break;
            case "sio2" : queryHandler.order("bean.sio2 " + orderType); break;
            case "tio2" : queryHandler.order("bean.tio2 " + orderType); break;
            case "al2o3" : queryHandler.order("bean.al2o3 " + orderType); break;
            case "fe2o3" : queryHandler.order("bean.fe2o3 " + orderType); break;
            case "feo" : queryHandler.order("bean.feo " + orderType); break;
            case "fe2o3t" : queryHandler.order("bean.fe2o3t " + orderType); break;
            case "feot" : queryHandler.order("bean.feot " + orderType); break;
            case "tfe" : queryHandler.order("bean.tfe " + orderType); break;
            case "mno" : queryHandler.order("bean.mno " + orderType); break;
            case "mgo" : queryHandler.order("bean.mgo " + orderType); break;
            case "cao" : queryHandler.order("bean.cao " + orderType); break;
            case "na2o" : queryHandler.order("bean.na2o " + orderType); break;
            case "k2o" : queryHandler.order("bean.k2o " + orderType); break;
            case "p2o5" : queryHandler.order("bean.p2o5 " + orderType); break;
            case "h2op" : queryHandler.order("bean.h2op " + orderType); break;
            case "h2on" : queryHandler.order("bean.h2on " + orderType); break;
            case "co2" : queryHandler.order("bean.co2 " + orderType); break;
            case "so3" : queryHandler.order("bean.so3 " + orderType); break;
            case "f" : queryHandler.order("bean.f " + orderType); break;
            case "cl" : queryHandler.order("bean.cl " + orderType); break;
            case "loi" : queryHandler.order("bean.loi " + orderType); break;
            case "total" : queryHandler.order("bean.total " + orderType); break;
            case "la" : queryHandler.order("bean.la " + orderType); break;
            case "ce" : queryHandler.order("bean.ce " + orderType); break;
            case "pr" : queryHandler.order("bean.pr " + orderType); break;
            case "nd" : queryHandler.order("bean.nd " + orderType); break;
            case "pm" : queryHandler.order("bean.pm " + orderType); break;
            case "sm" : queryHandler.order("bean.sm " + orderType); break;
            case "eu" : queryHandler.order("bean.eu " + orderType); break;
            case "gd" : queryHandler.order("bean.gd " + orderType); break;
            case "tb" : queryHandler.order("bean.tb " + orderType); break;
            case "dy" : queryHandler.order("bean.dy " + orderType); break;
            case "ho" : queryHandler.order("bean.ho " + orderType); break;
            case "er" : queryHandler.order("bean.er " + orderType); break;
            case "tm" : queryHandler.order("bean.tm " + orderType); break;
            case "yb" : queryHandler.order("bean.yb " + orderType); break;
            case "lu" : queryHandler.order("bean.lu " + orderType); break;
            case "y" : queryHandler.order("bean.y " + orderType); break;
            case "sc" : queryHandler.order("bean.sc " + orderType); break;
            case "totalReElement" : queryHandler.order("bean.totalReElement " + orderType); break;
            case "v" : queryHandler.order("bean.v " + orderType); break;
            case "cr" : queryHandler.order("bean.cr " + orderType); break;
            case "co" : queryHandler.order("bean.co " + orderType); break;
            case "ni" : queryHandler.order("bean.ni " + orderType); break;
            case "mn" : queryHandler.order("bean.mn " + orderType); break;
            case "cu" : queryHandler.order("bean.cu " + orderType); break;
            case "zn" : queryHandler.order("bean.zn " + orderType); break;
            case "ga" : queryHandler.order("bean.ga " + orderType); break;
            case "ge" : queryHandler.order("bean.ge " + orderType); break;
            case "cs" : queryHandler.order("bean.cs " + orderType); break;
            case "rb" : queryHandler.order("bean.rb " + orderType); break;
            case "ba" : queryHandler.order("bean.ba " + orderType); break;
            case "th" : queryHandler.order("bean.th " + orderType); break;
            case "u" : queryHandler.order("bean.u " + orderType); break;
            case "nb" : queryHandler.order("bean.nb " + orderType); break;
            case "ta" : queryHandler.order("bean.ta " + orderType); break;
            case "ti" : queryHandler.order("bean.ti " + orderType); break;
            case "p" : queryHandler.order("bean.p " + orderType); break;
            case "pb" : queryHandler.order("bean.pb " + orderType); break;
            case "sr" : queryHandler.order("bean.sr " + orderType); break;
            case "zr" : queryHandler.order("bean.zr " + orderType); break;
            case "hf" : queryHandler.order("bean.hf " + orderType); break;
            case "li" : queryHandler.order("bean.li " + orderType); break;
            case "be" : queryHandler.order("bean.be " + orderType); break;
            case "w" : queryHandler.order("bean.w " + orderType); break;
            case "pt" : queryHandler.order("bean.pt " + orderType); break;
            case "pd" : queryHandler.order("bean.pd " + orderType); break;
            case "os" : queryHandler.order("bean.os " + orderType); break;
            case "ir" : queryHandler.order("bean.ir " + orderType); break;
            case "ru" : queryHandler.order("bean.ru " + orderType); break;
            case "rh" : queryHandler.order("bean.rh " + orderType); break;
            case "srisotope" : queryHandler.order("bean.srisotope " + orderType); break;
            case "ndisotope" : queryHandler.order("bean.ndisotope " + orderType); break;
            case "rb87Sr86" : queryHandler.order("bean.rb87Sr86 " + orderType); break;
            case "sr87Sr86M" : queryHandler.order("bean.sr87Sr86M " + orderType); break;
            case "sm147Nd144" : queryHandler.order("bean.sm147Nd144 " + orderType); break;
            case "nd143Nd144" : queryHandler.order("bean.nd143Nd144 " + orderType); break;
            case "testRockMa" : queryHandler.order("bean.testRockMa " + orderType); break;
            case "sr87Sr86I" : queryHandler.order("bean.sr87Sr86I " + orderType); break;
            case "nd143Nd144TChur" : queryHandler.order("bean.nd143Nd144TChur " + orderType); break;
            case "nd143Nd144I" : queryHandler.order("bean.nd143Nd144I " + orderType); break;
            case "FSmNdS" : queryHandler.order("bean.FSmNdS " + orderType); break;
            case "epsilonNd0" : queryHandler.order("bean.epsilonNd0 " + orderType); break;
            case "epsilonNdT" : queryHandler.order("bean.epsilonNdT " + orderType); break;
            case "tdmMa" : queryHandler.order("bean.tdmMa " + orderType); break;
            case "tdm2Ma" : queryHandler.order("bean.tdm2Ma " + orderType); break;
            case "hfisotope" : queryHandler.order("bean.hfisotope " + orderType); break;
            case "hfPointnum" : queryHandler.order("bean.hfPointnum " + orderType); break;
            case "hfNormalnum" : queryHandler.order("bean.hfNormalnum " + orderType); break;
            case "epsilonHftMin" : queryHandler.order("bean.epsilonHftMin " + orderType); break;
            case "epsilonHftMax" : queryHandler.order("bean.epsilonHftMax " + orderType); break;
            case "epsilonHftMedian" : queryHandler.order("bean.epsilonHftMedian " + orderType); break;
            case "epsilonHftAverage" : queryHandler.order("bean.epsilonHftAverage " + orderType); break;
            case "tdmcMin" : queryHandler.order("bean.tdmcMin " + orderType); break;
            case "tdmcMax" : queryHandler.order("bean.tdmcMax " + orderType); break;
            case "tdmcMedian" : queryHandler.order("bean.tdmcMedian " + orderType); break;
            case "tdmcAverage" : queryHandler.order("bean.tdmcAverage " + orderType); break;
            case "hfoisotope" : queryHandler.order("bean.hfoisotope " + orderType); break;
            case "d18oMin" : queryHandler.order("bean.d18oMin " + orderType); break;
            case "d18oMax" : queryHandler.order("bean.d18oMax " + orderType); break;
            case "d18oAverage" : queryHandler.order("bean.d18oAverage " + orderType); break;
            case "d18oMedian" : queryHandler.order("bean.d18oMedian " + orderType); break;
            default : queryHandler.order("bean.id " + orderType);
        }
        return getPage(queryHandler, pageIndex, pageSize);
    }

    @Override
    protected SampleInfo init(SampleInfo entity) {
        return entity;
    }

}