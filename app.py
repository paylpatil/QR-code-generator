from flask import Flask, render_template, request, send_file 
import qrcode
import io

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_qr", methods=["POST"])
def generate_qr():
    data = request.json.get("data")
    if not data:
        return {"error": "No data provided"}, 400

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)