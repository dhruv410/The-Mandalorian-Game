class boss:
	def __init__ (self, bor, x, y):
		self.__x = x
		self.__y = y
		self.__boss1 = []
		self.__boss = 1
		self.__health = 5

	@property
	def x(self):
		return self.__x
	@x.setter
	def x(self, a):
		self.__x = a

	@property
	def y(self):
		return self.__y
	@y.setter
	def y(self, a):
		self.__y = a

	@property
	def health(self):
		return self.__health
	@health.setter
	def health(self, a):
		self.__health = a

	@property
	def boss(self):
		return self.__boss
	@boss.setter
	def boss(self, a):
		self.__boss = a


	def place (self, bor, c, d):
		with open("./boss.txt") as obj:
			for line in obj:
				self.__boss1.append(line.strip('\n'))
		e = d
		for i in range (24):
			for j in range (49):
				bor[c][d] = self.__boss1[i][j]
				d += 1
			d = e
			c += 1

	def fresh(self,bor,c,d):
		for x1 in range(c, c + 24):
			for y1 in range(d, d + 50):
				# print(x1,y1)
				bor[x1][y1] = ' '

	def printboss(self,bor,c,d):
		with open("./boss.txt") as obj:
			for line in obj:
				self.__boss1.append(line.strip('\n'))
		e = d
		for i in range (24):
			for j in range (49):
				bor[c][d] = self.__boss1[i][j]
				d += 1
			d = e
			c += 1

class bullet:
	def __init__(self,bor,x,y):
		self.__x = x
		self.__y = y

	@property
	def x(self):
		return self.__x
	@x.setter
	def x(self, a):
		self.__x = a
	@property
	def y(self):
		return self.__y
	@y.setter
	def y(self, a):
		self.__y = a

class bossbullet(bullet):
	def __init__(self, bor, x, y):
		bullet.__init__(self,bor,x,y)
	def place (self,bor,x,y):
		bor[x][y] = '<'

def bossfire(bor,c,d):
	bull2 = []
	for x1 in range(c+2,c+24,2):
		# bor[x][448] = '<'
		# print(x1)
		boss2 = bossbullet(bor,x1,448)
		boss2.place(bor,x1,448)
		bull2.append(boss2)
	return bull2

def bosscheckbullets(bor,c,d,man = 0, shield = -1, bullets = []):
	if shield == -1:
		bull2 = []
		for x1 in range(c+2,c+24,7):
			# bor[x][448] = '<'
			# print(x1)
			boss2 = bossbullet(bor,x1,448)
			boss2.place(bor,x1,448)
			bull2.append(boss2)
		return bull2
	bullets2 = []

	for x in bullets:
		if bor[x.x][x.y] == '<' : 
			bor[x.x][x.y] = ' '
		elif bor[x.x][x.y] == '>':
			bor[x.x][x.y] = ' '
			continue
		if x.y > 300:
			if (bor[x.x][x.y-1]=='_' or bor[x.x][x.y-1] == '/' or bor[x.x][x.y-2]=='_'):
				if shield == 0:
					man.lives -= 1
				else :
					continue
			elif (bor[x.x][x.y-2] == '/' or bor[x.x][x.y-3]=='_' or bor[x.x][x.y-3] == '/'):
				if shield == 0:
					man.lives -=1
				else:
					continue
			# elif bor[x.x][x.y-2] == '>' :
			# 	bor[x.x][x.y-2] = ' '

			# elif bor[x.x][x.y-1] == '>' :
			# 	bor[x.x][x.y-1] = ' '

			# elif bor[x.x][x.y-3] == '>':
			# 	bor[x.x][x.y-3] = ' '

			# elif bor[x.x][x.y-4] == '>' :
			# 	bor[x.x][x.y-4] = ' '

			# elif bor[x.x][x.y-5] == '>' :
			# 	bor[x.x][x.y-5] = ' '

			# elif bor[x.x][x.y-6] == '>':
			# 	bor[x.x][x.y-6] = ' '

			else:
				x.y -= 3 
				bor[x.x][x.y] = '<'
				bullets2.append(x)
	return bullets2
