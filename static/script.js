function input_change(evt) {
    let result = document.getElementById('result');
    result.innerHTML = '<div id="spinner"><div></div><div></div><div></div><div></div></div>';

    let seq = evt.target.value
                        .trim()
                        .replace(/\s+/g, ':');

    fetch('/graph/' + seq)
        .then(r => r.text())
        .then(t => result.innerHTML = t)
        .catch(err => console.error(err));
}

document.getElementById('seq').addEventListener('input', input_change);
