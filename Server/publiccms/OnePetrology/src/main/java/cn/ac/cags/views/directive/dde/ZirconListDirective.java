package cn.ac.cags.views.directive.dde;

// Generated 2021-5-9 16:49:30 by com.publiccms.common.generator.SourceGenerator
import java.io.IOException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import cn.ac.cags.logic.service.dde.ZirconService;
import com.publiccms.common.base.AbstractTemplateDirective;
import com.publiccms.common.handler.RenderHandler;
import com.publiccms.common.handler.PageHandler;

/**
 *
 * ZirconListDirective
 * 
 */
@Component
public class ZirconListDirective extends AbstractTemplateDirective {

    @Override
    public void execute(RenderHandler handler) throws IOException, Exception {
        PageHandler page = service.getPage(handler.getString("sampleId"), handler.getString("oraginalSampleId"), 
                handler.getString("pointNum"), handler.getString("hfType"), handler.getDouble("testAge"), 
                handler.getDouble("yb176Hf177"), handler.getDouble("lu176Hf177"), handler.getDouble("sigma2LuHf"), 
                handler.getDouble("hf176Hf177"), handler.getDouble("sigma2HfHf"), handler.getDouble("hf176Hf177T"), 
                handler.getDouble("churT"), handler.getDouble("dmT"), handler.getDouble("epsilonHfT"), 
                handler.getDouble("sigma2EpsilonHfT"), handler.getDouble("FLuHf"), handler.getDouble("tdm1"), 
                handler.getDouble("sigma2Tdm1"), handler.getDouble("tdm2"), handler.getDouble("sigma2Tdm2"), 
                handler.getDouble("epsilonHf0"), handler.getDouble("d18o"), handler.getDouble("epsilonD180"), 
                handler.getDouble("epsilonD18oControl"), handler.getDouble("siO2"), handler.getString("lithology"), 
                handler.getString("mineralType"), handler.getDouble("grainsNumber"), handler.getDouble("chiSquareProbability"), 
                handler.getDouble("centralAge"), handler.getDouble("centralAgeError"), handler.getDouble("pooledAge"), 
                handler.getDouble("pooledAgeError"), handler.getDouble("meanTrackLength"), handler.getDouble("lengthError"), 
                handler.getDouble("UThHeAge"), handler.getDouble("UThHeAgeError"), handler.getString("articleRef"), 
                handler.getString("articleDoi"), 
                handler.getString("orderField"), handler.getString("orderType"), handler.getInteger("pageIndex",1), handler.getInteger("pageSize",30));
        handler.put("page", page).render();
    }

    @Autowired
    private ZirconService service;

}