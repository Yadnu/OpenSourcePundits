import cv2
import os
from PIL import Image
import numpy as np
#import face_recognition

def imageTrainer():
    dataset_path = 'FaceRecognitionRpi/dataset'
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("FaceRecognitionRpi/haarcascade_frontalface_default.xml")

    ## Get Image's Label Data and the Image
    def getImgLabel(dataset_path):
        imgpaths = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path)]
        face_samples = []
        ids = []
        for imgpath in imgpaths:
            pil_img = Image.open(imgpath).convert('L')  # Converting it into Grayscale
            np_img = np.array(pil_img, 'uint8')
            id = int(os.path.split(imgpath)[-1].split(".")[1])
            print(id)
            faces = detector.detectMultiScale(np_img)
            print(faces)
            for x, y, w, h in faces:
                face_samples.append(np_img[y:y + h, x:x + w])
                ids.append(id)
        return face_samples, ids

    print("\n Training Faces Be Patient")

    faces, ids = getImgLabel(dataset_path)
    recognizer.train(faces, np.array(ids))

    ## Saving the Trainer Model trainer.yml file
    recognizer.write('FaceRecognitionRpi/trainer/trainer.yml')

    ## Printing the Number of Faces trained with Program
    print("{0} Faces Trained. Exiting Program".format(len(np.unique(ids))))


# if __name__ == '__main__':
#     print("Intializing Face Trainer Program ...")
#     imageTrainer()
