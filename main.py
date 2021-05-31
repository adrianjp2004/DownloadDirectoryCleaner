import os
from os import path
import shutil

extensiones = {
	"video": [".mp4", ".avi", ".mpeg", ".mwv"],
	"audio": [".mp3", ".wav", ".wma"],
	"imagen": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
	"comprimidos": [".zip", ".rar", ".tar", ".gz"],
	"textos": [".txt", ".doc", ".docx"],
	"ejecutables": [".exe", ".bat", ".dll", ".sys"]
}

def pause():
	pause = input()

if __name__ == "__main__":
	username = input("Ingrese su nombre de usuario en windows: ")
	downloaddir = "C:/Users/"+ username +"/Downloads"

	if path.isdir(downloaddir):
		os.chdir(downloaddir)
		elementos = os.listdir()

		if not path.isdir(downloaddir + "/otros"):
			os.mkdir(downloaddir + "/otros")
		if not path.isdir(downloaddir + "/video"):
			os.mkdir(downloaddir + "/video")
		if not path.isdir(downloaddir + "/imagen"):
			os.mkdir(downloaddir + "/imagen")
		if not path.isdir(downloaddir + "/audio"):
			os.mkdir(downloaddir + "/audio")
		if not path.isdir(downloaddir + "/ejecutables"):
			os.mkdir(downloaddir + "/ejecutables")
		if not path.isdir(downloaddir + "/comprimidos"):
			os.mkdir(downloaddir + "/comprimidos")
		if not path.isdir(downloaddir + "/textos"):
			os.mkdir(downloaddir + "/textos")

		for elemento in elementos:
			if not path.isdir(elemento):
				root, ext = path.splitext(elemento)
					
				rext = False

				for extension in extensiones:
					for ex in extensiones[extension]:
						if ext == ex:
							shutil.move(elemento, extension)
							rext = True

				if not rext:
					shutil.move(elemento, "otros")

		print("accion realizada")
		pause()