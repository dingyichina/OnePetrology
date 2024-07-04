package cn.ac.cags.views.directive.customize;

import cn.ac.cags.logic.mapper.SampleInfoMapper;
import com.publiccms.common.base.AbstractTemplateDirective;
import com.publiccms.common.handler.RenderHandler;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import java.io.IOException;

@Component
public class SampleListDirective  extends AbstractTemplateDirective {
    @Override
    public void execute(RenderHandler handler) throws IOException, Exception {
        handler.put("count",service.getAllSample().size());
        handler.put("page",service.getAllSample()).render();

    }
    @Autowired
    private SampleInfoMapper service;
}
