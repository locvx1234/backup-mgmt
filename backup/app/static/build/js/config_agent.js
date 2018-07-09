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
