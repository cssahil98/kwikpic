from fer import FER  #import library
import matplotlib.pyplot as plt  

img = plt.imread("img.jpg")  # read image
detector = FER(mtcnn=True)  # mtcnn = multicascade covolution network
emotion, score = detector.top_emotion(img)   # detecting emotion and its result
print(emotion,score) 
