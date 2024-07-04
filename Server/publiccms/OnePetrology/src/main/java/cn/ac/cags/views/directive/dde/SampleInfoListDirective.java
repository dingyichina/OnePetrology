package cn.ac.cags.views.directive.dde;

// Generated 2021-7-29 15:30:09 by com.publiccms.common.generator.SourceGenerator
import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import cn.ac.cags.logic.service.dde.SampleInfoService;
import com.publiccms.common.base.AbstractTemplateDirective;
import com.publiccms.common.handler.RenderHandler;
import com.publiccms.common.handler.PageHandler;

/**
 *
 * SampleInfoListDirective
 * 
 */
@Component
public class SampleInfoListDirective extends AbstractTemplateDirective {

    @Override
    public void execute(RenderHandler handler) throws IOException, Exception {
        PageHandler page = service.getPage(handler.getString("sampleId"), handler.getString("oraginalSampleId"), 
                handler.getString("location"), handler.getString("regionLocation"), handler.getString("locationType"), 
                handler.getString("tectonicLocation"), handler.getString("tectonicType"), handler.getString("lithology"), 
                handler.getString("lithologyOrigin"), handler.getString("occurrence"), handler.getString("intrusion"), 
                handler.getString("pluton"), handler.getString("plutonOrigin"), handler.getString("rockName"), 
                handler.getString("rockCode"), handler.getString("era"), handler.getString("geobodyName"), 
                handler.getString("geobodyCode"), handler.getString("surroundingRockAge"), handler.getString("surroundingRockLithology"), 
                handler.getString("relationshipWithSurroundingRock"), handler.getString("form"), handler.getString("whetherToCutAreaConstructionLine"), 
                handler.getString("degreeOfDeformation"), handler.getString("characteristicMinerals"), handler.getString("miningArea"), 
                handler.getString("oreType"), handler.getString("geneticType"), handler.getDouble("age"), 
                handler.getDouble("ageError"), handler.getDouble("ageSelected"), handler.getDouble("ageSelectedError"), 
                handler.getString("testObject"), handler.getString("testMethod"), handler.getString("primaryStructuralUnit"), 
                handler.getString("secondaryStructuralUnit"), handler.getString("tertiaryStructuralUnit"), handler.getString("sourceOfStructuralTypeDiscrimination"), 
                handler.getString("alkalinity"), handler.getString("aluminumQuality"), handler.getString("photo"), 
                handler.getString("collector"), handler.getString("collectorOrg"), handler.getString("reviewer"), 
                handler.getString("analyzeOrg"), handler.getString("analyzePerson"), handler.getString("testDate"), 
                handler.getString("dataSource"), handler.getString("articleDoi"), handler.getString("remark"), 
                handler.getString("refAuthor"), handler.getString("refYear"), handler.getString("refMagazine"), 
                handler.getString("issuePage"), handler.getString("refTitle"), handler.getString("refOrigin"), 
                handler.getString("refMagazineOrigin"), handler.getString("refTitleOrigin"), handler.getDouble("sio2"), 
                handler.getDouble("tio2"), handler.getDouble("al2o3"), handler.getDouble("fe2o3"), 
                handler.getDouble("feo"), handler.getDouble("fe2o3t"), handler.getDouble("feot"), 
                handler.getDouble("tfe"), handler.getDouble("mno"), handler.getDouble("mgo"), 
                handler.getDouble("cao"), handler.getDouble("na2o"), handler.getDouble("k2o"), 
                handler.getDouble("p2o5"), handler.getDouble("h2op"), handler.getDouble("h2on"), 
                handler.getDouble("co2"), handler.getDouble("so3"), handler.getDouble("f"), 
                handler.getDouble("cl"), handler.getDouble("loi"), handler.getDouble("total"), 
                handler.getDouble("la"), handler.getDouble("ce"), handler.getDouble("pr"), 
                handler.getDouble("nd"), handler.getDouble("pm"), handler.getDouble("sm"), 
                handler.getDouble("eu"), handler.getDouble("gd"), handler.getDouble("tb"), 
                handler.getDouble("dy"), handler.getDouble("ho"), handler.getDouble("er"), 
                handler.getDouble("tm"), handler.getDouble("yb"), handler.getDouble("lu"), 
                handler.getDouble("y"), handler.getDouble("sc"), handler.getDouble("totalReElement"), 
                handler.getDouble("v"), handler.getDouble("cr"), handler.getDouble("co"), 
                handler.getDouble("ni"), handler.getDouble("mn"), handler.getDouble("cu"), 
                handler.getDouble("zn"), handler.getDouble("ga"), handler.getDouble("ge"), 
                handler.getDouble("cs"), handler.getDouble("rb"), handler.getDouble("ba"), 
                handler.getDouble("th"), handler.getDouble("u"), handler.getDouble("nb"), 
                handler.getDouble("ta"), handler.getDouble("ti"), handler.getDouble("p"), 
                handler.getDouble("pb"), handler.getDouble("sr"), handler.getDouble("zr"), 
                handler.getDouble("hf"), handler.getDouble("li"), handler.getDouble("be"), 
                handler.getDouble("w"), handler.getDouble("pt"), handler.getDouble("pd"), 
                handler.getDouble("os"), handler.getDouble("ir"), handler.getDouble("ru"), 
                handler.getDouble("rh"), handler.getString("srisotope"), handler.getString("ndisotope"), 
                handler.getDouble("rb87Sr86"), handler.getDouble("sr87Sr86M"), handler.getDouble("sm147Nd144"), 
                handler.getDouble("nd143Nd144"), handler.getDouble("testRockMa"), handler.getDouble("sr87Sr86I"), 
                handler.getDouble("nd143Nd144TChur"), handler.getDouble("nd143Nd144I"), handler.getDouble("FSmNdS"), 
                handler.getDouble("epsilonNd0"), handler.getDouble("epsilonNdT"), handler.getDouble("tdmMa"), 
                handler.getDouble("tdm2Ma"), handler.getString("hfisotope"), handler.getInteger("hfPointnum"), 
                handler.getDouble("hfNormalnum"), handler.getDouble("epsilonHftMin"), handler.getDouble("epsilonHftMax"), 
                handler.getDouble("epsilonHftMedian"), handler.getDouble("epsilonHftAverage"), handler.getDouble("tdmcMin"), 
                handler.getDouble("tdmcMax"), handler.getDouble("tdmcMedian"), handler.getDouble("tdmcAverage"), 
                handler.getString("hfoisotope"), handler.getDouble("d18oMin"), handler.getDouble("d18oMax"), 
                handler.getDouble("d18oAverage"), handler.getDouble("d18oMedian"), 
                handler.getString("orderField"), handler.getString("orderType"), handler.getInteger("pageIndex",1), handler.getInteger("pageSize",30));
        handler.put("page", page).render();
    }

    @Autowired
    private SampleInfoService service;

}