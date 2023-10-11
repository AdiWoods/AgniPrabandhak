# tensorflow daata
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import numpy as np
from django.core.files.uploadedfile import InMemoryUploadedFile
from reportedfire.models import ForestDepartmentData,ReportData


# for the message
from twilio.rest import Client
from reportedfire import keys
client=Client(keys.account_sid,keys.auth_token)





def validationandmessage(image,lat,lon):
    CLASSES=['fire','no_fire']
    model=load_model("/Users/khumapokharel/Desktop/Hackathon/backendforreport/fire_report/firereport/deeplearningmodel/moddel1.h5")
    pil_image = Image.open(image)
    desired_size = (224, 224)
    resized_image = pil_image.resize(desired_size)
    
    image_array = np.array(resized_image)
    normalized_image = image_array / 255.0
    expanded_image=np.expand_dims(normalized_image,axis=0)
    
    
    
    prediction=model.predict(expanded_image)
    
    prediction=CLASSES[int(prediction[0])]
    
    if prediction==CLASSES[0]:
        if  ForestDepartmentData.objects.filter(longitude=lon,lattitude=lat).exists() or ForestDepartmentData.objects.filter(longitude=lon+1,lattitude=lat+1):
            obj=ForestDepartmentData.objects.get(lattitude=lat,longitude=lon)
            phone_no=obj.phone_no
            print("pHone no ",phone_no)
            messagetodepartment(phone_no)
            
            
        else:
            pass
           
           
            
            
            

       
    
           
           
        
        # call the messagetodeapartment function
        
        
        
        
        return "fire"

    
    
    else:
        return "nofire"
    
   
    
    
    
    
    



# message to he forest department
def messagetodepartment(phoneno):
    message=client.messages.create(
    body=keys.notification_message,
    from_=keys.twilio_number,
    to=keys.target_number
    
)
    
    
    
   
    