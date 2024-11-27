document.getElementById("qr-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const qrData = document.getElementById("qr-data").value;
    const qrCodeImage = document.getElementById("qr-code");

    try {
        const response = await fetch("/generate_qr", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ data: qrData }),
        });

        if (response.ok) {
            const blob = await response.blob();
            const url = URL.createObjectURL(blob);

            qrCodeImage.src = url;
            qrCodeImage.style.display = "block";
        } else {
            alert("Failed to generate QR Code. Try again.");
        }
    } catch (error) {
        console.error("Error generating QR Code:", error);
        alert("An error occurred. Please check your connection.");
    }
});