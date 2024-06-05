import configparser
import os

autoSave = False
config = configparser.ConfigParser()
config.read("config.ini")

def autoSave(a):
	global autoSave
	autoSave = a

def save():
	with open('config.ini', 'w') as config_file:
		config.write(config_file)

def set(a,b,c):
	try:
		config.set(a, b, c)
	except configparser.NoSectionError:
		config.add_section(a)
		config.set(a, b, c)
	except TypeError:
		try:
			config.set(a, b, str(c))
		except configparser.NoSectionError:
			config.add_section(a)
			config.set(a, b, str(c))
	if autoSave:
		save()

def get(a,b):
	try:
		textGet = config.get(a,b)
		if textGet.startswith("["):	
			newTxtGet = ""
			for i in textGet.replace("[", "").replace("]", "").replace("'", "").split(","):
				if i.startswith(" "):
					newTxtGet+=i[1:]
				else:
					newTxtGet+=i
				newTxtGet+=","
			newTxtGet = newTxtGet.split(",")
			del newTxtGet[-1]
			return newTxtGet
		else:
			return textGet
	except Exception as e:
		print(e)
		return None