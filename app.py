from flask import Flask, render_template ,jsonify

app = Flask(__name__)


@app.route('/')
def hello_yash():
  return render_template('home.html')

# return dynamic data using an API
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ =='__main__':
  app.run('0.0.0.0',debug=True)