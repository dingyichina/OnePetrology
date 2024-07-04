# OnePetrology

![OnePetrology Igneous Database ](../images/logo.png) 
![DDE of IUGS](../images/ddelogo.png)

Currently, the server side of OnePetrology includes the following components:

1.Relational Database: PostgreSQL is recommended, version 13 or above, with the integration of PostGIS. Its functions include: providing database support for CMS (which uses Publiccms), providing Institutional Repository (IR) support for DSpace, and providing spatial data storage support for the WebGIS Server.

2.[Publiccms](https://publiccms.com/)：Provides CMS functionality for the website, please comply with its licensing rules. OnePetrology has purchased its authorization.

3.DSpace Server： It is recommended to deploy version 7.5 or higher of the server, including the required Solr, Cantaloupe, etc. For details, please refer to the relevant documentation of DSpace.

4.[Arangodb](https://arangodb.com/):OnePetrology has deployed its community version, please adhere to its licensing principles when using it.

5.WebGIS Server： It is recommended to use [Worldwind-serverkit](https://github.com/NASAWorldWind/WorldWindServerKit/releases),which is encapsulated based on GeoServer. You can also choose the version of GeoServer for deployment according to your own needs. It mainly provides WMTS/TMS/WFS and other functions.

6.Self-developed FastAPI services, mainly providing integrated services for knowledge and data. For specific code, see the API Server module. Deploy according to Python rules. Load balance by starting different services on different servers and ports.

7.The above services are integrated through Nginx, for load balancing and reverse proxy, etc.

