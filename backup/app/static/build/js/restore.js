$('#bid_select').click(function () {
    var bid = $(this).val();
    $.ajax({
        type: "GET",
        beforeSend: function(request) {
            request.setRequestHeader("Authorization", token);
        },
        url: 'http://' + core_domain + "/rest/api/get-paths/" + bid + "/",
        dataType: 'json',
        success: function (data) {

            console.log(data);
            var paths = $('#target_select');
            paths.empty();
            console.log(data.paths)
            $.each(data.paths, function (i, val) {

                paths.append(
                        $('<option>', {
                            value: this.Value
                        }).text(val)
                    );
            });
        },
        failure: function(data) {
            alert('Got an error dude');
        },
        
    });
});

$('#target_select').click(function () {
    var path = $(this).val();
    $.ajax({
        type: "GET",
        beforeSend: function(request) {
            request.setRequestHeader("Authorization", token);
        },
        url: 'http://' + core_domain + "/rest/api/get-backups/",
        data: {
            path: path
        },
        dataType: 'json',
        success: function (data) {

            var backups = $('#bid_select');
            backups.empty();
            $.each(data.backups, function (i, val) {
                backups.append(
                        $('<option>', {
                            value: val['pk']
                        }).text(val['date'])
                    );
            });
        },
        failure: function(data) {
            alert('Got an error dude');
        },
        
    });
});