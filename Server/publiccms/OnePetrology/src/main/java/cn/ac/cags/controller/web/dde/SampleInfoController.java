package cn.ac.cags.controller.web.dde;

// Generated 2021-7-29 15:30:09 by com.publiccms.common.generator.SourceGenerator

import cn.ac.cags.entities.dde.SampleInfo;
import cn.ac.cags.logic.service.dde.SampleInfoService;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import com.publiccms.common.annotation.Csrf;
import com.publiccms.common.constants.CommonConstants;
import com.publiccms.common.constants.Constants;
import com.publiccms.common.tools.CommonUtils;
import com.publiccms.common.tools.JsonUtils;
import com.publiccms.common.tools.RequestUtils;
import com.publiccms.entities.log.LogOperate;
import com.publiccms.entities.sys.SysSite;
import com.publiccms.entities.sys.SysUser;
import com.publiccms.logic.service.log.LogLoginService;
import com.publiccms.logic.service.log.LogOperateService;
import org.apache.commons.lang3.StringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.view.UrlBasedViewResolver;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;
import java.util.*;

/**
 * SampleInfoAdminController
 */
@Controller
@RestController
@RequestMapping("sampleInfo")
public class SampleInfoController {

    @Autowired
    protected LogOperateService logOperateService;
    private String[] ignoreProperties = new String[]{"id"};
    @Autowired
    private SampleInfoService service;

    /**
     * @param site
     * @param entity
     * @param request
     * @param model
     * @return operate result
     */
    @RequestMapping("save")
    //@Csrf
    @ResponseBody
    public String save(@RequestAttribute SysSite site, SampleInfo entity, String returnUrl, HttpServletRequest request, ModelMap model) {
        if (null != entity.getId()) {
            entity = service.update(entity.getId(), entity, ignoreProperties);
            logOperateService.save(new LogOperate(site.getId(), 1l, LogLoginService.CHANNEL_WEB_MANAGER, "update.sampleInfo",
                    RequestUtils.getIpAddress(request), CommonUtils.getDate(), JsonUtils.getString(entity)));
        } else {
            service.save(entity);
            logOperateService.save(new LogOperate(site.getId(), 1l, LogLoginService.CHANNEL_WEB_MANAGER, "save.sampleInfo",
                    RequestUtils.getIpAddress(request), CommonUtils.getDate(), JsonUtils.getString(entity)));
        }
        return UrlBasedViewResolver.REDIRECT_URL_PREFIX + returnUrl;
    }

    /**
     * @param site
     * @param queryGeojson
     * @param returnUrl
     * @param request
     * @param model
     * @return operate result
     */
    @RequestMapping("queryPolygon")
//    @Csrf
    @ResponseBody
    public String queryPolygon(@RequestAttribute SysSite site,String queryGeojson, String returnUrl,
                               Integer pageIndex, Integer pageSize, String OrderByField, String orderByType, HttpServletRequest request, ModelMap model) {
        logOperateService.save(new LogOperate(site.getId(), 1l, LogLoginService.CHANNEL_WEB_MANAGER, "queryPolygon.sampleInfo",
                RequestUtils.getIpAddress(request), CommonUtils.getDate(), queryGeojson));


        return UrlBasedViewResolver.REDIRECT_URL_PREFIX + returnUrl;
    }



    /**
     * @param site
     * @param polygon
     * @param request
     * @param model
     * @return operate result
     */
    @RequestMapping("getSampleList")
    //@Csrf
    @ResponseBody
    public Map<Object, Object> getSampleList(@RequestAttribute SysSite site, @SessionAttribute SysUser admin, String polygon, HttpServletRequest request, ModelMap model) {
        logOperateService.save(new LogOperate(site.getId(), admin.getId(), LogLoginService.CHANNEL_WEB_MANAGER, "queryPolygon.sampleInfo",
                RequestUtils.getIpAddress(request), CommonUtils.getDate(), polygon));
        String draw = request.getParameter("draw");
        List<SampleInfo> myList = service.queryPolygon(polygon);
        Map<Object, Object> info = new HashMap<Object, Object>();
        info.put("data", myList);
        info.put("total", myList.size());
        info.put("draw", draw);
        return info;
    }


    /**
     * added by sunchao
     * @param geoage
     * @param site
     * @param age
     * @param age_min
     * @param age_max
     * @param request
     * @param model
     * @return operate result
     */
    @RequestMapping("getSampleListByAge")
    //@Csrf
    @ResponseBody
    public Map<Object, Object> getSampleListByAge(@RequestAttribute SysSite site, @SessionAttribute SysUser admin, Double age, Double age_min, Double age_max, Double geoage, HttpServletRequest request, ModelMap model) {
        if (age == null) age = Double.valueOf(0);
        logOperateService.save(new LogOperate(site.getId(), 0L, LogLoginService.CHANNEL_WEB_MANAGER, "queryByAge.sampleInfo",
                RequestUtils.getIpAddress(request), CommonUtils.getDate(), age.toString()));
        Map<Object, Object> info = new HashMap<Object, Object>();
        String draw = request.getParameter("draw");
        if( null==age)
            age= Double.valueOf(-1);
        if( null==age_min)
            age_min= Double.valueOf(-1);
        if(null==age_max)
            age_max= Double.valueOf(-1);
             if(null==geoage)
               geoage= Double.valueOf(-1);
             System.out.println(geoage);
        //System.out.println(geoage);
        System.out.println("age="+age+":"+"geoage="+geoage);
        if (age > 0&&geoage<1) {
            List<SampleInfo> myList = service.queryByAge(age);
            info.put("data", myList);
            info.put("total", myList.size());

        } else if (age_min >0|| age_max >0) {
            List<SampleInfo> myList = service.queryByAgeInterval(age, age_min, age_max);
            info.put("data", myList);
            info.put("total", myList.size());
        } else if (geoage >= 1) {

            List<SampleInfo> myList = service.queryByGeoAge(geoage);
            info.put("data", myList);
            info.put("total", myList.size());
        }
        info.put("draw", draw);
        return info;
    }

    /**
     * @param site
     * @param request
     * @param model
     * @return operate result
     */
    @RequestMapping("getSampleList4GeoCloud")
    //@Csrf
    @ResponseBody
    public Map<Object, Object> getSampleList4GeoCloud(@RequestAttribute SysSite site, HttpServletRequest request, ModelMap model) {
        logOperateService.save(new LogOperate(site.getId(), 0L, LogLoginService.CHANNEL_WEB_MANAGER, "地质云查询",
                RequestUtils.getIpAddress(request), CommonUtils.getDate(), "地质云检索"));
        String draw = request.getParameter("draw");
        List<SampleInfo> myList = service.query4GeoCloud();
        Map<Object, Object> info = new HashMap<Object, Object>();
        info.put("data", myList);
        info.put("total", myList.size());
        info.put("draw", draw);
        return info;
    }

    /**
     * added by sunchao
     * @param site
     * @param request
     * @param model
     * @return operate result
     */
    @RequestMapping("getAgedSampleListAll")
    //@Csrf
    @ResponseBody
    public Map<Object, Object> getAgedSampleListAll(@RequestAttribute SysSite site, HttpServletRequest request, ModelMap model) {
        logOperateService.save(new LogOperate(site.getId(), 0L, LogLoginService.CHANNEL_WEB_MANAGER, "年龄查询",
                RequestUtils.getIpAddress(request), CommonUtils.getDate(), "年龄"));
        String draw = request.getParameter("draw");
        List<SampleInfo> myList = service.queryAgedSampleListAll();
        Map<Object, Object> info = new HashMap<Object, Object>();
        info.put("data", myList);
        info.put("total", myList.size());
        info.put("draw", draw);
        return info;
    }

    /**
     * @param ids
     * @param request
     * @param site
     * @param admin
     * @param _csrf
     * @param model
     * @return operate result
     */
    @RequestMapping("delete")
    @Csrf
    public String delete(@RequestAttribute SysSite site, @SessionAttribute SysUser admin, Integer[] ids, String _csrf, HttpServletRequest request,
                         ModelMap model) {
        if (CommonUtils.notEmpty(ids)) {
            service.delete(ids);
            logOperateService.save(new LogOperate(site.getId(), admin.getId(), LogLoginService.CHANNEL_WEB_MANAGER, "delete.sampleInfo",
                    RequestUtils.getIpAddress(request), CommonUtils.getDate(), StringUtils.join(ids, ',')));
        }
        return CommonConstants.TEMPLATE_DONE;
    }

    /**
     * query Major Element added by sunchao
     *
     * @param site
     * @param request
     * @param chemswitch
     * @param SIO2_lt
     * @param SIO2_gt
     * @param TIO2_lt
     * @param TIO2_gt
     * @param AL2O3_lt
     * @param AL2O3_gt
     * @param FE2O3_lt
     * @param FE2O3_gt
     * @param FE2O3T_lt
     * @param FE2O3T_gt
     * @param FEO_lt
     * @param FEO_gt
     * @param FEOT_lt
     * @param FEOT_gt
     * @param MGO_lt
     * @param MGO_gt
     * @param CAO_lt
     * @param CAO_gt
     * @param NA2O_lt
     * @param NA2O_gt
     * @param K2O_lt
     * @param K2O_gt
     * @param P2O5_lt
     * @param P2O5_gt
     * @param MNO_lt
     * @param MNO_gt
     * @param CR2O3_lt
     * @param CR2O3_gt
     * @param NIO_lt
     * @param NIO_gt
     * @param CACO3_lt
     * @param CACO3_gt
     * @param pkey
     * @param glossary_pkey
     * @param model
     * @return operate result
     */
    @RequestMapping("getSampleListByMajorElement")
    //@Csrf
    @ResponseBody
    public Map<Object, Object> getSampleListByMajorElement(@RequestAttribute SysSite site, @SessionAttribute SysUser admin, String chemswitch,
                                                         String SIO2_lt,
                                                         String SIO2_gt,
                                                         String TIO2_lt,
                                                         String TIO2_gt, String AL2O3_lt,
                                                         String AL2O3_gt, String FE2O3_lt,
                                                         String FE2O3_gt, String FE2O3T_lt, String FE2O3T_gt,
                                                         String FEO_lt, String FEO_gt,
                                                         String FEOT_lt, String FEOT_gt,
                                                         String MGO_lt, String MGO_gt, String CAO_lt, String CAO_gt,
                                                         String NA2O_lt, String NA2O_gt, String K2O_lt,
                                                         String K2O_gt, String P2O5_lt, String P2O5_gt,
                                                         String MNO_lt, String MNO_gt, String CR2O3_lt, String CR2O3_gt,
                                                         String NIO_lt, String NIO_gt, String CACO3_lt, String CACO3_gt, String pkey, String glossary_pkey,
                                                         HttpServletRequest request, ModelMap model,HttpSession session) {
        logOperateService.save(new LogOperate(site.getId(), 0L, LogLoginService.CHANNEL_WEB_MANAGER, "queryPolygon.sampleInfo",
                RequestUtils.getIpAddress(request), CommonUtils.getDate(), "化学元素查询"));
        String draw = request.getParameter("draw");
        chemswitch =request.getParameter("chemswitch");
        String sqlString="";
           if(!"".equalsIgnoreCase(SIO2_lt)&&!"".equalsIgnoreCase(SIO2_gt))
                sqlString+="(sio2>"+SIO2_lt+" and sio2<"+SIO2_gt+") "+chemswitch+" ";
           if(!"".equalsIgnoreCase(TIO2_lt)&&!"".equalsIgnoreCase(TIO2_gt))
               sqlString+="(tio2>"+TIO2_lt+" and tio2<"+TIO2_gt+") "+chemswitch+" ";
           if(!"".equalsIgnoreCase(AL2O3_lt)&&!"".equalsIgnoreCase(AL2O3_gt))
              sqlString+="(al2o3>"+AL2O3_lt+" and al2o3<"+AL2O3_gt+") "+chemswitch+" ";
           if(!"".equalsIgnoreCase(FE2O3_lt)&&!"".equalsIgnoreCase(FE2O3_gt))
               sqlString+="(fe2o3>"+FE2O3_lt+" and fe2o3<"+FE2O3_gt+") "+chemswitch+" ";
           if(!"".equalsIgnoreCase(FE2O3T_lt)&&!"".equalsIgnoreCase(FE2O3T_gt))
          sqlString+="(fe2o3t>"+FE2O3T_lt+" and fe2o3t<"+FE2O3T_gt+") "+chemswitch+" ";
          if(!"".equalsIgnoreCase(FEO_lt)&&!"".equalsIgnoreCase(FEO_gt))
            sqlString+="(feo>"+FEO_lt+" and feo<"+FEO_gt+") "+chemswitch+" ";
          if(!"".equalsIgnoreCase(FEOT_lt)&&!"".equalsIgnoreCase(FEOT_gt))
            sqlString+="(feot>"+FEOT_lt+" and feot<"+FEOT_gt+") "+chemswitch+" ";
        if(!"".equalsIgnoreCase(MGO_lt)&&!"".equalsIgnoreCase(MGO_gt))
            sqlString+="(mgo>"+MGO_lt+" and mgo<"+MGO_gt+") "+chemswitch+" ";
        if(!"".equalsIgnoreCase(CAO_lt)&&!"".equalsIgnoreCase(CAO_gt))
            sqlString+="(cao>"+CAO_lt+" and cao<"+CAO_gt+") "+chemswitch+" ";
        if(!"".equalsIgnoreCase(NA2O_lt)&&!"".equalsIgnoreCase(NA2O_gt))
            sqlString+="(na2o>"+NA2O_lt+" and na2o<"+NA2O_gt+") "+chemswitch+" ";
        if(!"".equalsIgnoreCase(K2O_lt)&&!"".equalsIgnoreCase(K2O_gt))
            sqlString+="(k2o>"+K2O_lt+" and k2o<"+K2O_gt+") "+chemswitch+" ";
        if(!"".equalsIgnoreCase(P2O5_lt)&&!"".equalsIgnoreCase(P2O5_gt))
            sqlString+="(p2o5>"+P2O5_lt+" and p2o5<"+P2O5_gt+") "+chemswitch+" ";
        if(!"".equalsIgnoreCase(MNO_lt)&&!"".equalsIgnoreCase(MNO_gt))
            sqlString+="(mno>"+MNO_lt+" and mno<"+MNO_gt+") "+chemswitch+" ";
//        if(!"".equalsIgnoreCase(CR2O3_lt)&&!"".equalsIgnoreCase(CR2O3_gt))
//            sqlString="(cr2o3>"+CR2O3_lt+" and cr2o3<t"+CR2O3_lt+") "+chemswitch+" ";

        Map<String, String[]> paraMap =  request.getParameterMap();
        Set<String> keyset = paraMap.keySet();

        Iterator it = keyset.iterator();

        String paramkey,chemValue,chemString_lt, chemString_gt= "";

        int i=0;

        while (it.hasNext()) {

             paramkey = it.next().toString();
             chemValue = paraMap.get(paramkey)[0];
             i++;
            System.out.println(i+"key:"+paramkey+", value="+chemValue+" ");
//
//            if (paramkey.indexOf("_lt") >= 0) {
//
//                if ("" == chemValue || null == chemValue)
//                    chemValue = "0";
//                chemString_lt = paramkey.replace("_lt", ">") + paraMap.get(paramkey)[0];
//                sqlString +="("+ chemString_lt+" ";
//            }
//            if (paramkey.indexOf("_gt") >= 0) {
//                if ("" .equalsIgnoreCase(chemValue) || null == chemValue)
//                    chemValue = "100";
//                chemString_gt = paramkey.replace("_gt", "<") + paraMap.get(paramkey)[0];
//                sqlString = " and " + chemString_gt+ "）  ";
//            }
//
//            sqlString+=sqlString+chemswitch+ " ";
        }



//        Enumeration<String> parameterNames = request.getParameterNames();
//        while (parameterNames.hasMoreElements()) {
//            String paramName = (String) parameterNames.nextElement();
//            String[] values = request.getParameterValues(paramName);
//            for (int i = 0; i < values.length; i++) {
//                System.out.println("[" + i + "]   " + paramName + "  " + values[i]);
//            }
//        }
        if("or".equalsIgnoreCase(chemswitch))
            sqlString="select * from sample_info where 1=1 and "+sqlString+" 1>1";
        else
            sqlString="select * from sample_info where 1=1 and "+sqlString+" 1=1";
        System.out.println(sqlString);

        List<SampleInfo> myList = service.queryByChem(sqlString);
        Map<Object, Object> info = new HashMap<Object, Object>();
        info.put("data", myList);
        info.put("total", myList.size());
        info.put("draw", draw);
        return info;
    }

    /**
     * @param site
     * @param chemswitch
     * @param chemjson
     * @param request
     * @param model
     * @return operate result
     */
    @RequestMapping("getSampleListByChem")
    //@Csrf
    @ResponseBody
    public Map<Object, Object> getSampleListByChem(@RequestAttribute SysSite site, @SessionAttribute SysUser admin, String chemswitch,String chemjson,
                            HttpServletRequest request, ModelMap model) throws JsonProcessingException {
        logOperateService.save(new LogOperate(site.getId(), admin.getId(), LogLoginService.CHANNEL_WEB_MANAGER, "getSampleListByChem.sampleInfo",
                RequestUtils.getIpAddress(request), CommonUtils.getDate(), chemswitch));

        String draw = request.getParameter("draw");
        JsonNode eleArrayNode = Constants.objectMapper.readTree(chemjson);


       String sqlString = "";
        for (JsonNode eleNode : eleArrayNode) {
            int i=0;
            String expstr1 = "", expstr2 = "";
            for (JsonNode singleNode : eleNode) {
                String[] strArray=singleNode.textValue().split(":");

                if(strArray.length>1) {
                    if (strArray[0].indexOf("lt") >= 0)
                        expstr1 = strArray[0].replace("_lt", ">")+strArray[1];
                    else if (strArray[0].indexOf("gt") >= 0)
                        expstr2 = strArray[0].replace("_gt", "<")+strArray[1];
                }
                i++;
            }
            if(!"".equalsIgnoreCase(expstr1)&&!"".equalsIgnoreCase(expstr2))
                sqlString += "(" + expstr1 + " and " + expstr2 + ") " + chemswitch + " ";

        }
        if("or".equalsIgnoreCase(chemswitch))
            sqlString="select * from sample_info where 1=1 and "+sqlString+" 1>1";
        else
            sqlString="select * from sample_info where 1=1 and "+sqlString+" 1=1";
        System.out.println(sqlString);
        List<SampleInfo> myList = service.queryByChem(sqlString);
        Map<Object, Object> info = new HashMap<Object, Object>();


        info.put("data", myList);
        info.put("total", myList.size());
        info.put("draw", draw);
        return info;
    }


//    @Autowired
//    private SampleInfoRepository sampleInfoRepository;

//    @PersistenceContext
//    private EntityManager em;
//    /**
//     * 服务端模式
//     * @param input
//     * @return
//     * @draw
//     * @param request
//     */
//    @RequestMapping(value = "dtlist", method = RequestMethod.POST)
//    @ResponseBody
//    public DataTablesOutput<SampleInfo> list(@Valid DataTablesInput input,HttpServletRequest request) {
////        String draw = request.getParameter("draw");
////        List<SampleInfo> list=service.queryAgedSampleListAll();
////       DataTablesOutput<SampleInfo> samples=new DataTablesOutput<SampleInfo>();
////            samples.setData(list);
////        System.out.println(list.size());
////        samples.setDraw(Integer.valueOf(draw));
////        samples.setRecordsTotal(list.size());
////        return samples;
////        private sampleInfoRepository=new SampleInfoRepositoryImpl() ;
//
//
//        return sampleInfoRepository.findAll(input);
//
//    }



    /**
     * Trace elemet
     *@param LI_check
     * @param LI_lt
     * @param LI_gt
     * @param BE_check
     * @param BE_lt
     * @param BE_gt
     * @param B_check
     * @param B_lt
     * @param B_gt
     * @param C_check
     * @param C_lt
     * @param C_gt
     * @param K_check
     * @param K_lt
     * @param K_gt
     * @param CA_check
     * @param CA_lt
     * @param CA_gt
     * @param MG_check
     * @param MG_lt
     * @param MG_gt
     * @param SC_check
     * @param SC_lt
     * @param SC_gt
     * @param TI_check
     * @param TI_lt
     * @param TI_gt
     * @param V_check
     * @param V_lt
     * @param V_gt
     * @param FE_check
     * @param FE_lt
     * @param FE_gt
     * @param CR_check
     * @param CR_lt
     * @param CR_gt
     * @param MN_check
     * @param MN_lt
     * @param MN_gt
     * @param CO_check
     * @param CO_lt
     * @param CO_gt
     * @param NI_check
     * @param NI_lt
     * @param NI_gt
     * @param ZN_check
     * @param ZN_lt
     * @param ZN_gt
     * @param CU_check
     * @param CU_lt
     * @param CU_gt
     * @param ZR_check
     * @param ZR_lt
     * @param ZR_gt
     * @param GA_check
     * @param GA_lt
     * @param GA_gt
     * @param GER_check
     * @param GER_lt
     * @param GER_gt
     * @param P_check
     * @param P_lt
     * @param P_gt
     * @param SN_check
     * @param SN_lt
     * @param SN_gt
     * @param CD_check
     * @param CD_lt
     * @param CD_gt
     * @param HF_check
     * @param HF_lt
     * @param HF_gt
     * @param IR_check
     * @param IR_lt
     * @param IR_gt
     * @param PT_check
     * @param PT_lt
     * @param PT_gt
     * @param TL_check
     * @param TL_lt
     * @param TL_gt
     * @param SE_check
     * @param SE_lt
     * @param SE_gt
     * @param ARSENIC_check
     * @param ARSENIC_lt
     * @param ARSENIC_gt
     * @param PD_check
     * @param PD_lt
     * @param PD_gt
     * @param SR_check
     * @param SR_lt
     * @param SR_gt
     * @param AG_check
     * @param AG_lt
     * @param AG_gt
     * @param Y_check
     * @param Y_lt
     * @param Y_gt
     * @param RE_check
     * @param RE_lt
     * @param RE_gt
     * @param BA_check
     * @param BA_lt
     * @param BA_gt
     * @param PB_check
     * @param PB_lt
     * @param PB_gt
     * @param BI_check
     * @param BI_lt
     * @param BI_gt
     * @param I_check
     * @param I_lt
     * @param I_gt
     * @param AL_check
     * @param AL_lt
     * @param AL_gt
     * @param HG_check
     * @param HG_lt
     * @param HG_gt
     * @param NB_check
     * @param NB_lt
     * @param NB_gt
     * @param TE_check
     * @param TE_lt
     * @param TE_gt
     * @param W_check
     * @param W_lt
     * @param W_gt
     * @param SB_check
     * @param SB_lt
     * @param SB_gt
     * @param TH_check
     * @param TH_lt
     * @param TH_gt
     * @param OS_check
     * @param OS_lt
     * @param OS_gt
     * @param RB_check
     * @param RB_lt
     * @param RB_gt
     * @param S_check
     * @param S_lt
     * @param S_gt
     * @param AU_check
     * @param AU_lt
     * @param AU_gt
     * @param CS_check
     * @param CS_lt
     * @param CS_gt
     * @param MO_check
     * @param MO_lt
     * @param MO_gt
     * @param U_check
     * @param U_lt
     * @param U_gt
     * @param TA_check
     * @param TA_lt
     * @param TA_gt
     */



    /**
     *VOLATILE
     *  * @param LOI_check
     * @param LOI_lt
     * @param LOI_gt
     * @param H2O_P_check
     * @param H2O_P_lt
     * @param H2O_P_gt
     * @param H2O_M_check
     * @param H2O_M_lt
     * @param H2O_M_gt
     * @param H2O_check
     * @param H2O_lt
     * @param H2O_gt
     * @param H2O_T_check
     * @param H2O_T_lt
     * @param H2O_T_gt
     * @param CO2_check
     * @param CO2_lt
     * @param CO2_gt
     * @param F_check
     * @param F_lt
     * @param F_gt
     * @param CL_check
     * @param CL_lt
     * @param CL_gt
     *
     */


    /**
     *RARE EARTH ELEMENTS
     * @param LA_check
     * @param LA_lt
     * @param LA_gt
     * @param CE_check
     * @param CE_lt
     * @param CE_gt
     * @param PR_check
     * @param PR_lt
     * @param PR_gt
     * @param ND_check
     * @param ND_lt
     * @param ND_gt
     * @param SM_check
     * @param SM_lt
     * @param SM_gt
     * @param EU_check
     * @param EU_lt
     * @param EU_gt
     * @param GD_check
     * @param GD_lt
     * @param GD_gt
     * @param TB_check
     * @param TB_lt
     * @param TB_gt
     * @param DY_check
     * @param DY_lt
     * @param DY_gt
     * @param HO_check
     * @param HO_lt
     * @param HO_gt
     * @param ER_check
     * @param ER_lt
     * @param ER_gt
     * @param TM_check
     * @param TM_lt
     * @param TM_gt
     * @param YB_check
     * @param YB_lt
     * @param YB_gt
     * @param LU_check
     * @param LU_lt
     * @param LU_gt
     */

    /**
     *STABLE ISOTOPES
     * @param DELTA_O18_check
     * @param DELTA_O18_lt
     * @param DELTA_O18_gt
     * @param DELTA_C13_check
     * @param DELTA_C13_lt
     * @param DELTA_C13_gt
     * @param delta_fe57_check
     * @param delta_fe57_lt
     * @param delta_fe57_gt
     * @param delta_b11_check
     * @param delta_b11_lt
     * @param delta_b11_gt
     * @param delta_cl37_check
     * @param delta_cl37_lt
     * @param delta_cl37_gt
     * @param delta_cu65_check
     * @param delta_cu65_lt
     * @param delta_cu65_gt
     * @param delta_d_check
     * @param delta_d_lt
     * @param delta_d_gt
     * @param delta_fe56_check
     * @param delta_fe56_lt
     * @param delta_fe56_gt
     * @param delta_li6_check
     * @param delta_li6_lt
     * @param delta_li6_gt
     * @param delta_li7_check
     * @param delta_li7_lt
     * @param delta_li7_gt
     * @param delta_mg25_check
     * @param delta_mg25_lt
     * @param delta_mg25_gt
     * @param delta_mg26_check
     * @param delta_mg26_lt
     * @param delta_mg26_gt
     * @param delta_mo98_check
     * @param delta_mo98_lt
     * @param delta_mo98_gt
     * @param delta_n15_check
     * @param delta_n15_lt
     * @param delta_n15_gt
     * @param delta_ni60_check
     * @param delta_ni60_lt
     * @param delta_ni60_gt
     * @param delta_s33_check
     * @param delta_s33_lt
     * @param delta_s33_gt
     * @param delta_s34_check
     * @param delta_s34_lt
     * @param delta_s34_gt
     * @param cap_delta_s33_check
     * @param cap_delta_s33_lt
     * @param cap_delta_s33_gt
     * @param cap_delta_s36_check
     * @param cap_delta_s36_lt
     * @param cap_delta_s36_gt
     * @param delta_s36_check
     * @param delta_s36_lt
     * @param delta_s36_gt
     * @param delta_si29_check
     * @param delta_si29_lt
     * @param delta_si29_gt
     * @param delta_si30_check
     * @param delta_si30_lt
     * @param delta_si30_gt
     * @param delta_zn66_check
     * @param delta_zn66_lt
     * @param delta_zn66_gt
     * @param delta_zn68_check
     * @param delta_zn68_lt
     * @param delta_zn68_gt
     * @param ar40_ar36_ini_check
     * @param ar40_ar36_ini_lt
     * @param ar40_ar36_ini_gt
     * @param ar40_atm_check
     * @param ar40_atm_lt
     * @param ar40_atm_gt
     * @param b11_b10_check
     * @param b11_b10_lt
     * @param b11_b10_gt
     * @param os188_check
     * @param os188_lt
     * @param os188_gt
     * @param tl203_tl205_check
     * @param tl203_tl205_lt
     * @param tl203_tl205_gt
     */

    /**
     *  * @param AR37_AR39_check
     * @param AR37_AR39_lt
     * @param AR37_AR39_gt
     * @param BE10_BE_check
     * @param BE10_BE_lt
     * @param BE10_BE_gt
     * @param AR40_AR36_check
     * @param AR40_AR36_lt
     * @param AR40_AR36_gt
     * @param BE10_BE9_check
     * @param BE10_BE9_lt
     * @param BE10_BE9_gt
     * @param AR36_AR39_check
     * @param AR36_AR39_lt
     * @param AR36_AR39_gt
     * @param PB207_PB204_check
     * @param PB207_PB204_lt
     * @param PB207_PB204_gt
     * @param XE126_XE130_check
     * @param XE126_XE130_lt
     * @param XE126_XE130_gt
     * @param PB206_PB207_check
     * @param PB206_PB207_lt
     * @param PB206_PB207_gt
     * @param XE131_XE132_check
     * @param XE131_XE132_lt
     * @param XE131_XE132_gt
     * @param XE129_XE132_check
     * @param XE129_XE132_lt
     * @param XE129_XE132_gt
     * @param KR80_KR84_check
     * @param KR80_KR84_lt
     * @param KR80_KR84_gt
     * @param XE126_XE132_check
     * @param XE126_XE132_lt
     * @param XE126_XE132_gt
     * @param K40_AR36_check
     * @param K40_AR36_lt
     * @param K40_AR36_gt
     * @param ND143_ND144_check
     * @param ND143_ND144_lt
     * @param ND143_ND144_gt
     * @param LU176_HF177_check
     * @param LU176_HF177_lt
     * @param LU176_HF177_gt
     * @param XE124_XE132_check
     * @param XE124_XE132_lt
     * @param XE124_XE132_gt
     * @param XE136_XE132_check
     * @param XE136_XE132_lt
     * @param XE136_XE132_gt
     * @param AR37_AR40_check
     * @param AR37_AR40_lt
     * @param AR37_AR40_gt
     * @param HE4_NE20_check
     * @param HE4_NE20_lt
     * @param HE4_NE20_gt
     * @param XE129_XE130_check
     * @param XE129_XE130_lt
     * @param XE129_XE130_gt
     * @param SM147_ND144_check
     * @param SM147_ND144_lt
     * @param SM147_ND144_gt
     * @param XE132_XE130_check
     * @param XE132_XE130_lt
     * @param XE132_XE130_gt
     * @param RE187_OS188_check
     * @param RE187_OS188_lt
     * @param RE187_OS188_gt
     * @param XE128_XE130_check
     * @param XE128_XE130_lt
     * @param XE128_XE130_gt
     * @param NE20_NE22_check
     * @param NE20_NE22_lt
     * @param NE20_NE22_gt
     * @param XE130_XE132_check
     * @param XE130_XE132_lt
     * @param XE130_XE132_gt
     * @param HF176_HF177_check
     * @param HF176_HF177_lt
     * @param HF176_HF177_gt
     * @param XE131_XE130_check
     * @param XE131_XE130_lt
     * @param XE131_XE130_gt
     * @param KR86_KR84_check
     * @param KR86_KR84_lt
     * @param KR86_KR84_gt
     * @param NE21_NE22_check
     * @param NE21_NE22_lt
     * @param NE21_NE22_gt
     * @param KR78_KR84_check
     * @param KR78_KR84_lt
     * @param KR78_KR84_gt
     * @param NE21_NE20_check
     * @param NE21_NE20_lt
     * @param NE21_NE20_gt
     * @param HE3_HE4_check
     * @param HE3_HE4_lt
     * @param HE3_HE4_gt
     * @param OS187_OS188_check
     * @param OS187_OS188_lt
     * @param OS187_OS188_gt
     * @param PB206_PB204_check
     * @param PB206_PB204_lt
     * @param PB206_PB204_gt
     * @param SR87_SR86_check
     * @param SR87_SR86_lt
     * @param SR87_SR86_gt
     * @param KR82_KR84_check
     * @param KR82_KR84_lt
     * @param KR82_KR84_gt
     * @param XE134_XE130_check
     * @param XE134_XE130_lt
     * @param XE134_XE130_gt
     * @param XE134_XE132_check
     * @param XE134_XE132_lt
     * @param XE134_XE132_gt
     * @param NE22_NE20_check
     * @param NE22_NE20_lt
     * @param NE22_NE20_gt
     * @param OS187_OS186_check
     * @param OS187_OS186_lt
     * @param OS187_OS186_gt
     * @param PB206_PB208_check
     * @param PB206_PB208_lt
     * @param PB206_PB208_gt
     * @param HE4_HE3_check
     * @param HE4_HE3_lt
     * @param HE4_HE3_gt
     * @param CL36_CL_check
     * @param CL36_CL_lt
     * @param CL36_CL_gt
     * @param PB208_PB204_check
     * @param PB208_PB204_lt
     * @param PB208_PB204_gt
     * @param XE124_XE130_check
     * @param XE124_XE130_lt
     * @param XE124_XE130_gt
     * @param KR83_KR84_check
     * @param KR83_KR84_lt
     * @param KR83_KR84_gt
     * @param RB87_SR86_check
     * @param RB87_SR86_lt
     * @param RB87_SR86_gt
     * @param OS186_OS188_check
     * @param OS186_OS188_lt
     * @param OS186_OS188_gt
     * @param XE136_XE130_check
     * @param XE136_XE130_lt
     * @param XE136_XE130_gt
     * @param OS184_OS188_check
     * @param OS184_OS188_lt
     * @param OS184_OS188_gt
     * @param XE128_XE132_check
     * @param XE128_XE132_lt
     * @param XE128_XE132_gt
     * @param E_ND_check
     * @param E_ND_lt
     * @param E_ND_gt
     * @param RE187_OS186_check
     * @param RE187_OS186_lt
     * @param RE187_OS186_gt
     * @param AR40_K40_check
     * @param AR40_K40_lt
     * @param AR40_K40_gt
     * @param AR40_AR39_check
     * @param AR40_AR39_lt
     * @param AR40_AR39_gt
     * @param AR38_AR36_check
     * @param AR38_AR36_lt
     * @param AR38_AR36_gt
     * /

    /**
     *DISEQUILIBRIUM SERIES ISOTOPES
     * @param U238_check
     * @param U238_lt
     * @param U238_gt
     * @param U238_ACTIVITY_check
     * @param U238_ACTIVITY_lt
     * @param U238_ACTIVITY_gt
     * @param U234_ACTIVITY_check
     * @param U234_ACTIVITY_lt
     * @param U234_ACTIVITY_gt
     * @param TH230_check
     * @param TH230_lt
     * @param TH230_gt
     * @param TH230_ACTIVITY_check
     * @param TH230_ACTIVITY_lt
     * @param TH230_ACTIVITY_gt
     * @param RA226_check
     * @param RA226_lt
     * @param RA226_gt
     * @param RA226_ACTIVITY_check
     * @param RA226_ACTIVITY_lt
     * @param RA226_ACTIVITY_gt
     * @param PO210_ACTIVITY_check
     * @param PO210_ACTIVITY_lt
     * @param PO210_ACTIVITY_gt
     * @param PB210_ACTIVITY_check
     * @param PB210_ACTIVITY_lt
     * @param PB210_ACTIVITY_gt
     * @param PA231_check
     * @param PA231_lt
     * @param PA231_gt
     * @param PA231_ACTIVITY_check
     * @param PA231_ACTIVITY_lt
     * @param PA231_ACTIVITY_gt
     * @param TH232_check
     * @param TH232_lt
     * @param TH232_gt
     * @param TH232_ACTIVITY_check
     * @param TH232_ACTIVITY_lt
     * @param TH232_ACTIVITY_gt
     * @param U234_U238_check
     * @param U234_U238_lt
     * @param U234_U238_gt
     * @param U234_U238_ACTIVITY_check
     * @param U234_U238_ACTIVITY_lt
     * @param U234_U238_ACTIVITY_gt
     * @param TH230_U238_ACTIVITY_check
     * @param TH230_U238_ACTIVITY_lt
     * @param TH230_U238_ACTIVITY_gt
     * @param TH230_TH232_check
     * @param TH230_TH232_lt
     * @param TH230_TH232_gt
     * @param TH230_TH232_ACTIVITY_check
     * @param TH230_TH232_ACTIVITY_lt
     * @param TH230_TH232_ACTIVITY_gt
     * @param TH232_TH230_check
     * @param TH232_TH230_lt
     * @param TH232_TH230_gt
     * @param TH232_TH230_ACTIVITY_check
     * @param TH232_TH230_ACTIVITY_lt
     * @param TH232_TH230_ACTIVITY_gt
     * @param U238_TH232_ACTIVITY_check
     * @param U238_TH232_ACTIVITY_lt
     * @param U238_TH232_ACTIVITY_gt
     * @param RA226_TH230_ACTIVITY_check
     * @param RA226_TH230_ACTIVITY_lt
     * @param RA226_TH230_ACTIVITY_gt
     * @param RA226_TH230_ACTIVITY_INITIAL_check
     * @param RA226_TH230_ACTIVITY_INITIAL_lt
     * @param RA226_TH230_ACTIVITY_INITIAL_gt
     * @param PB210_RA226_ACTIVITY_check
     * @param PB210_RA226_ACTIVITY_lt
     * @param PB210_RA226_ACTIVITY_gt
     * @param PO210_PB210_ACTIVITY_check
     * @param PO210_PB210_ACTIVITY_lt
     * @param PO210_PB210_ACTIVITY_gt
     * @param PA231_U235_ACTIVITY_check
     * @param PA231_U235_ACTIVITY_lt
     * @param PA231_U235_ACTIVITY_gt
     * @param RA228_RA226_ACTIVITY_check
     * @param RA228_RA226_ACTIVITY_lt
     * @param RA228_RA226_ACTIVITY_gt
     * @param RA228_TH232_ACTIVITY_check
     * @param RA228_TH232_ACTIVITY_lt
     * @param RA228_TH232_ACTIVITY_gt
     * @param TH228_TH232_ACTIVITY_check
     * @param TH228_TH232_ACTIVITY_lt
     * @param TH228_TH232_ACTIVITY_gt
     * @param TH232_U238_check
     * @param TH232_U238_lt
     * @param TH232_U238_gt
     * @param U235_PB204_check
     * @param U235_PB204_lt
     * @param U235_PB204_gt
     * @param TH232_PB204_check
     * @param TH232_PB204_lt
     * @param TH232_PB204_gt
     */




}