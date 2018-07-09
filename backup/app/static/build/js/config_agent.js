// $("ul.nav-pills li.active").toggleClass("active");
/*alert(111);*/

$(function () {
    $('#datetimepicker1').datetimepicker({
        format: 'YYYY-MM-DD HH:mm'
    });
});

$(function () {
    $('#timepicker1').datetimepicker({
        format: 'HH:mm'
    });
});

$(document).ready(function() {
    $('#dt1').DataTable();
});