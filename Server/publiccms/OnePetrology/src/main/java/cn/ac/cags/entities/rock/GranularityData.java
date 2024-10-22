package cn.ac.cags.entities.rock;
// Generated 2020-2-15 13:24:38 by Hibernate Tools 6.0.0-SNAPSHOT


import com.publiccms.common.database.CmsUpgrader;
import com.publiccms.common.generator.annotation.GeneratorColumn;
import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;

/**
 * GranularityData generated by hbm2java
 */
@Entity
@Table(name="granularity_data"
    ,schema="public"
)
public class GranularityData  implements java.io.Serializable {

     /**
     *
     */
    private static final long serialVersionUID = 1L;
    @GeneratorColumn(title = "ID")
    private Integer id;
    @GeneratorColumn(title = "样品",condition = true,order = true)
    private Integer sampleId;
    @GeneratorColumn(title = "φ 值分组")
    private String phiValueGroup;
    @GeneratorColumn(title = "颗粒数")
    private Integer particleNumber;
    @GeneratorColumn(title = "百分含量（%）")
    private Double percentage;

    public GranularityData() {
    }


    public GranularityData(int id) {
        this.id = id;
    }
    public GranularityData(int id, String phiValueGroup, Integer sampleId, Integer particleNumber, Double percentage) {
        this.id = id;
        this.phiValueGroup = phiValueGroup;
        this.sampleId = sampleId;
        this.particleNumber = particleNumber;
        this.percentage = percentage;
    }
   
    @Id
    @GeneratedValue(generator = "cmsGenerator")
    @GenericGenerator(name = "cmsGenerator", strategy = CmsUpgrader.IDENTIFIER_GENERATOR)
    @Column(name="id", unique=true, nullable=false)
    public Integer getId() {
        return this.id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    @Column(name="sample_id")
    public Integer getSampleId() {
        return this.sampleId;
    }

    public void setSampleId(Integer sampleId) {
        this.sampleId = sampleId;
    }
    
    @Column(name="phi_value_group", length=15)
    public String getPhiValueGroup() {
        return this.phiValueGroup;
    }
    
    public void setPhiValueGroup(String phiValueGroup) {
        this.phiValueGroup = phiValueGroup;
    }
    
    @Column(name="particle_number")
    public Integer getParticleNumber() {
        return this.particleNumber;
    }
    
    public void setParticleNumber(Integer particleNumber) {
        this.particleNumber = particleNumber;
    }
    
    @Column(name="percentage", precision=17, scale=17)
    public Double getPercentage() {
        return this.percentage;
    }
    
    public void setPercentage(Double percentage) {
        this.percentage = percentage;
    }




}


