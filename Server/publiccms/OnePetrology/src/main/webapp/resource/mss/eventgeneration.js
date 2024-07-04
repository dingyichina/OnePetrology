window.onload = function () {
    $.ajax({
        type:"POST",
        url:"http://localhost:8095/eventgeneration",
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