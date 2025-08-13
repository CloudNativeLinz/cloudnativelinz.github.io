function generateRandomNumbers() {
    const resultCard = document.getElementById('result-card');
    const resultHeader = document.getElementById('result-header');
    const resultContainer = document.getElementById('result');
    
    // Clear previous results
    resultHeader.innerText = '';
    resultContainer.innerHTML = '';
    resultCard.style.display = 'none';

    const min = parseInt(document.getElementById('min').value, 10);
    const max = parseInt(document.getElementById('max').value, 10);
    const spins = parseInt(document.getElementById('spins').value, 10);

    if (
        isNaN(min) || min < 0 ||
        isNaN(max) || max < min ||
        isNaN(spins) || spins <= 0 || spins > max - min + 1
    ) {
        resultHeader.innerText = '❌ Invalid input';
        resultHeader.style.color = '#dc2626';
        resultContainer.innerHTML = '<p style="text-align: center; color: #6b7280;">Please check your input values. Make sure minimum < maximum and number of results ≤ range size.</p>';
        resultCard.style.display = 'block';
        resultCard.style.border = '2px solid #ef4444';
        resultCard.style.background = 'linear-gradient(135deg, #fef2f2 0%, #fef7f7 100%)';
        return;
    }

    const generatedNumbers = new Set();
    while (generatedNumbers.size < spins) {
        const randomNumber = Math.floor(Math.random() * (max - min + 1)) + min;
        generatedNumbers.add(randomNumber);
    }

    // Show success results
    resultHeader.innerText = '🎉 Your lucky numbers are:';
    resultHeader.style.color = '#065f46';
    
    const numbersArray = Array.from(generatedNumbers).sort((a, b) => a - b);
    const numbersHTML = numbersArray.map(num => 
        `<span class="result-number">${num}</span>`
    ).join('');
    
    resultContainer.innerHTML = numbersHTML;
    resultCard.style.border = '2px solid #10b981';
    resultCard.style.background = 'linear-gradient(135deg, #ecfdf5 0%, #f0fdf4 100%)';
    resultCard.style.display = 'block';
    
    // Smooth scroll to results
    setTimeout(() => {
        resultCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }, 100);
}
