
/**$('#like').onclick(function(){
    var pk = $(this).attr('place')
    let likeVal = 1

    $.ajax({
        url : pk,
        type : 'POST',
        data :{'pk':pk,'likeVal':likeVal},

        success:function(response){
            $('#like').html(response.second)
        },
        error:function(){
            ElementInternals('실패');
        }

    })



})**/


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





    $("#like").click(function(){
        $.ajax({
            url : '',
            type : 'POST',
            data :{like_text: $(this).text()},
    
            success:function(response){
                $('#like').text(response.second)
            },
            error:function(){
                ElementInternals('실패');
            }
        });
    });


});