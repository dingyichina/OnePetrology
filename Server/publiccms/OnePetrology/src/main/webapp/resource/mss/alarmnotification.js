window.onload = function () {
    $.ajax({
        type:"POST",
        url:"http://localhost:8095/alarmnotification",
        data:{},
        async:true,
        dataType:"json",
        success:function(data){

        },
        error:function(){

        },
        complete:function(){

        }
    });
}