import pickle

lr=pickle.load(open("models/Crop_classification_model.pkl","rb"))
ssc=pickle.load(open("models/Crop_Standard_Scalar.pkl","rb"))