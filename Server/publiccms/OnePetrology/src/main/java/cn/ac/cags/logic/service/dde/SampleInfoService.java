package cn.ac.cags.logic.service.dde;

// Generated 2021-7-29 15:30:09 by com.publiccms.common.generator.SourceGenerator

import cn.ac.cags.entities.dde.SampleInfo;
import cn.ac.cags.logic.dao.dde.SampleInfoDao;
import cn.ac.cags.logic.mapper.SampleInfoMapper;
import com.publiccms.common.base.BaseService;
import com.publiccms.common.handler.PageHandler;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

/**
 *
 * SampleInfoService
 * 
 */
@Service
@Transactional
public class SampleInfoService extends BaseService<SampleInfo> {

    /**
     * added by sunchao initial geoage selection
     */
    static double doubleArray[][] = {{0,65.5},{0,2.6},{0,0.01},{0.01,2.6},{0.01,1.8},{1.8,2.6},{2.6,65.5},{2.6,23},{
            2.6,5.3},{2.6,3.6},{3.6,5.3},{5.3,23},{5.3,7.2},{7.3,11.6},{11.6,13.8},{13.8,16},{16,20.4},{20.4,23},{
            23,33.9},{23,28.4},{28.4,33.9},{33.9,55.8},{33.9,37.2},{37.2,40.4},{40.4,48.6},{48.6,55.8},{55.8,65.5},{
            55.8,58.7},{58.7,61.7},{61.7,65.5},{65.5,251},{65.5,145.5},{65.5,99.6},{65.5,70.6},{70.6,83.5},{83.5,
            85.8},{85.8,89.3},{89.3,93.5},{93.5,99.6},{99.6,145.5},{99.6,112},{112,125},{125,130},{130,136},{136,
            140},{140,145.5},{145.5,201.6},{145.5,161},{145.5,151},{151,156},{156,161},{161,176},{161,165},{165,168},{
            168,172},{172,176},{176,201.6},{176,183},{183,190},{190,197},{197,201.6},{201.6,251},{201.6,235},{201.6,
            204},{204,228},{228,235},{235,245},{235,241},{241,245},{245,251},{245,250},{250,251},{251,542},{251,
            299},{251,260},{251,254},{254,260},{260,271},{260,266},{266,268},{268,271},{271,299},{271,276},{276,
            284},{284,297},{297,299},{299,359},{299,318},{299,304},{304,306},{306,312},{312,318},{318,359},{318,
            326},{326,345},{345,359},{359,416},{359,385},{359,374},{374,385},{385,398},{385,392},{392,398},{398,
            416},{398,407},{407,411},{411,416},{416,444},{416,423},{416,419},{419,421},{421,423},{423,428},{423,
            426},{426,428},{428,444},{428,436},{436,439},{439,444},{444,488},{444,461},{444,446},{446,455},{455,
            461},{461,472},{461,468},{468,472},{472,488},{472,479},{479,488},{488,542},{488,501},{488,492},{492,
            496},{496,501},{501,510},{501,503},{503,507},{507,510},{510,521},{510,517},{517,521},{521,542},{521,
            535},{535,542},{542,3850},{542,2500},{542,1000},{542,630},{630,850},{850,1000},{1000,1600},{1000,1200},{
            1200,1400},{1400,1600},{1600,2500},{1600,1800},{1800,2050},{2050,2300},{2300,2500},{2500,3850},{2500,
            2800},{2800,3200},{3200,3600},{3600,3850},{3850,10000}};


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
    @Transactional(readOnly = true)
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
        return dao.getPage(sampleId, oraginalSampleId, 
                location, regionLocation, locationType, 
                tectonicLocation, tectonicType, lithology, 
                lithologyOrigin, occurrence, intrusion, 
                pluton, plutonOrigin, rockName, 
                rockCode, era, geobodyName, 
                geobodyCode, surroundingRockAge, surroundingRockLithology, 
                relationshipWithSurroundingRock, form, whetherToCutAreaConstructionLine, 
                degreeOfDeformation, characteristicMinerals, miningArea, 
                oreType, geneticType, age, 
                ageError, ageSelected, ageSelectedError, 
                testObject, testMethod, primaryStructuralUnit, 
                secondaryStructuralUnit, tertiaryStructuralUnit, sourceOfStructuralTypeDiscrimination, 
                alkalinity, aluminumQuality, photo, 
                collector, collectorOrg, reviewer, 
                analyzeOrg, analyzePerson, testDate, 
                dataSource, articleDoi, remark, 
                refAuthor, refYear, refMagazine, 
                issuePage, refTitle, refOrigin, 
                refMagazineOrigin, refTitleOrigin, sio2, 
                tio2, al2o3, fe2o3, 
                feo, fe2o3t, feot, 
                tfe, mno, mgo, 
                cao, na2o, k2o, 
                p2o5, h2op, h2on, 
                co2, so3, f, 
                cl, loi, total, 
                la, ce, pr, 
                nd, pm, sm, 
                eu, gd, tb, 
                dy, ho, er, 
                tm, yb, lu, 
                y, sc, totalReElement, 
                v, cr, co, 
                ni, mn, cu, 
                zn, ga, ge, 
                cs, rb, ba, 
                th, u, nb, 
                ta, ti, p, 
                pb, sr, zr, 
                hf, li, be, 
                w, pt, pd, 
                os, ir, ru, 
                rh, srisotope, ndisotope, 
                rb87Sr86, sr87Sr86M, sm147Nd144, 
                nd143Nd144, testRockMa, sr87Sr86I, 
                nd143Nd144TChur, nd143Nd144I, FSmNdS, 
                epsilonNd0, epsilonNdT, tdmMa, 
                tdm2Ma, hfisotope, hfPointnum, 
                hfNormalnum, epsilonHftMin, epsilonHftMax, 
                epsilonHftMedian, epsilonHftAverage, tdmcMin, 
                tdmcMax, tdmcMedian, tdmcAverage, 
                hfoisotope, d18oMin, d18oMax, 
                d18oAverage, d18oMedian, 
                orderField, orderType, pageIndex, pageSize);
    }
    
    @Autowired
    private SampleInfoDao dao;
    @Autowired
    private SampleInfoMapper mapper;  //mybatis方式的

    /**
     * 得到polygon中的全部样品点
     * @param polygon
     * @return
     */
    public List<SampleInfo> queryPolygon(String polygon ) {
        return mapper.queryPolygon4all(polygon);
    }

    /**
     * 得到polygon中的全部样品点
     * @return
     */
    public List<SampleInfo> query4GeoCloud() {
        return mapper.query4GeoCloud();
    }

    /**
     * added by sunchao
     * @param age
     * @param ageMin
     * @param ageMax
     * @return
     */
    public List<SampleInfo> queryByAgeInterval(Double age, Double ageMin, Double ageMax) {
        return mapper.queryByAgeInterval(age,ageMin,ageMax);
    }

    /**
     * added by sunchao
     * @param age
     * @return
     */
    public List<SampleInfo> queryByAge(Double age) {
        return mapper.queryByAge(age);
    }

    /**
     * added by sunchao
     * @param geoage
     * @return
     */
    public List<SampleInfo> queryByGeoAge(Double geoage) {
        double age=0,ageMin=0,ageMax=10000;
        ageMin=doubleArray[(int) (geoage-1)][0];
        ageMax=doubleArray[(int) (geoage-1)][1];
        System.out.println("age="+age+";agemin="+ageMin+";ageMAX="+ageMax);
        return mapper.queryByAgeInterval(age,ageMin,ageMax);
    }


    //added by sunchao
    public List<SampleInfo> queryAgedSampleListAll() {
        return mapper.queryAgedSampleListAll();
    }

    //added by sunchao
    public List<SampleInfo> queryByChem(String sqlString) {
        List<SampleInfo> sampleList =mapper.queryByMajorElement(sqlString);


        return sampleList;
    }

}
