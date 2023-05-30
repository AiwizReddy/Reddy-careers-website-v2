from flask import Flask,render_template,jsonify
app = Flask(__name__)
JOBS=[{"id":1,"jobprofile":"Data analyst","location":"Bengaluru,india","salary":"10,00,000"},{"id":2,"jobprofile":"Data scientist","location":"Delhi,india","salary":"15,00,000"},{"id":3,"jobprofile":"Data Engineer","location":"Remote,india","salary":"12,00,000"},{"id":4,"jobprofile":"Frontend Engineer","location":"Hydrabad,india","salary":"9,00,000"}]

@app.route("/")
def hello_reddy():
  return render_template ('home.html',jobs=JOBS)

@app.route("/api/json")
def list_jobs():
  jsonify(JOBS)
if __name__== "__main__" :
  app.run(host="0.0.0.0",debug=True)