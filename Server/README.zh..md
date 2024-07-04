# OnePetrology
![OnePetrology Igneous Database ](../images/logo.png) 
![DDE of IUGS](../images/ddelogo.png)

目前OnePetrology的Server端包括如下几个部分：

1.关系数据库：postgresql ，推荐13或以上，集成postgis。它的作用包括：为cms（采用的是[publiccms](https://publiccms.com/)) 提供DB支撑，为[DSpace](https://www.dspace.org/)(用来为DSpace提供IR支撑)，为WebGIS Server提供空间存储支撑；

2.[Publiccms](https://publiccms.com/)：为Website提供CMS功能，请遵循其授权规则。OnePetrology已购买其授权。

3.DSpace Server：推荐部署7.5及以上版本的Server端，包括其所需要的Solr、Cantolope等，具体请参考DSpace有关文档。

4.[Arangodb](https://arangodb.com/):OnePetrology部署了其社区版本，请使用时遵循其授权原则。

5.WebGIS Server：推荐采用[Worldwind-serverkit](https://github.com/NASAWorldWind/WorldWindServerKit/releases),其基于geoserver进行了封装。也可以自行按照geoserver选择版本进行部署。主要提供wmts/tms/wfs等功能。

6.自研的FastAPI服务，主要提供知识与数据的一体化服务。具体代码参看API Server模块。按照Python规则进行部署。把不同负载起在不同服务器和端口上进行负载均衡。

7.以上服务通过Nginx进行整合，进行负载均衡和反向代理等。
