
# 🎉 QR Code Generator & Scanner API

A simple FastAPI project to **generate** and **scan** QR codes. You can even **customize the color** of the generated QR codes!

## 🚀 Features
- Generate custom-colored QR codes from any text or URL.
- Scan and decode QR codes from image files.

## 🛠️ Quick Start

1. **Clone and Install**:
    ```bash
    git clone https://github.com/emmanuel1-byte/qr-code-generator-and-scanner-api.git
    cd "qr-code-generator-and-scanner-api"
    pip install -r requirements.txt
    ```

2. **Run the Server**:
    ```bash
    uvicorn main:app --reload
    ```

## 🔑 API Endpoints

### 1. **Generate a QR Code**
   - **POST** `/generate-qrcode`
   - **Request**:
     ```json
     {
       "data": "https://example.com",
       "background_color":"yellow",  // Optional (Default: white)
       "fill_color":"green",  // Optional (Default: black)
     }
     ```
   - **Response**: Streams a PNG image of the QR code.

### 2. **Scan a QR Code**
   - **POST** `/scan-qr`
   - Send an image file and get the decoded data.
