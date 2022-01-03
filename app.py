from flask import Flask,jsonify,request
from model import getPrediction
app = Flask(__name__)

@app.route("/digit_predict",methods = ["POST"])
def getPredict():
    image = request.files.get("digit")
    predict = getPrediction(image)
    return jsonify ({'data':predict , "message":"the digit is sucessfully recognized"})

if __name__ == '__main__':
    app.run(debug = True)