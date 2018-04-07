$("ul.nav-pills li.active").toggleClass("active");
/*alert(111);*/

$(document).ready(function(){
    $(".sync_button").on('click',function(){
        $(this).toggleClass('sync_button_checked');
    });
});