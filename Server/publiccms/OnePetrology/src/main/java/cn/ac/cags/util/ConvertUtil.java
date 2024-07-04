package cn.ac.cags.util;

import cn.ac.cags.entities.rock.SampleBasicInfo;
import cn.ac.cags.vo.SampleInfoVO;


/**
 * 转换工具类，把VO转为对应的entity类
 */
public class ConvertUtil {

    public static SampleBasicInfo fromSampleInfoVO(SampleInfoVO vo){
        SampleBasicInfo rtn=new SampleBasicInfo();
        //逐个字段赋值
        rtn.setHasChecked(Boolean.FALSE);//默认没有审核

        rtn.setCountryCode("CN");//默认为中国，如果是其它国家需要修改

        rtn.setAge(vo.getAge());
        rtn.setAgeError(vo.getAgeError());
        rtn.setAgeSelected(vo.getAgeSelected());
        rtn.setAgeSelectedError(vo.getAgeSelectedError());
        rtn.setAlkalinity(vo.getAlkalinity());
        rtn.setAluminumQuality(vo.getAluminumQuality());
        rtn.setAnalyzeOrg(vo.getAnalyzeOrg());
        rtn.setAnalyzePerson(vo.getAnalyzePerson());
        rtn.setArticleDoi(vo.getArticleDoi());
        rtn.setArticleId(vo.getArticleId());
        rtn.setCharacteristicMinerals(vo.getCharacteristicMinerals());
        rtn.setCollector(vo.getCollector());
        rtn.setCollectorOrg(vo.getCollectorOrg());
        rtn.setDegreeOfDeformation(vo.getDegreeOfDeformation());
        rtn.setEra(vo.getEra());
        rtn.setForm(vo.getForm());
        rtn.setGeneticType(vo.getGeneticType());
        rtn.setGeobodyCode(vo.getGeobodyCode());
        rtn.setGeobodyName(vo.getGeobodyName());
        rtn.setIsCutAreaConstructionLine(translate(vo.getCutAreaConstructionLine()));
        rtn.setLatitude(vo.getLatitude());
        rtn.setLithology(vo.getLithology());
        rtn.setLocation(vo.getLocation());
        rtn.setLongitude(vo.getLongitude());
        rtn.setOriginalSampleId(vo.getOriginalSampleId());
        rtn.setPhoto(vo.getPhoto());//此处是否需要转化相对路径？？？待定
        rtn.setPrimaryStructuralUnit(vo.getPrimaryStructuralUnit());
        rtn.setRelationshipWithSurroundingRock(vo.getRelationshipWithSurroundingRock());
        rtn.setRemark(vo.getRemark());
        rtn.setReviewer(vo.getReviewer());
        rtn.setRockCode(vo.getRockCode());
        rtn.setRockName(vo.getRockName());
        rtn.setSecondaryStructuralUnit(vo.getSecondaryStructuralUnit());
        rtn.setSourceOfStructuralTypeDiscrimination(vo.getSourceOfStructuralTypeDiscrimination());
        rtn.setSurroundingRockAge(vo.getSurroundingRockAge());
        rtn.setSurroundingRockLithology(vo.getSurroundingRockLithology());
        rtn.setTectonicLocation(vo.getTectonicLocation());
        rtn.setTectonicType(vo.getTectonicType());
        rtn.setTertiarySturcturalUnit(vo.getTertiarySturcturalUnit());
        rtn.setTestDate(vo.getTestDate());
        rtn.setTestMethod(vo.getTestMethod());
        rtn.setTestObject(vo.getTestObject());

        if(rtn.getLatitude()==null){
            rtn.setLatitude(0.0);
        }
        if(rtn.getLongitude()==null){
            rtn.setLongitude(0.0);
        }

        return rtn;
    }

    /**
     * 从字符型描述转换为boolean型
     * @param str
     * @return
     */
    public static Boolean translate(String str){
        if(str==null || str.isEmpty()) return  Boolean.FALSE;

        if(str.equalsIgnoreCase("是")||str.equalsIgnoreCase("Y")){
            return Boolean.TRUE;
        }else{
            return Boolean.FALSE;
        }
    }

    /**
     *样品标识：采集样品的全球统一标识编号，共 11 位。标识编码规则， 1位纬度符号
     （N/S S）+2 位纬度整数值 +1 位经度符号 (W/E)+3 位经度整数值 +5位顺序号，顺序号
     从 00001 开始编号。样本标识根据 经纬度项由程序自动生成。
     * @param longtitude
     * @param latitude
     * @return
     */
    public static String getSampleId(Double longtitude,Double latitude,int count){
        //纬度从-90~90,经度从-180~180
        String strLat,strLon;
        if(latitude<0){
           strLat="S";
        }else{
            strLat="N";
        }
        if(longtitude<0){
            strLon="W";
        }else{
            strLon="E";
        }

        String rtn=String.format("%s%02d%s%03d%05d",strLat,Math.round(latitude),strLon,Math.round(longtitude),count++);
        return rtn;
    }
}
