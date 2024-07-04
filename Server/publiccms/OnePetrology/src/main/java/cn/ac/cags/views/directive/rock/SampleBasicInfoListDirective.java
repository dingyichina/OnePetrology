package cn.ac.cags.views.directive.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator
import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import cn.ac.cags.logic.service.rock.SampleBasicInfoService;
import com.publiccms.common.base.AbstractTemplateDirective;
import com.publiccms.common.handler.RenderHandler;
import com.publiccms.common.handler.PageHandler;

/**
 *
 * SampleBasicInfoListDirective
 * 
 */
@Component
public class SampleBasicInfoListDirective extends AbstractTemplateDirective {

    @Override
    public void execute(RenderHandler handler) throws IOException, Exception {
        PageHandler page = service.getPage(handler.getString("sampleId"), handler.getString("originalSampleId"), 
                handler.getString("countryCode"), handler.getString("location"), handler.getString("lithology"), 
                handler.getString("rockName"), handler.getString("rockCode"), handler.getString("era"), 
                handler.getString("geobodyName"), handler.getString("geobodyCode"), handler.getString("tectonicLocation"), 
                handler.getString("primaryStructuralUnit"), handler.getString("secondaryStructuralUnit"), handler.getString("tertiarySturcturalUnit"), 
                handler.getString("surroundingRockAge"), handler.getString("surroundingRockLithology"), handler.getString("relationshipWithSurroundingRock"), 
                handler.getString("form"), handler.getBoolean("isCutAreaConstructionLine"), handler.getString("degreeOfDeformation"), 
                handler.getString("characteristicMinerals"), handler.getString("geneticType"), handler.getString("tectonicType"), 
                handler.getString("sourceOfStructuralTypeDiscrimination"), handler.getString("alkalinity"), handler.getString("aluminumQuality"), 
                handler.getString("collector"), handler.getString("collectorOrg"), handler.getString("reviewer"), 
                handler.getString("analyzeOrg"), handler.getString("analyzePerson"), handler.getString("testObject"), 
                handler.getString("testDate"), handler.getString("testMethod"), handler.getString("articleDoi"), 
                handler.getBoolean("hasChecked"), 
                handler.getString("orderField"), handler.getString("orderType"), handler.getInteger("pageIndex",1), handler.getInteger("pageSize",30));
        handler.put("page", page).render();
    }

    @Autowired
    private SampleBasicInfoService service;

}