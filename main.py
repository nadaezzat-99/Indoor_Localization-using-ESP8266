from cProfile import label
from flask import Flask , request
from flask_cors import CORS
from flask import jsonify
from joblib import  load
# from classifier.prediction import prediction
# Create flask & cors instance 
app = Flask(__name__)
cors = CORS()

cors.init_app(app)

#Load Random forest classifier 
clf = load('model2.joblib')

locations=[]

# Serve ESP 8266 Get request with RSSI(received signal strength indicator).
@app.route('/data', methods=['GET'])
def home():      
  #Get query parameters 
  args = request.args
  data = args.to_dict()
   
  place = clf.predict([[data.get('STUDBME1'),data.get('STUDBME2'),data.get('STUDBME3'),data.get('RehabLab'),data.get('CMP_LAB1'),data.get('CMP_LAB2'),data.get('CMP_LAB3'),data.get('CMP_LAB4'),data.get('Mikasa'),data.get('Nada'),data.get('Mariem'),data.get('Alaa'), data.get('C_H_S_4'), data.get('tarek')]])   
  print(place[0])

  locations.append(label[0])
  # print(label)

  print('location: ', locations[0])
  return jsonify(place[0])
  # return jsonify(data.get('STUDBME1'))
    
# Serve Get Request from React Server 
@app.route("/mapping", methods=['GET'])
def show_mapping():
  #Respone with the location chip exist in 
    return jsonify(label=locations[-1])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 8090,debug=True)
    	
