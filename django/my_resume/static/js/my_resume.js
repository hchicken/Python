$(document).ready(function () {
    $('.div2').hover(function () {
        $(this).children('div:first-child').css("opacity",'0.5');
        $(this).find("ul").css("display",'block')
    });
    $('.div2').mouseleave(function () {
        $(this).children('div:first-child').css("opacity",'1');
        $('.ul_1').css("display",'none')
    })
})

$(document).ready(function(){
    var myVar=setInterval(function () {
        mytime()
    },3000);
    function mytime() {
        var x = $("div").scrollTop();
        if(x>100){
            alert(x)
        }
    }
});



