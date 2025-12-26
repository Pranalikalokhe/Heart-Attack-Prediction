// HeartCare AI - Dashboard JavaScript

document.addEventListener('DOMContentLoaded', async function () {
    // Load statistics
    await loadStatistics();

    // Initialize charts
    initializeCharts();
});

async function loadStatistics() {
    try {
        const response = await fetch('/api/statistics');
        const stats = await response.json();

        // Update stat cards
        document.getElementById('totalPredictions').textContent = stats.total_predictions.toLocaleString();
        document.getElementById('highRiskCount').textContent = stats.high_risk_count.toLocaleString();
        document.getElementById('mediumRiskCount').textContent = stats.medium_risk_count.toLocaleString();
        document.getElementById('lowRiskCount').textContent = stats.low_risk_count.toLocaleString();

    } catch (error) {
        console.error('Error loading statistics:', error);
    }
}

async function initializeCharts() {
    // Get feature importance data
    let featureImportance = {};
    try {
        const response = await fetch('/api/feature-importance');
        featureImportance = await response.json();
    } catch (error) {
        console.error('Error loading feature importance:', error);
        // Use default values
        featureImportance = {
            'cp': 0.25,
            'thalachh': 0.18,
            'oldpeak': 0.15,
            'caa': 0.12,
            'age': 0.10,
            'sex': 0.08,
            'trtbps': 0.06,
            'chol': 0.06
        };
    }

    // Risk Distribution Chart
    const riskDistCtx = document.getElementById('riskDistributionChart').getContext('2d');
    new Chart(riskDistCtx, {
        type: 'doughnut',
        data: {
            labels: ['Low Risk', 'Medium Risk', 'High Risk'],
            datasets: [{
                data: [437, 498, 312],
                backgroundColor: [
                    '#10b981',
                    '#f59e0b',
                    '#ef4444'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 20,
                        font: {
                            size: 12,
                            family: 'Inter'
                        }
                    }
                }
            }
        }
    });

    // Feature Importance Chart
    const featureNames = {
        'cp': 'Chest Pain Type',
        'thalachh': 'Max Heart Rate',
        'oldpeak': 'ST Depression',
        'caa': 'Major Vessels',
        'age': 'Age',
        'sex': 'Gender',
        'trtbps': 'Blood Pressure',
        'chol': 'Cholesterol'
    };

    const featureLabels = Object.keys(featureImportance).map(key => featureNames[key] || key);
    const featureValues = Object.values(featureImportance).map(v => v * 100);

    const featureCtx = document.getElementById('featureImportanceChart').getContext('2d');
    new Chart(featureCtx, {
        type: 'bar',
        data: {
            labels: featureLabels,
            datasets: [{
                label: 'Importance (%)',
                data: featureValues,
                backgroundColor: [
                    '#667eea',
                    '#764ba2',
                    '#f093fb',
                    '#f5576c',
                    '#4facfe',
                    '#00f2fe',
                    '#43e97b',
                    '#38f9d7'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            indexAxis: 'y',
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    max: 30,
                    ticks: {
                        callback: function (value) {
                            return value + '%';
                        }
                    }
                }
            }
        }
    });

    // Age Distribution Chart
    const ageCtx = document.getElementById('ageDistributionChart').getContext('2d');
    new Chart(ageCtx, {
        type: 'line',
        data: {
            labels: ['29-35', '36-42', '43-49', '50-56', '57-63', '64-70', '71-77'],
            datasets: [{
                label: 'Number of Patients',
                data: [28, 45, 62, 78, 54, 28, 7],
                borderColor: '#667eea',
                backgroundColor: 'rgba(102, 126, 234, 0.1)',
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Gender Distribution Chart
    const genderCtx = document.getElementById('genderDistributionChart').getContext('2d');
    new Chart(genderCtx, {
        type: 'pie',
        data: {
            labels: ['Male', 'Female'],
            datasets: [{
                data: [68.3, 31.7],
                backgroundColor: [
                    '#3b82f6',
                    '#ec4899'
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 20,
                        font: {
                            size: 12,
                            family: 'Inter'
                        }
                    }
                }
            }
        }
    });

    // Cholesterol Levels Chart
    const cholesterolCtx = document.getElementById('cholesterolChart').getContext('2d');
    new Chart(cholesterolCtx, {
        type: 'bar',
        data: {
            labels: ['<200', '200-239', '240-279', '280+'],
            datasets: [{
                label: 'Patients',
                data: [245, 412, 358, 232],
                backgroundColor: '#16a34a',
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Blood Pressure Trends Chart
    const bloodPressureCtx = document.getElementById('bloodPressureChart').getContext('2d');
    new Chart(bloodPressureCtx, {
        type: 'line',
        data: {
            labels: ['<120', '120-129', '130-139', '140-159', '160+'],
            datasets: [{
                label: 'Patients',
                data: [156, 298, 387, 312, 94],
                borderColor: '#2563eb',
                backgroundColor: 'rgba(37, 99, 235, 0.1)',
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
