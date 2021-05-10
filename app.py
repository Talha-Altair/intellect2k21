from flask import Flask, render_template #Imports Flask Module
app = Flask(__name__)

@app.route('/about') #Defining Root Node
def hello_world():
    return render_template('about.html')


@app.route('/') #Second Node
def hello_world1():
    return 'You are in 3nd Node'    

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True) #Port is Set to 8080 and Host is set to Global