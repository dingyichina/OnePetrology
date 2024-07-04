package cn.ac.cags.vo;

public class SampleInfoVO {
    private String originalSampleId;
   // //@GeneratorColumn(title = "地理经度",order = true)
    private Double longitude;
   // //@GeneratorColumn(title = "地理纬度",order = true)
    private Double latitude;
    //@GeneratorColumn(title = "国家编码",condition = true,order = true)
    private String countryCode;
    //@GeneratorColumn(title = "所在地区",condition = true,like=true,order = true)
    private String location;
    //@GeneratorColumn(title = "岩性",condition=true,order=true)
    private String lithology;
    //@GeneratorColumn(title = "岩石名称",condition=true,order=true)
    private String rockName;
    //@GeneratorColumn(title = "岩石名称代码",condition = true,order = true)
    private String rockCode;
    //@GeneratorColumn(title = "地质年代",condition=true,order=true)
    private String era;
    //@GeneratorColumn(title = "地质体名称",condition=true,order=true)
    private String geobodyName;
    //@GeneratorColumn(title = "地质体代码",condition=true,order=true)
    private String geobodyCode;

    //@GeneratorColumn(title = "构造位置",condition = true,order = true,like = true)
    private String tectonicLocation;
    /* @GeneratorColumn(title = "一级构造单元",condition = true,order = true,like = true) */
    private String primaryStructuralUnit;
    //@GeneratorColumn(title = "二级构造单元",condition = true,order = true,like = true)
    private String secondaryStructuralUnit;
    //@GeneratorColumn(title = "三级构造单元",condition = true,order = true,like = true)
    private String tertiarySturcturalUnit;
    //@GeneratorColumn(title = "围岩时代",condition = true,order = true,like = true)
    private String surroundingRockAge;
    //@GeneratorColumn(title = "围岩岩性",condition = true,order = true,like = true)
    private String surroundingRockLithology;
    //@GeneratorColumn(title = "与围岩关系",condition = true,order = true,like = true)
    private String relationshipWithSurroundingRock;
    //@GeneratorColumn(title = "形态",condition = true,order = true,like = true)
    private String form;
    //@GeneratorColumn(title = "是否切割区域构造线",condition = true,order = true)
    private String cutAreaConstructionLine;
    //@GeneratorColumn(title = "变形程度",condition = true,order = true,like = true)
    private String degreeOfDeformation;
    //@GeneratorColumn(title = "特征矿物",condition = true,order = true,like = true)
    private String characteristicMinerals;
    //@GeneratorColumn(title = "成因类型",condition = true,order = true,like = true)
    private String geneticType;

    //@GeneratorColumn(title = "构造类型",condition = true,order = true,like = true)
    private String tectonicType;
    //@GeneratorColumn(title = "构造类型判别来源",condition = true,order = true,like = true)
    private String sourceOfStructuralTypeDiscrimination;
    //@GeneratorColumn(title = "碱性程度",condition = true,order = true,like = true)
    private String alkalinity;
    //@GeneratorColumn(title = "铝质程度",condition = true,order = true,like = true)
    private String aluminumQuality;

    //@GeneratorColumn(title = "年龄",order = true)
    private Double age;
    //@GeneratorColumn(title = "年龄误差",order = true)
    private Double ageError;

    //@GeneratorColumn(title = "样品照片",order = true)
    private String photo;
    //@GeneratorColumn(title = "样品采集人员",condition=true,order=true,like=true)
    private String collector;
    //@GeneratorColumn(title = "采集人员单位",condition=true,order=true,like=true)
    private String collectorOrg;
    //@GeneratorColumn(title = "样品审核人",condition=true,order=true,like=true)
    private String reviewer;
    //@GeneratorColumn(title = "分析/鉴定单位",condition=true,order=true,like=true)
    private String analyzeOrg;
    //@GeneratorColumn(title = "分析/鉴定人员",condition=true,order=true,like=true)
    private String analyzePerson;

    //@GeneratorColumn(title = "测试对象",condition = true,order = true,like = true)
    private String testObject;

    //@GeneratorColumn(title = "分析/测定时间",condition=true,order=true,like=true)
    private String testDate;
    //@GeneratorColumn(title = "分析/测定方法",condition=true,order=true,like=true)
    private String testMethod;
    //@GeneratorColumn(title = "选用年龄",order = true)
    private Double ageSelected;
    //@GeneratorColumn(title = "选用年龄误差",order = true)
    private Double ageSelectedError;


    //@GeneratorColumn(title = "发表文献编号",order = true)
    private Integer articleId;

    //@GeneratorColumn(title = "文章DOI",condition = true,order = true,like = true)
    private String articleDoi;

    //@GeneratorColumn(title = "备注")
    private String remark;

    public String getOriginalSampleId() {
        return originalSampleId;
    }

    public void setOriginalSampleId(String originalSampleId) {
        this.originalSampleId = originalSampleId;
    }

    public Double getLongitude() {
        return longitude;
    }

    public void setLongitude(Double longitude) {
        this.longitude = longitude;
    }

    public Double getLatitude() {
        return latitude;
    }

    public void setLatitude(Double latitude) {
        this.latitude = latitude;
    }

    public String getCountryCode() {
        return countryCode;
    }

    public void setCountryCode(String countryCode) {
        this.countryCode = countryCode;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getLithology() {
        return lithology;
    }

    public void setLithology(String lithology) {
        this.lithology = lithology;
    }

    public String getRockName() {
        return rockName;
    }

    public void setRockName(String rockName) {
        this.rockName = rockName;
    }

    public String getRockCode() {
        return rockCode;
    }

    public void setRockCode(String rockCode) {
        this.rockCode = rockCode;
    }

    public String getEra() {
        return era;
    }

    public void setEra(String era) {
        this.era = era;
    }

    public String getGeobodyName() {
        return geobodyName;
    }

    public void setGeobodyName(String geobodyName) {
        this.geobodyName = geobodyName;
    }

    public String getGeobodyCode() {
        return geobodyCode;
    }

    public void setGeobodyCode(String geobodyCode) {
        this.geobodyCode = geobodyCode;
    }

    public String getTectonicLocation() {
        return tectonicLocation;
    }

    public void setTectonicLocation(String tectonicLocation) {
        this.tectonicLocation = tectonicLocation;
    }

    public String getPrimaryStructuralUnit() {
        return primaryStructuralUnit;
    }

    public void setPrimaryStructuralUnit(String primaryStructuralUnit) {
        this.primaryStructuralUnit = primaryStructuralUnit;
    }

    public String getSecondaryStructuralUnit() {
        return secondaryStructuralUnit;
    }

    public void setSecondaryStructuralUnit(String secondaryStructuralUnit) {
        this.secondaryStructuralUnit = secondaryStructuralUnit;
    }

    public String getTertiarySturcturalUnit() {
        return tertiarySturcturalUnit;
    }

    public void setTertiarySturcturalUnit(String tertiarySturcturalUnit) {
        this.tertiarySturcturalUnit = tertiarySturcturalUnit;
    }

    public String getSurroundingRockAge() {
        return surroundingRockAge;
    }

    public void setSurroundingRockAge(String surroundingRockAge) {
        this.surroundingRockAge = surroundingRockAge;
    }

    public String getSurroundingRockLithology() {
        return surroundingRockLithology;
    }

    public void setSurroundingRockLithology(String surroundingRockLithology) {
        this.surroundingRockLithology = surroundingRockLithology;
    }

    public String getRelationshipWithSurroundingRock() {
        return relationshipWithSurroundingRock;
    }

    public void setRelationshipWithSurroundingRock(String relationshipWithSurroundingRock) {
        this.relationshipWithSurroundingRock = relationshipWithSurroundingRock;
    }

    public String getForm() {
        return form;
    }

    public void setForm(String form) {
        this.form = form;
    }

    public String getCutAreaConstructionLine() {
        return cutAreaConstructionLine;
    }

    public void setCutAreaConstructionLine(String cutAreaConstructionLine) {
        this.cutAreaConstructionLine = cutAreaConstructionLine;
    }

    public String getDegreeOfDeformation() {
        return degreeOfDeformation;
    }

    public void setDegreeOfDeformation(String degreeOfDeformation) {
        this.degreeOfDeformation = degreeOfDeformation;
    }

    public String getCharacteristicMinerals() {
        return characteristicMinerals;
    }

    public void setCharacteristicMinerals(String characteristicMinerals) {
        this.characteristicMinerals = characteristicMinerals;
    }

    public String getGeneticType() {
        return geneticType;
    }

    public void setGeneticType(String geneticType) {
        this.geneticType = geneticType;
    }

    public String getTectonicType() {
        return tectonicType;
    }

    public void setTectonicType(String tectonicType) {
        this.tectonicType = tectonicType;
    }

    public String getSourceOfStructuralTypeDiscrimination() {
        return sourceOfStructuralTypeDiscrimination;
    }

    public void setSourceOfStructuralTypeDiscrimination(String sourceOfStructuralTypeDiscrimination) {
        this.sourceOfStructuralTypeDiscrimination = sourceOfStructuralTypeDiscrimination;
    }

    public String getAlkalinity() {
        return alkalinity;
    }

    public void setAlkalinity(String alkalinity) {
        this.alkalinity = alkalinity;
    }

    public String getAluminumQuality() {
        return aluminumQuality;
    }

    public void setAluminumQuality(String aluminumQuality) {
        this.aluminumQuality = aluminumQuality;
    }

    public Double getAge() {
        return age;
    }

    public void setAge(Double age) {
        this.age = age;
    }

    public Double getAgeError() {
        return ageError;
    }

    public void setAgeError(Double ageError) {
        this.ageError = ageError;
    }

    public String getPhoto() {
        return photo;
    }

    public void setPhoto(String photo) {
        this.photo = photo;
    }

    public String getCollector() {
        return collector;
    }

    public void setCollector(String collector) {
        this.collector = collector;
    }

    public String getCollectorOrg() {
        return collectorOrg;
    }

    public void setCollectorOrg(String collectorOrg) {
        this.collectorOrg = collectorOrg;
    }

    public String getReviewer() {
        return reviewer;
    }

    public void setReviewer(String reviewer) {
        this.reviewer = reviewer;
    }

    public String getAnalyzeOrg() {
        return analyzeOrg;
    }

    public void setAnalyzeOrg(String analyzeOrg) {
        this.analyzeOrg = analyzeOrg;
    }

    public String getAnalyzePerson() {
        return analyzePerson;
    }

    public void setAnalyzePerson(String analyzePerson) {
        this.analyzePerson = analyzePerson;
    }

    public String getTestObject() {
        return testObject;
    }

    public void setTestObject(String testObject) {
        this.testObject = testObject;
    }

    public String getTestDate() {
        return testDate;
    }

    public void setTestDate(String testDate) {
        this.testDate = testDate;
    }

    public String getTestMethod() {
        return testMethod;
    }

    public void setTestMethod(String testMethod) {
        this.testMethod = testMethod;
    }

    public Double getAgeSelected() {
        return ageSelected;
    }

    public void setAgeSelected(Double ageSelected) {
        this.ageSelected = ageSelected;
    }

    public Double getAgeSelectedError() {
        return ageSelectedError;
    }

    public void setAgeSelectedError(Double ageSelectedError) {
        this.ageSelectedError = ageSelectedError;
    }

    public Integer getArticleId() {
        return articleId;
    }

    public void setArticleId(Integer articleId) {
        this.articleId = articleId;
    }

    public String getArticleDoi() {
        return articleDoi;
    }

    public void setArticleDoi(String articleDoi) {
        this.articleDoi = articleDoi;
    }

    public String getRemark() {
        return remark;
    }

    public void setRemark(String remark) {
        this.remark = remark;
    }
}
