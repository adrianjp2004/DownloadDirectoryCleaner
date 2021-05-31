import os
from os import path

extensiones = {
	"video": [".mp4", ".avi", ".mpeg", ".mwv"],
	"audio": [".mp3", ".wav", ".wma"],
	"imagen": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
	"comprimidos": [".zip", ".rar", ".tar", ".gz"],
	"codigo": [".java", ".c", ".cpp", ".py", ".js", ".html", ".css", ".h", ".cs", ".cc", ".c++", ".ts", ".go", ".hs"],
	"texto": [".txt", ".doc", ".docx"],
	"exe": [".exe", ".bat", ".dll", ".sys"]
}

def pause():
	pause = input()

if __name__ == "__main__":
	username = input("Ingrese su nombre de usuario en windows: ")

	if path.isdir("C:/Users/"+ username +"/Downloads"):
		print(extensiones)
		