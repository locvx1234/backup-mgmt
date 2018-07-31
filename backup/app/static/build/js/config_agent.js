// Copy 
function myFunction(my_id) {
    // Create an auxiliary hidden input
    var aux = document.createElement("input");
    // Get the text from the element passed into the input
    aux.setAttribute("value", document.getElementById(my_id).innerHTML);
    // Append the aux input to the body
    document.body.appendChild(aux);
    aux.select();
    document.execCommand("copy");
    document.body.removeChild(aux);
}

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

$(function () {
    // $('#datetime-div').hide();
    $('#day-div').hide();
    $('#time-div').hide();
    $('#typeofbackup').change(function () {
        if ($('#typeofbackup').val() == '0') {
            $('#datetime-div').show();
            $('#datetime').prop('required',true);
            $('#day-div').hide();
            $('#day_select').prop('required',false);
            $('#time-div').hide();
            $('#time').prop('required',false);
        }
        else if ($('#typeofbackup').val() == '1') {
            $('#datetime-div').hide();
            $('#datetime').prop('required',false);
            $('#time-div').show();
            $('#time').prop('required',true);
            $('#day-div').hide();
            $('#day_select').prop('required',false);
        }
        else {
            $('#datetime-div').hide();
            $('#datetime').prop('required',false);
            $('#day-div').show();
            $('#day_select').prop('required',true);
            $('#time-div').show();
            $('#time').prop('required',true);
        }
    });
});
