package cn.ac.cags.logic.mapper;

import cn.ac.cags.entities.dde.SampleInfo;
import org.apache.ibatis.annotations.*;

import java.util.List;

@Mapper
public interface SampleInfoMapper {

    @Select("SELECT count(*)\n" +
            "  FROM sample_info\n" +
            "  where round(longitude)=round(#{longitude}) and round(latitude)=round(#{latitude})")
    public int getExistsCount(@Param("longitude")Double longitude, @Param("latitude")Double latitude);



    @Results({
            @Result(property = "longitude", column = "longitude", javaType = Double.class),
            @Result(property = "latitude", column = "latitude", javaType = Double.class),
            @Result(property = "oraginalSampleId", column = "oraginal_sample_id", javaType = String.class),
    })
    @Select("select longitude,latitude,concat_ws(':',id ,oraginal_sample_id) as oraginal_sample_id" +
            " from sample_info" +
            " where longitude<>0 and latitude<>0 ")
    List<SampleInfo>  getAllSample();


    /**
     * 多边形查询,带分页和按照字段排序
     * @param limit   每页数据条数
     * @param offset  从多少开始
     * @param polygon  空间polygon的坐标点集合   (lng,lat),(lng,lat),(lng,lat)
     * @param orderByField   排序字段
     * @param orderByType   排序类型  默认asc
     * @return
     */
    @Select("select * from sample_info where point(longitude, latitude) <@ polygon(path('(#{polygon})'))  order by #{orderByField}  #{orderByType}  limit #{limit} OFFSET #{offset}  ")
    List<SampleInfo>  queryPolygon(@Param("limit")Integer limit, @Param("offset")Integer offset,@Param("polygon")String polygon ,@Param("orderByField")String orderByField
    ,@Param("orderByType") String orderByType);




    /**
     * 多边形查询,带分页和按照字段排序
     * @param polygon  空间polygon的坐标点集合   (lng,lat),(lng,lat),(lng,lat)
     * @return
     */
    @Select("select * from sample_info where oraginal_sample_id  is not null and point(longitude, latitude) <@ polygon(path('(${polygon})'))  ")
    List<SampleInfo>  queryPolygon4all(@Param("polygon")String polygon );



    /**
     * 多边形查询,带分页和按照字段排序

     * @return
     */
    @Select("select * from sample_info  order by id \n" +
            "limit 16800 ")
    List<SampleInfo>  query4GeoCloud();


    /**
     * added by sunchao
     * @param age
     * @param ageMin
     * @param ageMax
     * @return
     */
    @Select("select * from sample_info where age=#{age} or (age>=#{age_min} and age<=#{age_max})")
    List<SampleInfo> queryByAgeInterval(@Param("age")Double age, @Param("age_min")Double ageMin,  @Param("age_max")Double ageMax);

    /**
     * added by sunchao
     * @param age
     * @return
     */
    @Select("select * from sample_info where age=#{age}")
    List<SampleInfo> queryByAge(@Param("age")Double age);


    /**
     * added by sunchao
     */

    @Select("select * from sample_info where age=#{age}")
    List<SampleInfo> queryByGeoAge(@Param("geoage")Double geoage);

    /**
     * added by sunchao
     * @return
     */
    @Select("select * from sample_info where age>0 order by id" )
    List<SampleInfo> queryAgedSampleListAll();




    /**
     * added by sunchao
     *
     * @param sql sql 语句
     * @return R 返回值
     */
    @SelectProvider(value = SampleSelectProvider.class, method = "getSql")
         <R> R select(String sql);

    /**
     * added by sunchao
     * @param sqlStr
     * @return
     */
    @Select("${sqlStr}")

    List<SampleInfo>  queryByMajorElement(@Param(value = "sqlStr") String sqlStr);



//    @Select("select * from sample_info where #{sqlString}" )
//    List<SampleInfo> queryByChem(String sqlString);
}
