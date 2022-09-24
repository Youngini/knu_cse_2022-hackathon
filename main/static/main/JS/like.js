$(document).ready(function(){

    $("#btn").click(function(){
        $.ajax({
            url : '',
            type : 'get',
            data :{button_text: $(this).text()},
    
            success:function(response){
                $('#btn').text(response.second)
            },
            error:function(){
                ElementInternals('실패');
            }
        });
    });

});



window.onload = function(){
    $(".like").click(function(){
        var pk = $(this).attr('name');
        $.ajax({
            url : 'tourSpot',
            type : 'POST',
            dataType:'json',
            data :{
                'like_text': $(this).text(),
                'pk' : pk
            },
    
            success:function(response){
                $('.like').text(response.second)
            },
            error:function(){
                ElementInternals('실패');
            }
        });
    });



    $(".unlike").click(function(){
        var pk = $(this).attr('name');
        $.ajax({
            url : 'tourSpot',
            type : 'POST',
            dataType:'json',
            data :{
                'like_text': $(this).text(),
                'pk' : pk
            },
    
            success:function(response){
                $('.unlike').text(response.second)
            },
            error:function(){
                ElementInternals('실패');
            }
        });
    });



}
