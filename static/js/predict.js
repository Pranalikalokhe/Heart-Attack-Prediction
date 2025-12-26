// HeartCare AI - Prediction Page JavaScript

document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('predictionForm');
    const resultsPanel = document.getElementById('resultsPanel');
    const loadingOverlay = document.getElementById('loadingOverlay');
    const closeResults = document.getElementById('closeResults');
    const newAssessment = document.getElementById('newAssessment');

    // Form submission
    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        // Collect form data
        const formData = {
            age: document.getElementById('age').value,
            sex: document.getElementById('sex').value,
            cp: document.getElementById('cp').value,
            trtbps: document.getElementById('trtbps').value,
            chol: document.getElementById('chol').value,
            fbs: document.getElementById('fbs').value,
            restecg: document.getElementById('restecg').value,
            thalachh: document.getElementById('thalachh').value,
            exng: document.getElementById('exng').value,
            oldpeak: document.getElementById('oldpeak').value,
            slp: document.getElementById('slp').value,
            caa: document.getElementById('caa').value,
            thall: document.getElementById('thall').value
        };

        // Show loading overlay
        loadingOverlay.style.display = 'flex';

        try {
            // Make API call
            const response = await fetch('/api/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            if (!response.ok) {
                throw new Error('Prediction failed');
            }

            const result = await response.json();

            // Hide loading, show results
            loadingOverlay.style.display = 'none';
            displayResults(result);

        } catch (error) {
            loadingOverlay.style.display = 'none';
            alert('Error making prediction. Please try again.');
            console.error('Error:', error);
        }
    });

    // Display results
    function displayResults(result) {
        // Update risk gauge
        const riskValue = document.getElementById('riskValue');
        const riskLabel = document.getElementById('riskLabel');
        const riskGauge = document.getElementById('riskGauge');

        riskValue.textContent = result.risk_probability.toFixed(1) + '%';
        riskLabel.textContent = result.risk_category;

        // Update gauge color based on risk
        if (result.risk_category === 'Low Risk') {
            riskGauge.style.background = 'linear-gradient(135deg, #10b981 0%, #059669 100%)';
        } else if (result.risk_category === 'Medium Risk') {
            riskGauge.style.background = 'linear-gradient(135deg, #f59e0b 0%, #d97706 100%)';
        } else {
            riskGauge.style.background = 'linear-gradient(135deg, #ef4444 0%, #dc2626 100%)';
        }

        // Update explanation
        document.getElementById('riskExplanation').textContent = result.explanation;

        // Display risk factors
        const riskFactorsContainer = document.getElementById('riskFactors');
        riskFactorsContainer.innerHTML = '';

        if (result.risk_factors && result.risk_factors.length > 0) {
            result.risk_factors.forEach(factor => {
                const factorDiv = document.createElement('div');
                factorDiv.className = 'risk-factor-item';
                factorDiv.innerHTML = `
                    <strong>${factor.factor}</strong>: ${factor.description}
                    <br><small>Severity: <span class="risk-badge ${factor.severity.toLowerCase()}">${factor.severity}</span></small>
                `;
                riskFactorsContainer.appendChild(factorDiv);
            });
        } else {
            riskFactorsContainer.innerHTML = '<p>No significant risk factors identified.</p>';
        }

        // Generate recommendations
        const recommendations = generateRecommendations(result);
        const recommendationsContainer = document.getElementById('recommendations');
        recommendationsContainer.innerHTML = '';

        recommendations.forEach(rec => {
            const li = document.createElement('li');
            li.textContent = rec;
            recommendationsContainer.appendChild(li);
        });

        // Show results panel
        resultsPanel.style.display = 'block';
        resultsPanel.scrollIntoView({ behavior: 'smooth' });
    }

    // Generate recommendations based on risk level
    function generateRecommendations(result) {
        const recommendations = [];

        if (result.risk_category === 'High Risk') {
            recommendations.push('Immediate medical consultation is strongly recommended');
            recommendations.push('Comprehensive cardiac evaluation should be scheduled');
            recommendations.push('Consider stress test and advanced cardiac imaging');
            recommendations.push('Discuss preventive medication options with your doctor');
            recommendations.push('Implement strict lifestyle modifications immediately');
        } else if (result.risk_category === 'Medium Risk') {
            recommendations.push('Schedule a medical consultation for cardiac assessment');
            recommendations.push('Regular monitoring of blood pressure and cholesterol');
            recommendations.push('Adopt heart-healthy diet and exercise routine');
            recommendations.push('Consider stress management techniques');
            recommendations.push('Follow up with healthcare provider within 3-6 months');
        } else {
            recommendations.push('Maintain current healthy lifestyle practices');
            recommendations.push('Continue regular health check-ups');
            recommendations.push('Stay physically active with regular exercise');
            recommendations.push('Maintain healthy diet and weight');
            recommendations.push('Annual cardiac health screening recommended');
        }

        return recommendations;
    }

    // Close results
    closeResults.addEventListener('click', function () {
        resultsPanel.style.display = 'none';
    });

    // New assessment
    newAssessment.addEventListener('click', function () {
        resultsPanel.style.display = 'none';
        form.reset();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Form reset
    form.addEventListener('reset', function () {
        resultsPanel.style.display = 'none';
    });
});
