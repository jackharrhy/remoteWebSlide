from bottle import *
from os import getcwd

HOST = '0.0.0.0'
PORT = 80
DEBUG = True 

currentSlide = [0]
slides = 10 

@route("/files/<file>")
def getFile(file):
	return static_file(file, root=os.getcwd()+"/staticFiles/")

@route("/getSlide")
def getSlide():
	return str(currentSlide[0])

@route("/increaseSlide")
def setSlide():
	if currentSlide[0] >= slides:
		return "Cannot increase slide, reached final slide"

	currentSlide[0] = currentSlide[0] + 1 

	return "Complete!, current slide is: " + str(currentSlide[0])

@route("/decreaseSlide")
def setSlide():
	if currentSlide[0] <= 0:
		return "Cannot decrease slide, on the first slide"

	currentSlide[0] = currentSlide[0] - 1

	return "Complete!, current slide is: " + str(currentSlide[0])

@route("/")
def main():
	return "This page is a WIP"

@route("/client")
def client():
	return template("client.tpl")

@route("/remote")
def remote():
	return template("remote.tpl")

run(host=HOST,port=PORT,debug=DEBUG)
