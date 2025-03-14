function generateRandomNumbers() {
    document.getElementById('result-header').innerText = '';
    document.getElementById('result').innerText = '';

    const min = parseInt(document.getElementById('min').value, 10);
    const max = parseInt(document.getElementById('max').value, 10);
    const spins = parseInt(document.getElementById('spins').value, 10);

    if (
        !min || isNaN(min) || min < 0 ||
        !max || isNaN(max) || max <= min ||
        !spins || isNaN(spins) || spins <= 0 || spins > max - min + 1
    ) {
        document.getElementById('result-header').innerText = 'Invalid input';
        return
    }


    const generatedNumbers = new Set();
    while (generatedNumbers.size < spins) {
        const randomNumber = Math.floor(Math.random() * (max - min + 1)) + min;
        generatedNumbers.add(randomNumber);
    }

    document.getElementById('result-header').innerText = 'Your lucky numbers are:';
    document.getElementById('result').innerText = Array.from(generatedNumbers).join(', ');
}
