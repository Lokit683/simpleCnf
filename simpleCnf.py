import configparser

class file:
	def __init__(self, name,saveMode):
		if "bool" in str(type(saveMode)):
			self.autoSave = saveMode
		else:
			raise IOError("Use example file('fileName', True or False)\n")
		self.fileName= name
		self.config = configparser.ConfigParser()
		self.config.read(name)
	def save(self):
		with open(self.fileName, 'w') as config_file:
			self.config.write(config_file)
	def set(self, a,b,c):
		try:
			self.config.set(a, b, c)
		except configparser.NoSectionError:
			self.config.add_section(a)
			self.config.set(a, b, c)
		except TypeError:
			try:
				self.config.set(a, b, str(c))
			except configparser.NoSectionError:
				self.config.add_section(a)
				self.config.set(a, b, str(c))
		if self.autoSave:
			self.save()
		def get(self,a,b):
			try:
				textGet = self.config.get(a,b)
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
	def get(self,a,b):
		try:
			textGet = self.config.get(a,b)
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
			return None
	def del_option(self,a,b):
		try:
			self.config.remove_option(a, b)
			return 1
		except:
			return 0
	def del_section(self,a):
		try:
			self.config.remove_section(a)
			return 1
		except:
			return 0
