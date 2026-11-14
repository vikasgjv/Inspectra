const imageInput = document.getElementById("imageInput");
const categorySelect = document.getElementById("category");
const inspectButton = document.getElementById("inspectButton");

const loading = document.getElementById("loading");
const results = document.getElementById("results");

const resultCategory = document.getElementById("resultCategory");
const prediction = document.getElementById("prediction");
const anomalyScore = document.getElementById("anomalyScore");
const threshold = document.getElementById("threshold");
const processingTime = document.getElementById("processingTime");

const originalImage = document.getElementById("originalImage");
const heatmapImage = document.getElementById("heatmapImage");
const overlayImage = document.getElementById("overlayImage");


 
// Show selected file name
 

imageInput.addEventListener("change", () => {

    if (imageInput.files.length > 0) {

        const file = imageInput.files[0];

        console.log("Selected image:", file.name);

        const fileNameElement = document.getElementById("fileName");

        if (fileNameElement) {
            fileNameElement.textContent = file.name;
        }
    }
});


 
// Inspect Image
 

inspectButton.addEventListener("click", async (event) => {

    // Prevent any default browser action
    event.preventDefault();
    event.stopPropagation();

    console.log("Inspect button clicked");

    const imageFile = imageInput.files[0];
    const category = categorySelect.value;

    // Check image
    if (!imageFile) {
        alert("Please select an image.");
        return;
    }

    console.log("Image:", imageFile.name);
    console.log("Category:", category);


 
    // Prepare request
 

    const formData = new FormData();

    formData.append("image", imageFile);
    formData.append("category", category);


    // Show loading
    loading.classList.remove("hidden");
    results.classList.add("hidden");

    inspectButton.disabled = true;


    try {

        console.log("Sending image to FastAPI...");


 
        // Send request to FastAPI
 

        const response = await fetch(
            "/predict",
            {
                method: "POST",
                body: formData
            }
        );


        console.log("FastAPI response:", response.status);


        if (!response.ok) {

            const errorText = await response.text();

            throw new Error(
                `Server error ${response.status}: ${errorText}`
            );
        }


       
        // Read API response
   

        const data = await response.json();

        console.log("Prediction result:", data);


 
        // Display result information
 

        resultCategory.textContent = data.category;

        prediction.textContent = data.prediction;

        anomalyScore.textContent =
            Number(data.anomaly_score).toFixed(4);

        threshold.textContent =
            Number(data.threshold).toFixed(4);

        processingTime.textContent =
            Number(data.processing_time).toFixed(2) + " seconds";


 
// Display original image
originalImage.src = URL.createObjectURL(imageFile);

// Display anomaly heatmap
heatmapImage.src = data.heatmap_url;

// Display heatmap overlay
overlayImage.src = data.overlay_url;

        if (data.heatmap_url) {
            heatmapImage.src = data.heatmap_url;
        } else {
            console.error("Heatmap URL is missing from API response");
        }


     
        // Show results
 

        results.classList.remove("hidden");

        console.log("RESULTS ARE NOW VISIBLE");


    } catch (error) {

        console.error("Prediction error:", error);

        alert(
            "Something went wrong while analyzing the image.\n\n" +
            error.message
        );


    } finally {

        // Hide loading
        loading.classList.add("hidden");

        // Enable button again
        inspectButton.disabled = false;

    }

});