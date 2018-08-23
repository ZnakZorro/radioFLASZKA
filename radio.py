import RPi.GPIO as GPIO
from flask import Flask, render_template
import datetime
import subprocess
app = Flask(__name__)

def formatuj(line,title):
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   result_success = line.replace("b'", "") 
   arr = result_success.split("\\n")
   ile = len(arr) 
   result1='';
   result2='';
   result3='';
   if ile>1: result1 = arr[0]
   if ile>2: result2 = arr[1]
   if ile>3: result3 = arr[2]
   templateData = {
      'title': title,
      'time':  timeString,
      'info':  result1,
      'info2': result2,
      'info3': result3
      }
   return templateData



@app.route("/")
def root():
   templateData = formatuj("Start \\nweb\\npage\\n???","START")
   return render_template('main.html', **templateData)



@app.route("/radio")
def radio():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   command = "mpc play"
   result_success = str(subprocess.check_output([command], shell=True))
   templateData = formatuj(result_success,'INFO')
   return render_template('main.html', **templateData)

@app.route("/current")
def current():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   command = "mpc current"
   result_success = str(subprocess.check_output([command], shell=True))
   templateData = formatuj(result_success,'Gramy')
   return render_template('main.html', **templateData)


@app.route('/radio/<int:radio_id>')
def show_post(radio_id):
   command = "mpc play "+str(radio_id)
   result_success = str(subprocess.check_output([command], shell=True))
   templateData = formatuj(result_success,'RADIO nr')
   return render_template('main.html', **templateData)

@app.route("/prev")
def prev():
   command = "mpc prev"
   result_success = str(subprocess.check_output([command], shell=True))
   templateData = formatuj(result_success,'prev')
   return render_template('main.html', **templateData)

@app.route("/next")
def next():
   command = "mpc next"
   result_success = str(subprocess.check_output([command], shell=True))
   templateData = formatuj(result_success,'next')
   return render_template('main.html', **templateData)



if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8880, debug=True)
   
