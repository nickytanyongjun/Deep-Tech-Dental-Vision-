document.getElementById('imageInput').onchange = function (evt) {
    const [file] = this.files;
    if (file) {
        const preview = document.getElementById('imagePreview');
        preview.src = URL.createObjectURL(file);
        document.getElementById('imagePreviewContainer').classList.remove('d-none');
    }
};

document.getElementById('analyzeBtn').onclick = async function() {
    const fileInput = document.getElementById('imageInput');
    const resultArea = document.getElementById('resultArea');
    const loader = document.getElementById('loader');

    if (fileInput.files.length === 0) {
        alert("Please select an image first!");
        return;
    }

    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    // UI Updates
    resultArea.innerHTML = "";
    loader.classList.remove('d-none');
    this.disabled = true;

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        
        if (data.result) {
            // Using a simple regex to replace markdown with basic HTML tags for display
            resultArea.innerHTML = data.result.replace(/\n/g, "<br>");
        } else {
            resultArea.innerHTML = `<span class="text-danger">Error: ${data.error}</span>`;
        }
    } catch (err) {
        resultArea.innerHTML = `<span class="text-danger">Network Error: ${err}</span>`;
    } finally {
        loader.classList.add('d-none');
        this.disabled = false;
    }
};