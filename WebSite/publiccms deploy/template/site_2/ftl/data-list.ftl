	<li class="hoverShadow clearfix-after">		
		<#if a.hasImages>			
			<div class="article-title">
				<h3><a href="<#if a.onlyUrl>${site.dynamicPath}content/redirect?id=${a.id}<#else>${a.url!}</#if>">${a.title}</a></h3>
				<div class="clearfix-after">			
			<@_contentFileList contentId=a.id fileTypes='image' count=4>
				<#list page.list as i>
					<a href="<#if a.onlyUrl>${site.dynamicPath}content/redirect?id=${a.id}<#else>${a.url!}</#if>">	<figure class="image-list"><img src="<@_thumb path=i.filePath width=160 height=120/>" alt="${a.title}"/></figure></a>
				</#list>
			</@_contentFileList>
				</div>
				<p class="info">
					<span><a href="${a.url}#comments">${a.comments}评论</a></span>
					<span><a href="${site.dynamicPath}comment.html?contentId=${a.id}">${a.scores}赞</a></span>
					<span>${a.publishDate?date}</span>
				</p>
			</div>
		<#else>
			<#if a.cover?has_content>
				<a href="<#if a.onlyUrl>${site.dynamicPath}content/redirect?id=${a.id}<#else>${a.url!}</#if>"><figure><img src="<@_thumb path=a.cover width=160 height=120/>" alt="${a.title}"/></figure></a>
			</#if>
			<div class="article-title">
				<h3><a href="<#if a.onlyUrl>${site.dynamicPath}content/redirect?id=${a.id}<#else>${a.url!}</#if>">${a.title}</a></h3>
				<p>${a.description!}</p>
				<p class="info">
					<span><a href="${a.url}#comments">${a.comments}评论</a></span>
					<span><a href="${site.dynamicPath}comment.html?contentId=${a.id}">${a.scores}赞</a></span>
					<span>${a.publishDate?date}</span>
				</p>
			</div>
		</#if>		
	</li>