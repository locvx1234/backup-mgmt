function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

$(document).ready(function(){
    var ctx = document.getElementById("mycanvas");
    var labels = [];
    var data_value = [];

    var table = document.getElementById('myTable');
    for (var r = 1, n = table.rows.length; r < n; r++) {
        labels.push(table.rows[r].cells[0].innerHTML);
        data_value.push(table.rows[r].cells[1].innerHTML);
    }

    var color_set = [];
    for (var item = 0; item < labels.length ; item++ ) {
        color_set.push(getRandomColor() )
    }

    var data = {
        labels: labels,
        datasets: [{
            data: data_value,
            backgroundColor: color_set
        }]
    };

    var canvasDoughnut = new Chart(ctx, {
        type: 'doughnut',
        tooltipFillColor: "rgba(51, 51, 51, 0.55)",
        data: data
    });

});