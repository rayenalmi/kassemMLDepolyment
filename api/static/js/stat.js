document.addEventListener('DOMContentLoaded', function () {
    var ctx = document.getElementById('dosAttackChart').getContext('2d');
    var dos = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: attack_types,
            datasets: [{
                label: 'DOS Attack',
                backgroundColor: ['#66c2a5', '#fc8d62', '#8da0cb', '#e78ac3', '#a6d854', '#ffd92f', '#e5c494', '#b3b3b3', '#66c2a5', '#fc8d62'],
                borderColor: 'black',
                borderWidth: 1,
                data: attackCountsList
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            },
            animation: {
                duration: 2000, // Durée de l'animation en millisecondes (2 secondes dans cet exemple)
                easing: 'easeInOutQuart' // Type d'animation (vous pouvez choisir un autre type si vous le souhaitez)
            }
        }
    });
});

//////////////////////////////////////////////////////////////////////////////////////
document.addEventListener('DOMContentLoaded', function () {

    // Créer le Pie Chart 3D
    var ctx = document.getElementById('u2rPieChart').getContext('2d');
    var u2rPieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: attack_types_U2R,
            datasets: [{
                data: attack_counts_U2R_list,
                backgroundColor: ['#ffcc66', '#339966', '#cc99cc', '#ff6666', '#99ccff', '#ffd92f', '#e5c494'],
                borderWidth: 1
            }]
        },
        options: {
            title: {
                display: true,
                text: 'Répartition des attaques U2R'
            },
            plugins: {
                legend: {
                    position: 'right'
                },
                datalabels: {
                    color: 'white',
                    display: function (context) {
                        return context.dataset.data[context.dataIndex] > 0; // Afficher l'étiquette uniquement si la valeur est supérieure à zéro
                    },
                    font: {
                        weight: 'bold'
                    },
                    formatter: function (value, context) {
                        return context.chart.data.labels[context.dataIndex] + ': ' + value;
                    }
                }
            },
            animation: {
                animateRotate: false, // Désactiver l'animation de rotation pour un aspect plus 3D
                animateScale: true
            }
        }
    });
});
/////////////////////////////////////////////////////////////////////////
document.addEventListener('DOMContentLoaded', function () {
    // Couleurs prédéfinies
    var predefinedColors = ['#ffcc66', '#339966', '#cc99cc', '#ff6666', '#99ccff', '#ffd92f'];

    // Créer le Bar Chart avec animation
    var ctxBarProbe = document.getElementById('probeBarChart').getContext('2d');
    var probeBarChart = new Chart(ctxBarProbe, {
        type: 'bar',
        data: {
            labels: attack_types_Probe,
            datasets: [{
                label: 'Occurrences',
                data: attack_counts_Probe_list,
                backgroundColor: predefinedColors,
                borderWidth: 1,
                borderColor: '#000'
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            plugins: {
                legend: {
                    display: false
                },
                datalabels: {
                    anchor: 'end',
                    align: 'top',
                    color: function (context) {
                        return context.dataset.borderColor;
                    },
                    formatter: Math.round // Afficher les valeurs entières
                }
            },
            animation: {
                type: 'scale', // ou 'chartArea'
                duration: 2000,
                easing: 'easeInOutQuart'
            }
        }
    });
});
