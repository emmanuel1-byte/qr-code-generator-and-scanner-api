from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from qr_code_helper import qr_code_generator_helper, qr_code_reader_helper
from schema import QrCode

app = FastAPI()

# #Cors configuration
app.add_middleware(
CORSMiddleware, allow_origins=["*"],  allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def base_url():
    return { "message":"App is helathy and running 🎉.."}

@app.post("/generate-qrcode")
def generate_qrcode(data: QrCode):
    qr_code = qr_code_generator_helper(data)
    if qr_code:
        headers = {"Content-Disposition": "attachement; filename=qrcode.png"}
        return StreamingResponse(qr_code, media_type="image/png", headers=headers)
    else:
         raise HTTPException(status_code=500, detail="Failed to generated Qr code")
    
    
@app.post("/scan-qr")
async def read_qrcode(file: UploadFile):
    qr_code = qr_code_reader_helper(file)
    if qr_code:
      return { "data": qr_code}
    else:
        raise HTTPException(status_code=500, detail="Failed to read QR code")