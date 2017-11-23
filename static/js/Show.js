const url = 'json';

fetch(url)
.then((resp) => resp.json())
.then(function(data) {    
    var ctx = document.getElementById("pings").getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.y,
            datasets: [{
                label: '# Ping by Hours',
                data: data.x,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero:true
                    }
                }]
            }
        }
    });
})
.catch(function(error) {
    console.log(error);
});
