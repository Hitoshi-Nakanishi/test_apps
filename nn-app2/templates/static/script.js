const fileInput = document.getElementById('file-upload');
const canvas = document.getElementById('image-preview');
const predictionResult = document.getElementById('prediction-result');
const loadingSpinner = document.getElementById('loading-spinner');
const uploadForm = document.getElementById('upload-form');

const ctx = canvas.getContext('2d');

// Handle form submission
uploadForm.addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the form from submitting the traditional way
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(event) {
            const img = new Image();
            img.onload = function() {
                // Draw the uploaded image onto the canvas
                canvas.width = 28;
                canvas.height = 28;
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.drawImage(img, 0, 0, 28, 28);
                canvas.style.display = 'block';

                // Send image data for prediction
                getPrediction();
            };
            img.src = event.target.result;
        };
        reader.readAsDataURL(file);
    }
});

function getPrediction() {
    loadingSpinner.style.display = 'block';
    predictionResult.innerHTML = '';

    // Get image data from the canvas
    const imgData = ctx.getImageData(0, 0, 28, 28).data;
    let pixels = [];
    for (let i = 0; i < imgData.length; i += 4) {
        let grayscale = imgData[i] / 255; // Normalize to [0, 1]
        pixels.push(grayscale);
    }

    // Prepare image data for the server
    const data = JSON.stringify({ "image": [pixels] });

    // Send image data to the server using Fetch API
    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: data
    })
    .then(response => response.json())
    .then(result => {
        loadingSpinner.style.display = 'none';
        predictionResult.innerHTML = `Prediction: ${result.prediction}`;
    })
    .catch(err => {
        loadingSpinner.style.display = 'none';
        predictionResult.innerHTML = 'Error occurred';
    });
}
