from bottle import *
from os import getcwd

HOST = '0.0.0.0'
PORT = int(input('What port should I use? > '))
DEBUG = True 

currentSlide = [0]
slides = 3

@route("/static/js/<file>")
def getJsFile(file):
    return static_file(file, root=os.getcwd()+"/static/js")

@route("/static/css/<file>")
def getCssFile(file):
    return static_file(file, root=os.getcwd()+"/static/css")

@route("/static/font/<file>")
def getFont(file):
    return static_file(file, root=os.getcwd()+"/static/font")

@route("/getSlide")
def getSlide():
    return str(currentSlide[0])

@route("/increaseSlide")
def setSlide():
    if currentSlide[0] >= slides:
        return "Cannot increase slide, reached final slide"

    else:
        currentSlide[0] = currentSlide[0] + 1 

        return "Complete!, current slide is: " + str(currentSlide[0])

@route("/decreaseSlide")
def setSlide():
    if currentSlide[0] <= 0:
        return "Cannot decrease slide, on the first slide"

    else:
        currentSlide[0] = currentSlide[0] - 1

        return "Complete!, current slide is: " + str(currentSlide[0])

@route("/")
def main():
    return template("index.tpl")

@route("/client")
def client():
    return template("client.tpl")

@route("/remote")
def remote():
    return template("remote.tpl")

run(host=HOST,port=PORT,debug=DEBUG)

