import io
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def qr_code_generator_helper(data):
    try:
        qr = qrcode.QRCode() #Create a new Instance of the QRCode class
    
        qr.add_data(data.content)  #Pass in the content for the QR code
        qr.make(fit=True)
    
        img = qr.make_image(fill_color=data.fill_color, back_color=data.background_color) #Generate the Image
    
        #save Image in memory
        img_io = io.BytesIO()
        img.save(img_io,"PNG")
        img_io.seek(0)
        
        return img_io
    except Exception as e:
        print(f"Error generating QR code: {e}")
        return None
  
  
def qr_code_reader_helper(file):
  try:
      image_data = file.file.read()
      image = Image.open(io.BytesIO(image_data))
      
      #decode qr code
      decoded_objects = decode(image)
      
      if decoded_objects:
          qr_code_data = decoded_objects[0].data.decode("utf-8")
          return qr_code_data
      else: 
          return None
  except Exception as e:
      print(f"Error Reading QR code: {e}")
      return None