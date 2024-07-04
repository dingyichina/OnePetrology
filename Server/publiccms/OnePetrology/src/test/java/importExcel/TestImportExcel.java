package importExcel;

import cn.ac.cags.entities.rock.SampleBasicInfo;
import cn.ac.cags.logic.dao.rock.SampleBasicInfoDao;
import cn.ac.cags.logic.mapper.SampleInfoMapper;
import cn.ac.cags.util.ConvertUtil;
import cn.ac.cags.util.ImportExcelUtil;
import cn.ac.cags.vo.SampleInfoVO;
import config.spring.ApplicationConfig;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

import java.io.File;
import java.io.FileInputStream;
import java.util.List;


@RunWith(SpringJUnit4ClassRunner.class)
@ContextConfiguration(classes = ApplicationConfig.class)
public class TestImportExcel {

    @Autowired
    SampleBasicInfoDao dao;
    @Autowired
    SampleInfoMapper sampleInfoMapper;

    @Test
    public void importtest(){
        File file=new File("/test.xlsx");
        if (!ImportExcelUtil.checkFileType(file.getName())) {

            System.out.println("只支持2007版以上的Excel导入");
            return ;
        }
        String sheetId = "样品基本信息";
        try {
            List<SampleInfoVO> result = (List<SampleInfoVO>) ImportExcelUtil.parseExcel(sheetId, new FileInputStream(file));

            //逐个导入
            for(int i=0;i<result.size();i++){
                SampleInfoVO vo=result.get(i);
                SampleBasicInfo sampleBasicInfo= ConvertUtil.fromSampleInfoVO(vo);
                int countExist=sampleInfoMapper.getExistsCount(sampleBasicInfo.getLongitude(),sampleBasicInfo.getLatitude());
                sampleBasicInfo.setSampleId(ConvertUtil.getSampleId(sampleBasicInfo.getLongitude(),sampleBasicInfo.getLatitude(),countExist+1));
                System.out.println("导入:"+sampleBasicInfo.getArticleDoi());

                dao.save(sampleBasicInfo);

            }


        } catch (Exception e) {
            e.printStackTrace();

        }
        finally {

        }

    }

}
