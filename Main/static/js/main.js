/**
 * Created by erfan on 1/27/15.
 */



$(document).ready(function(){
    var r= 255,g= 255,b= 255,o=0.95;

    $('#submit').click(function(){
        $('#myForm').submit();
    });
    $('a').click(function(){
       $('a').css('color','white');
       $(this).css('color','black');
    });
    var setColor = function () {
        $('.changingColor').css('background-color','rgba(' + r + ',' + g + ',' + b + ',' + o + ')');
        $('#submit').css('background-color','rgba(' + r + ',' + g + ',' + b + ',' + 1 + ')');
        $('#banner').css('color','rgb(' + r + ',' + g + ',' + b + ')')
    }
    setColor();
    $('.dropdown div.item').click(function(){
        switch($(this).data('value')){
            case 0:
                r=255;g=255;b=255,o=0.95;
                break;
            case 1:
                r=189;g=237;b=255,o=0.7;
                break;
            case 2:
                r=188;g=198;b=204,o=0.7;
                break;
            case 3:
                r=237;g=218;b=116,o=0.75;
                break;
            case 4:
                r=229;g=228;b=226,o=0.7;
                break;

        }
        setColor();
    })
})
