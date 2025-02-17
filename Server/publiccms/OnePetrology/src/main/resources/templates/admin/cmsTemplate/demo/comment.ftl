<#ftl auto_esc=false/>
[<#macro merge name value><#if !.vars[name]??><@"<#assign ${name}=''>"?interpret /></#if><#if value??><@"<#assign ${name}=${name}+'${value},'>"?interpret /></#if></#macro>
<@_commentList contentId=contentId pageIndex=pageIndex>
    <#list page.list as a>
        <@merge 'userIds' a.userId!/>
        <@merge 'userIds' a.replyUserId!/>
    </#list>
    <@_sysUser ids=userIds!><#assign userMap=map!/></@_sysUser>
    <#list page.list as a>
        {
            "userId":"${a.userId}",
            "userNickName":"${userMap[a.userId?string].nickName}",
            "createDate":"${a.createDate}",
            <#if a.replyId?has_content>
                "replay":{
                <@_comment id=a.replyId>
                    "userId":"${a.userId}",
                    "userNickName":"${userMap[a.replyUserId?string].nickName}",
                    "text":"${object.text!}"
                </@_comment>
                },
            </#if>
            "text":${a.text!}"
        }<#sep>,
    </#list>
</@_commentList>]