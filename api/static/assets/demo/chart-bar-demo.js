// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
// mon_script.js

document.addEventListener('DOMContentLoaded', function () {
    // Utilisez les données définies dans le script
    var ctx = document.getElementById('myBarChart').getContext('2d');
    var myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: attackTypes,
            datasets: [{
                label: 'Distribution of Attacks',
                backgroundColor: ['#ffcc99', '#c2c2f0'],
                borderColor: '#000',
                borderWidth: 1,
                data: count
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }],
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            title: {
                display: true,
                text: 'Distribution of Attacks'
            },
            legend: {
                display: false
            },
            animation: {
                duration: 5000, // Durée de l'animation en millisecondes (2 secondes dans cet exemple)
                easing: 'easeInOutQuad' // Type d'animation (vous pouvez choisir un autre type si vous le souhaitez)
            }
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    // Utilisez les données définies dans le script
    var ctx1 = document.getElementById('myBarChart1').getContext('2d');
    var myBarChart1 = new Chart(ctx1, {
        type: 'bar',
        data: {
            labels: protocolType,
            datasets: [{
                label: 'Type of protocoles',
                backgroundColor: ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0'],
                data: countsProtocolType,
                borderColor: '#000',
                borderWidth: 1,
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }],
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            title: {
                display: true,
                text: 'Protocole Types'
            },
            legend: {
                display: false
            },
            animation: {
                duration: 2000, // Durée de l'animation en millisecondes (2 secondes dans cet exemple)
                easing: 'linear' // Type d'animation (vous pouvez choisir un autre type si vous le souhaitez)
            }
        }
    });
});
document.addEventListener('DOMContentLoaded', function () {
    // Utilisez les données définies dans le script
    var ctx = document.getElementById('myProtocolAttackChart').getContext('2d');

    // Créez un tableau de couleurs pour chaque type d'attaque (au format hexadécimal)
    var colors = ['#cc99cc', '#36A2EB', '#FFCE56']; // Ajoutez ou modifiez les couleurs au besoin

    var myProtocolAttackChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: protocolTypes,
            datasets: attackTypes.map(function (attack, index) {
                return {
                    label: attack,
                    backgroundColor: colors[index],
                    borderColor: '#000', // Couleur de la bordure (au format hexadécimal)
                    borderWidth: 1,
                    data: countsByProtocol.map(function (count) {
                        return count[index];
                    })
                };
            })
        },
        options: {
            scales: {
                xAxes: [{
                    stacked: true
                }],
                yAxes: [{
                    stacked: true
                }]
            },
            title: {
                display: true,
                text: 'Distribution of Attacks'
            },
            animation: {
                duration: 5000, // Durée de l'animation en millisecondes (2 secondes dans cet exemple)
                easing: 'easeOutCubic' // Type d'animation (vous pouvez choisir un autre type si vous le souhaitez)
            }
        }
    });
});

// Créez le graphique avec Chart.js
document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('myServiceChart').getContext('2d');
    var myServiceChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: serviceTypes,
            datasets: [{
                label: 'Service Counts',
                backgroundColor: '#ccff66', // Couleur de fond
                borderColor: 'rgba(75, 192, 192, 1)', // Couleur de la bordure
                borderWidth: 1,
                data: countsService
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },animation: {
                duration: 10000, // Durée de l'animation en millisecondes (2 secondes dans cet exemple)
                easing: 'easeInQuad' // Type d'animation (vous pouvez choisir un autre type si vous le souhaitez)
            }
        }
    });
});
document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('myPieChart').getContext('2d');
    var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: attackTypes2,
            datasets: [{
                data: counts2,
                backgroundColor: ['#FF1493', '#00FA9A', '#FF69B4', '#20B2AA', '#FF4500'], 
                borderWidth: 1,

            }]
        },
        options: {
            title: {
                display: true,
                text: 'Répartition des types d\'attaques' 
            },
            animation: {
                duration: 10000, // Durée de l'animation en millisecondes (2 secondes dans cet exemple)
                easing: 'linear' // Type d'animation (vous pouvez choisir un autre type si vous le souhaitez)
            }
        }
    });
});

/*document.addEventListener('DOMContentLoaded', function () {
var ctx = document.getElementById('densityChart').getContext('2d');
var densityChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: Array.from({ length: duration_data.length() }, (_, i) => i + 1),
        datasets: [{
            label: 'Density of Duration',
            lineTension: 0.3,
            backgroundColor: 'rgba(2,117,216,0.2)',
            borderColor: 'rgba(2,117,216,1)',
            data: duration_data,
        }],
    },
    options: {
        scales: {
            x: {
                grid: {
                    display: false
                },
            },
            y: {
                grid: {
                    color: 'rgba(0, 0, 0, .125)',
                },
            },
        },
        legend: {
            display: false
        }
    }
});
});*/


