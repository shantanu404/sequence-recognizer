function input_change(evt) {
    let result = document.getElementById('result');

    let seq = evt.target.value
                        .trim()
                        .replace(/\s+/g, ':');

    if (/^[01:]+$/.test(seq)) {
        fetch('/graph/' + seq)
            .then(r => r.text())
            .then(t => result.innerHTML = t)
            .catch(err => console.error(err));
    } else {
        result.innerHTML = '<h1>Enter binary sequences (anything other than 0 or 1 is considered invalid)<h1>';
    }
}

document.getElementById('seq').addEventListener('input', input_change);
