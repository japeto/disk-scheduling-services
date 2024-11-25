async function fetchAvailableFiles() {
    try {
        const response = await fetch('http://127.0.0.1:8000/inputs');
        if (response.ok) {
            const data = await response.json();
            const select = document.getElementById('serverFile');
            select.innerHTML = ''; // Limpia el contenido previo
            data.files.forEach(file => {
                const option = document.createElement('option');
                option.value = file;
                option.textContent = file;
                select.appendChild(option);
            });
        } else {
            console.error('Error fetching files from server:', response.statusText);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

async function loadServerFile() {
    const filename = document.getElementById('serverFile').value;

    try {
        const response = await fetch(`http://127.0.0.1:8000/inputs/${filename}`);
        if (response.ok) {
            const { content } = await response.json();
            const jsonData = parseTxtToJSON(content.split('\n'));

            // Actualiza los campos del formulario
            updateFormFields(jsonData);

            document.getElementById('result').innerHTML = `<p>File ${filename} loaded successfully.</p>`;
        } else {
            document.getElementById('result').innerHTML = '<p>Error fetching file from server.</p>';
        }
    } catch (error) {
        document.getElementById('result').innerHTML = `<p>Error: ${error.message}</p>`;
    }
}

function loadLocalFile() {
    const fileInput = document.getElementById('localFile');
    const file = fileInput.files[0];
    if (!file) {
        alert('Please select a file to load.');
        return;
    }

    const reader = new FileReader();
    reader.onload = function (event) {
        const content = event.target.result;
        const jsonData = parseTxtToJSON(content.split('\n'));

        // Actualiza los campos del formulario
        updateFormFields(jsonData);

        document.getElementById('result').innerHTML = `<p>Local file loaded successfully.</p>`;
    };

    reader.readAsText(file);
}

function parseTxtToJSON(lines) {
    const payload = {};
    let lineIndex = 0;

    lines.forEach(line => {
        line = line.trim();
        if (line.startsWith('#') || line === '') return; // Ignorar comentarios y líneas vacías

        if (lineIndex === 0) payload.algorithm = parseInt(line);
        else if (lineIndex === 1) payload.tracks = parseInt(line);
        else if (lineIndex === 2) payload.ioresquest = parseInt(line);
        else if (lineIndex === 3) payload.arm = parseInt(line);
        else if (lineIndex === 4) payload.requests = line.split(',').map(Number);

        lineIndex++;
    });

    return payload;
}

function updateFormFields(jsonData) {
    document.getElementById('algorithm').value = jsonData.algorithm || '';
    document.getElementById('tracks').value = jsonData.tracks || '';
    document.getElementById('iorequest').value = jsonData.ioresquest || '';
    document.getElementById('arm').value = jsonData.arm || '';
    document.getElementById('requests').value = jsonData.requests ? jsonData.requests.map(String).join(',') : '';
}

async function sendRequest() {
    const algorithm = parseInt(document.getElementById('algorithm').value);
    const tracks = parseInt(document.getElementById('tracks').value);
    const iorequest = parseInt(document.getElementById('iorequest').value);
    const arm = parseInt(document.getElementById('arm').value);
    const requests = document.getElementById('requests').value
        .split(',')
        .map(Number)
        .filter(n => !isNaN(n));

    const payload = {
        algorithm: algorithm,
        tracks: tracks,
        iorequest: iorequest,
        arm: arm,
        requests: requests
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/sched', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            const { result } = await response.json();
            document.getElementById('result').innerHTML = `
                <p><b>Sequence:</b> ${result.sequence.join(", ")}<br/>
                <b>Distance:</b> ${result.distance}<br/>
                <b>Average:</b> ${result.average}</p>
            `;
        } else {
            const errorData = await response.json();
            document.getElementById('result').innerHTML = `<p>Error: ${errorData.error || response.statusText}</p>`;
        }
    } catch (error) {
        document.getElementById('result').innerHTML = `<p>Error: ${error.message}</p>`;
    }
}

// Cargar la lista de archivos disponibles al cargar la página
document.addEventListener('DOMContentLoaded', fetchAvailableFiles);
