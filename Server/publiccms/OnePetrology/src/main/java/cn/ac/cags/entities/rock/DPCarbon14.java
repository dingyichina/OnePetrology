package cn.ac.cags.entities.rock;
// Generated 2020-2-15 13:24:38 by Hibernate Tools 6.0.0-SNAPSHOT


import com.publiccms.common.database.CmsUpgrader;
import com.publiccms.common.generator.annotation.GeneratorColumn;
import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;

/**
 * DPCarbon14 generated by hbm2java
 */
@Entity
@Table(name="d_p_carbon_14"
    ,schema="public"
)
public class DPCarbon14  implements java.io.Serializable {

     /**
     *
     */
    private static final long serialVersionUID = 1L;
    @GeneratorColumn(title = "ID")
    private Integer id;
    @GeneratorColumn(title = "衰变常数 （1/年）")
    private Double decayConst;
    @GeneratorColumn(title = "放射性比度（dpm/g）")
    private Double radioActivSpecific;
    @GeneratorColumn(title = "碳-14 年龄（万年）")
    private Double c14Age;
    @GeneratorColumn(title = "年龄误差(Ma)")
    private Double ageError;
    @GeneratorColumn(title = "备注")
    private String remark;
    @GeneratorColumn(title = "样品")
    private int sampleId;


    public DPCarbon14() {
    }


    public DPCarbon14(int id, int sampleId) {
        this.id = id;
        this.sampleId = sampleId;
    }
    public DPCarbon14(int id, Double decayConst, Double radioActivSpecific, Double c14Age, Double ageError, String remark, int sampleId) {
        this.id = id;
        this.decayConst = decayConst;
        this.radioActivSpecific = radioActivSpecific;
        this.c14Age = c14Age;
        this.ageError = ageError;
        this.remark = remark;
        this.sampleId = sampleId;
    }
   
    @Id
    @GeneratedValue(generator = "cmsGenerator")
    @GenericGenerator(name = "cmsGenerator", strategy = CmsUpgrader.IDENTIFIER_GENERATOR)    @Column(name="id", unique=true, nullable=false)
    public Integer getId() {
        return this.id;
    }
    
    public void setId(Integer id) {
        this.id = id;
    }

    
    @Column(name="decay_const", precision=17, scale=17)
    public Double getDecayConst() {
        return this.decayConst;
    }
    
    public void setDecayConst(Double decayConst) {
        this.decayConst = decayConst;
    }
    
    @Column(name="radio_activ_specific", precision=17, scale=17)
    public Double getRadioActivSpecific() {
        return this.radioActivSpecific;
    }
    
    public void setRadioActivSpecific(Double radioActivSpecific) {
        this.radioActivSpecific = radioActivSpecific;
    }
    
    @Column(name="c_14_age", precision=17, scale=17)
    public Double getC14Age() {
        return this.c14Age;
    }
    
    public void setC14Age(Double c14Age) {
        this.c14Age = c14Age;
    }
    
    @Column(name="age_error", precision=17, scale=17)
    public Double getAgeError() {
        return this.ageError;
    }
    
    public void setAgeError(Double ageError) {
        this.ageError = ageError;
    }
    
    @Column(name="remark", length=80)
    public String getRemark() {
        return this.remark;
    }
    
    public void setRemark(String remark) {
        this.remark = remark;
    }

    @Column(name="sample_id", nullable=false)
    public int getSampleId() {
        return this.sampleId;
    }

    public void setSampleId(int sampleId) {
        this.sampleId = sampleId;
    }




}

