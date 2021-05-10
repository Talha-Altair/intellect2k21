from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/about') 
def hello_world():
    return render_template('about.html')


@app.route('/secret',methods=["POST","GET"])
def hello_world1():
    return render_template('secret.html')    

"""

http://0.0.0.0:8080/api/saponihimym

"""

@app.route('/api/saponihimym',methods=["POST","GET"])    
def hello_world2():
    key = request.values.get("secret")
    print(key)
    if (key=='pass'):
        return 'Access Granted'
    return 'Authentication Failed'    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)