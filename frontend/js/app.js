async function uploadResume() {

    const fileInput =
        document.getElementById("resumeFile");

    const file = fileInput.files[0];

    if (!file) {

        alert("Please select a file");

        return;
    }

    const formData = new FormData();

    formData.append("file", file);

    const response = await fetch(
        "http://127.0.0.1:8000/resume/upload",
        {
            method: "POST",
            body: formData
        }
    );

    const data = await response.json();

    displayResult(data);
}

function displayResult(data) {
    const resultDiv = document.getElementById("result");

    resultDiv.innerHTML = `
        <div class="result-header">
            <h2>Analysis Summary</h2>
        </div>
        
        <div class="result-item">
            <label>Filename</label>
            <p>${data.filename}</p>
        </div>

        <div class="result-item">
            <label>ATS Compatibility Score</label>
            <div class="ats-score">${data.ats_analysis.ats_score}%</div>
        </div>

        <div class="result-item">
            <label>Identified Skills</label>
            <p>${data.skills_detected.join(", ")}</p>
        </div>

        <div class="result-item">
            <label>Recommendations / Missing Skills</label>
            <p>${data.ats_analysis.missing_skills.length > 0 ? data.ats_analysis.missing_skills.join(", ") : "None - Great profile!"}</p>
        </div>
    `;
}

async function loadCandidates() {

    const response = await fetch(
        "http://127.0.0.1:8000/recruiter/candidates"
    );

    const result = await response.json();
    const candidateList = document.getElementById("candidateList");

    candidateList.innerHTML = "";

    // Access the list inside the 'data' property of the response
    if (result.data) {
        result.data.forEach(candidate => {
            candidateList.innerHTML += `
                <div class="candidate-card">
                    <h3>${candidate.filename}</h3>
                    <p><strong>Skills:</strong> ${candidate.skills}</p>
                    <p><strong>ATS Score:</strong> ${candidate.ats_score}</p>
                    <p><a href="${candidate.file_url}" target="_blank">View Resume</a></p>
                </div>
            `;
        });
    }
}