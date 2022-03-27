import os
import logging
import time
 
from flask import Flask
from flask_ask import Ask, request, session, question, statement
#import RPi.GPIO as GPIO
 
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)
 
STATUSON = ["on", "switch on", "enable", "power on", "activate", "turn on"]
STATUSOFF = ["off", "switch off", "disactivate", "disable", "turn off", "power off"]

def wrf1(fname):
    f = open(fname, "w")
    f.write("1")
    f.close()

def wrf0(fname):
    f = open(fname, "w")
    f.write("0")
    f.close()

def wrf3(fname,intent):
    f = open(fname, "w")
    f.write(intent)
    f.close()

@ask.launch
def launch():
    wrf1("flgS")
    time.sleep(1)
    speech_text = ' '
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('Couch', mapping = {'status':'status'})
def Couch_Intent(status,room):
    if status in STATUSON:
        wrf3("spkC","11")
        time.sleep(0.1)
        wrf1("flgC")
        return statement('')
    elif status in STATUSOFF:
        wrf3("spkC","10")
        time.sleep(0.1)
        wrf0("flgC")
        return statement('')
    else:
        return statement('Sorry, this command is not possible.')

@ask.intent('Lightintent', mapping = {'status':'status'})
def Gpio_Intent(status,room):
    if status in STATUSON:
        wrf3("spkL","11")
        time.sleep(0.1)
        wrf1("flgL")
        return statement('')
    elif status in STATUSOFF:
        wrf3("spkL","10")
        time.sleep(0.1)
        wrf0("flgL")
        return statement('')
    else:
        return statement('Sorry, this command is not possible.')
 
@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)
 
 
@ask.session_ended
def session_ended():
    return "{}", 200
 
 
if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
