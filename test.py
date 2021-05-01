import pickle
import joblib
import json
import numpy as np

Iris_model= pickle.load(open('Iris_model.pickle', 'rb'))


def predict_species(SepalLengthCm,SepalWidthCm,PetalLengthCm, PetalWidthCm):
    x = np.zeros(4)
    x[0] = SepalLengthCm
    x[1] = SepalWidthCm
    x[2] = PetalLengthCm
    x[3] = PetalWidthCm
    species= Iris_model.predict([x])[0]
    return species

if __name__=='__main__':
    Species= predict_species(5.1,3.5,1.4,0.2)
    print('Predicted species is', Species)