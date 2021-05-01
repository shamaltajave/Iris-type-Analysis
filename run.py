from flask import Flask, request, jsonify
import Iris_db
import test
app = Flask(__name__)

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data = request.form
        response = Iris_db.registeration(data)
    return jsonify({'msg':response})

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data = request.form
        response = Iris_db.login(data)
    return jsonify({'msg':response})

@app.route('/predict_species', methods=['GET', 'POST'])    
def prediction():
    data=request.form
    if request.method=='POST':
        SepalLengthCm = float(data['SepalLengthCm'])
        SepalWidthCm  = float(data['SepalWidthCm'])
        PetalLengthCm = float(data['PetalLengthCm'])
        PetalWidthCm  = float(data['PetalWidthCm'])
        print('SepalLengthCm,SepalWidthCm,PetalLengthCm, PetalWidthCm', SepalLengthCm,SepalWidthCm,PetalLengthCm, PetalWidthCm)
        species= test.predict_species(SepalLengthCm,SepalWidthCm,PetalLengthCm, PetalWidthCm)
    return 'Predicted Species is {}' .format(species)

if __name__ == "__main__":
    print("Starting Python Flask Server For Iris Species Prediction...")
    app.run(host='0.0.0.0', port='5004')