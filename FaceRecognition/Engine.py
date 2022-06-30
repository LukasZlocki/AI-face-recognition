# Recognizing face of model in set of examples
# using cv2 and face_recognition libraries


import cv2
import face_recognition

# Models set - models to compare with data set
model_set = ["BronislawK.png", "DonaldT.png", "JaroslawK.png", "TadeuszM.png"]
model_set_path = "Pics/LearningSet/"

# Examples set
data_set = ["pic1.png", "pic2.png", "pic3.png", "pic4.png", "pic5.png", "pic6.png", "pic7.png", "pic8.png", "pic9.png", "pic10.png"]
data_set_path = "Pics/"

def compare_photos(model, example):
    result = face_recognition.compare_faces([model], example)
    return result

def show_images(model_image, example_image):
        cv2.imshow("Model Photo", model_image)
        cv2.imshow("Example Photo", example_image)

i = 0
for model in model_set:
    img_model = cv2.imread(model_set_path + model_set[i])
    rgb_img_model = cv2.cvtColor(img_model , cv2.COLOR_BGR2RGB)
    img_model_encoded = face_recognition.face_encodings(rgb_img_model)[0]
    
    j = 0
    for example in data_set:
        img_example = cv2.imread(data_set_path + data_set[j])
        rgb_img_example = cv2.cvtColor(img_example, cv2.COLOR_BGR2RGB)
        img_example_encoded = face_recognition.face_encodings(rgb_img_example)[0]
        show_images(img_model, img_example )
        print("Result: ", compare_photos(img_model_encoded, img_example_encoded))
        cv2.waitKey(0) 
        j = j +1

    i = i + 1



