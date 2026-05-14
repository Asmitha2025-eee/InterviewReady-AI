async function submitData() {

    const technical =
        document.getElementById('technical').value;

    const communication =
        document.getElementById('communication').value;

    const projects =
        document.getElementById('projects').value;

    const certifications =
        document.getElementById('certifications').value;

    const response = await fetch(
        'http://127.0.0.1:5000/analyze',
        {
            method: 'POST',

            headers: {
                'Content-Type': 'application/json'
            },

            body: JSON.stringify({
                technical,
                communication,
                projects,
                certifications
            })
        }
    );

    const data = await response.json();

    document.getElementById('result').innerHTML = `
        <h2>Score: ${data.score}/100</h2>
        <h3>${data.level}</h3>
        <p>${data.suggestions.join('<br>')}</p>
    `;
}