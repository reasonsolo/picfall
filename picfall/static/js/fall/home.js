

function isOnScreen(element)
{
    var curPos = element.offset();
    var curTop = curPos.top;
    var screenHeight = $(window).height();
    return (curTop > screenHeight) ? false : true;
}



$(document).ready(function() {
    pictures = window.Pictures();
    if (isOnScreen($('#endofpage'))) {
        pictures._fetch_page();
    }
    $(window).scroll(function(){
    if  ($(window).scrollTop() == $(document).height() - $(window).height()){
        pictures._fetch_page();
    }});
});



