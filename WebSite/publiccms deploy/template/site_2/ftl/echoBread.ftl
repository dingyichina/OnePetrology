	<a href="${site.sitePath}">首页</a>
<#macro echoBread parentId>
	<#if parentId?has_content>
		<@_category id=parentId>
			<#if object.parentId?has_content>
				<@echoBread object.parentId!/>
			</#if>
				  &gt; <a href="${object.url!}" data-id="${object.id}">${object.name!}</a>
		</@_category>
	</#if>
</#macro>