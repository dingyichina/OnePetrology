package cn.ac.cags.views.directive.rock;

// Generated 2020-3-29 22:54:40 by com.publiccms.common.generator.SourceGenerator

import java.io.IOException;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import cn.ac.cags.entities.rock.ArtificialHeavyMineralData;
import cn.ac.cags.logic.service.rock.ArtificialHeavyMineralDataService;
import com.publiccms.common.tools.CommonUtils;
import com.publiccms.common.base.AbstractTemplateDirective;
import com.publiccms.common.handler.RenderHandler;

/**
 *
 * ArtificialHeavyMineralDataDirective
 * 
 */
@Component
public class ArtificialHeavyMineralDataDirective extends AbstractTemplateDirective {

    @Override
    public void execute(RenderHandler handler) throws IOException, Exception {
        Integer id = handler.getInteger("id");
        if (CommonUtils.notEmpty(id)) {
            ArtificialHeavyMineralData entity = service.getEntity(id);
            if (null != entity) {
                handler.put("object", entity).render();
            }
        } else {
            Integer[] ids = handler.getIntegerArray("ids");
            if (CommonUtils.notEmpty(ids)) {
                List<ArtificialHeavyMineralData> entityList = service.getEntitys(ids);
                Map<String, ArtificialHeavyMineralData> map = new LinkedHashMap<>();
                for (ArtificialHeavyMineralData entity : entityList) {
                    map.put(String.valueOf(entity.getId()), entity);
                }
                handler.put("map", map).render();
            }
        }
    }

    @Autowired
    private ArtificialHeavyMineralDataService service;

}