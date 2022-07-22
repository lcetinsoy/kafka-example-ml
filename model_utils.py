import joblib

def load_model():

    return joblib.load('regression.joblib')


def predict(model, data):

    return model.predict(data)
