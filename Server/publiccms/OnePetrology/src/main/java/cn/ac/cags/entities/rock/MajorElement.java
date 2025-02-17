package cn.ac.cags.entities.rock;
// Generated 2020-2-15 13:24:38 by Hibernate Tools 6.0.0-SNAPSHOT


import com.publiccms.common.database.CmsUpgrader;
import com.publiccms.common.generator.annotation.GeneratorColumn;
import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;

/**
 * MajorElement generated by hbm2java
 */
@Entity
@Table(name="major_element"
    ,schema="public"
)
public class MajorElement  implements java.io.Serializable {

     /**
     *
     */
    private static final long serialVersionUID = 1L;
    @GeneratorColumn(title = "ID")
    private Integer id;
    @GeneratorColumn(title = "样品",condition = true,order = true)
    private int sampleId;
    @GeneratorColumn(title = "SiO<sub>2</sub>（10<sup>-2</sup>）")
    private double siO2;
    @GeneratorColumn(title = "TiO<sub>2</sub> (10<sup>-2</sup>）")
    private double tiO2;
    @GeneratorColumn(title = "Al<sub>2</sub>O<sub>3</sub>(10<sup>-2</sup>）")
    private double al2O3;
    @GeneratorColumn(title = "Fe<sub>2</sub>O<sub>3</sub>(10<sup>-2</sup>）")
    private double fe2O3;
    @GeneratorColumn(title = "FeO(10<sup>-2</sup>)")
    private double feO;
    @GeneratorColumn(title = "Tfe(10<sup>-2</sup>)")
    private double tfe;
    @GeneratorColumn(title = "MnO(10<sup>-2</sup>)")
    private double mnO;
    @GeneratorColumn(title = "MgO(10<sup>-2</sup>)")
    private double mgO;
    @GeneratorColumn(title = "CaO(10<sup>-2</sup>)")
    private double caO;
    @GeneratorColumn(title = "Na<sub>2</sub>O(10<sup>-2</sup>)")
    private double na2O;
    @GeneratorColumn(title = "K<sub>2</sub>O(10<sup>-2</sup>)")
    private double k2O;
    @GeneratorColumn(title = "P<sub>2</sub>O<sub>5</sub>(10<sup>-2</sup>)")
    private double p2O5;
    @GeneratorColumn(title = "H<sub>2</sub>O<sub>+(10<sup>-2</sup>)")
    private double h2OP;
    @GeneratorColumn(title = "H<sub>2</sub>O-(10<sup>-2</sup>)")
    private double h2ON;
    @GeneratorColumn(title = "CO<sub>2</sub>(10<sup>-2</sup>)")
    private double CO2;
    @GeneratorColumn(title = "SO<sub>3</sub>(10<sup>-2</sup>)")
    private double SO3;
    @GeneratorColumn(title = "F(10<sup>-2</sup>)")
    private double f;
    @GeneratorColumn(title = "Cl(10<sup>-2</sup>)")
    private double ci;
    @GeneratorColumn(title = "烧失量(10<sup>-2</sup>)")
    private double ignitionLoss;
    @GeneratorColumn(title = "总量(10<sup>-2</sup>)")
    private Double total;
    @GeneratorColumn(title = "备注")
    private String remark;

    public MajorElement() {
    }

	
    public MajorElement(int id, double siO2, double tiO2, double al2O3, double fe2O3, double feO, double tfe, double mnO, double mgO, double caO, double na2O, double k2O, double p2O5, double h2OP, double h2ON, double CO2, double SO3, double f, double ci, double ignitionLoss, int sampleId) {
        this.id = id;
        this.siO2 = siO2;
        this.tiO2 = tiO2;
        this.al2O3 = al2O3;
        this.fe2O3 = fe2O3;
        this.feO = feO;
        this.tfe = tfe;
        this.mnO = mnO;
        this.mgO = mgO;
        this.caO = caO;
        this.na2O = na2O;
        this.k2O = k2O;
        this.p2O5 = p2O5;
        this.h2OP = h2OP;
        this.h2ON = h2ON;
        this.CO2 = CO2;
        this.SO3 = SO3;
        this.f = f;
        this.ci = ci;
        this.ignitionLoss = ignitionLoss;
        this.sampleId = sampleId;
    }
    public MajorElement(int id, double siO2, double tiO2, double al2O3, double fe2O3, double feO, double tfe, double mnO, double mgO, double caO, double na2O, double k2O, double p2O5, double h2OP, double h2ON, double CO2, double SO3, double f, double ci, double ignitionLoss, Double total, String remark, int sampleId) {
        this.id = id;
        this.siO2 = siO2;
        this.tiO2 = tiO2;
        this.al2O3 = al2O3;
        this.fe2O3 = fe2O3;
        this.feO = feO;
        this.tfe = tfe;
        this.mnO = mnO;
        this.mgO = mgO;
        this.caO = caO;
        this.na2O = na2O;
        this.k2O = k2O;
        this.p2O5 = p2O5;
        this.h2OP = h2OP;
        this.h2ON = h2ON;
        this.CO2 = CO2;
        this.SO3 = SO3;
        this.f = f;
        this.ci = ci;
        this.ignitionLoss = ignitionLoss;
        this.total = total;
        this.remark = remark;
        this.sampleId = sampleId;
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

    @Column(name="sample_id", nullable=false)
    public int getSampleId() {
        return this.sampleId;
    }

    public void setSampleId(int sampleId) {
        this.sampleId = sampleId;
    }
    
    @Column(name="si_o2", nullable=false, precision=17, scale=17)
    public double getSiO2() {
        return this.siO2;
    }
    
    public void setSiO2(double siO2) {
        this.siO2 = siO2;
    }
    
    @Column(name="ti_o2", nullable=false, precision=17, scale=17)
    public double getTiO2() {
        return this.tiO2;
    }
    
    public void setTiO2(double tiO2) {
        this.tiO2 = tiO2;
    }
    
    @Column(name="al2_o3", nullable=false, precision=17, scale=17)
    public double getAl2O3() {
        return this.al2O3;
    }
    
    public void setAl2O3(double al2O3) {
        this.al2O3 = al2O3;
    }
    
    @Column(name="fe2_o3", nullable=false, precision=17, scale=17)
    public double getFe2O3() {
        return this.fe2O3;
    }
    
    public void setFe2O3(double fe2O3) {
        this.fe2O3 = fe2O3;
    }
    
    @Column(name="fe_o", nullable=false, precision=17, scale=17)
    public double getFeO() {
        return this.feO;
    }
    
    public void setFeO(double feO) {
        this.feO = feO;
    }
    
    @Column(name="tfe", nullable=false, precision=17, scale=17)
    public double getTfe() {
        return this.tfe;
    }
    
    public void setTfe(double tfe) {
        this.tfe = tfe;
    }
    
    @Column(name="mn_o", nullable=false, precision=17, scale=17)
    public double getMnO() {
        return this.mnO;
    }
    
    public void setMnO(double mnO) {
        this.mnO = mnO;
    }
    
    @Column(name="mg_o", nullable=false, precision=17, scale=17)
    public double getMgO() {
        return this.mgO;
    }
    
    public void setMgO(double mgO) {
        this.mgO = mgO;
    }
    
    @Column(name="ca_o", nullable=false, precision=17, scale=17)
    public double getCaO() {
        return this.caO;
    }
    
    public void setCaO(double caO) {
        this.caO = caO;
    }
    
    @Column(name="na2_o", nullable=false, precision=17, scale=17)
    public double getNa2O() {
        return this.na2O;
    }
    
    public void setNa2O(double na2O) {
        this.na2O = na2O;
    }
    
    @Column(name="k2_o", nullable=false, precision=17, scale=17)
    public double getK2O() {
        return this.k2O;
    }
    
    public void setK2O(double k2O) {
        this.k2O = k2O;
    }
    
    @Column(name="p2_o5", nullable=false, precision=17, scale=17)
    public double getP2O5() {
        return this.p2O5;
    }
    
    public void setP2O5(double p2O5) {
        this.p2O5 = p2O5;
    }
    
    @Column(name="h2_o_p", nullable=false, precision=17, scale=17)
    public double getH2OP() {
        return this.h2OP;
    }
    
    public void setH2OP(double h2OP) {
        this.h2OP = h2OP;
    }
    
    @Column(name="h2_o_n", nullable=false, precision=17, scale=17)
    public double getH2ON() {
        return this.h2ON;
    }
    
    public void setH2ON(double h2ON) {
        this.h2ON = h2ON;
    }
    
    @Column(name="c_o2", nullable=false, precision=17, scale=17)
    public double getCO2() {
        return this.CO2;
    }
    
    public void setCO2(double CO2) {
        this.CO2 = CO2;
    }
    
    @Column(name="s_o3", nullable=false, precision=17, scale=17)
    public double getSO3() {
        return this.SO3;
    }
    
    public void setSO3(double SO3) {
        this.SO3 = SO3;
    }
    
    @Column(name="f", nullable=false, precision=17, scale=17)
    public double getF() {
        return this.f;
    }
    
    public void setF(double f) {
        this.f = f;
    }
    
    @Column(name="ci", nullable=false, precision=17, scale=17)
    public double getCi() {
        return this.ci;
    }
    
    public void setCi(double ci) {
        this.ci = ci;
    }
    
    @Column(name="ignition_loss", nullable=false, precision=17, scale=17)
    public double getIgnitionLoss() {
        return this.ignitionLoss;
    }
    
    public void setIgnitionLoss(double ignitionLoss) {
        this.ignitionLoss = ignitionLoss;
    }
    
    @Column(name="total", precision=17, scale=17)
    public Double getTotal() {
        return this.total;
    }
    
    public void setTotal(Double total) {
        this.total = total;
    }
    
    @Column(name="remark", length=50)
    public String getRemark() {
        return this.remark;
    }
    
    public void setRemark(String remark) {
        this.remark = remark;
    }




}


