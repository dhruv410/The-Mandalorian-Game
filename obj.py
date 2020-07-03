import random
class man:
	def __init__(self, bor, x, y):
		self.__score = 0
		self.__lives = 3
		self.__shield = 0
		self.__coins = 0
		bor[x][y] = '('
		bor[x][y+1] ='*'
		bor[x][y+2] = '_'
		bor[x][y+3] = '_'
		bor[x][y+4] = '*'
		bor[x][y+5] = ')'
		bor[x][y+6] = '/'
		bor[x+1][y] = '<'
		bor[x+1][y+1] = ')'
		bor[x+1][y+2] = ' '
		bor[x+1][y+3] = ' '
		bor[x+1][y+4] = ')'
		bor[x+2][y] = ' '
		bor[x+2][y+1] = '/'
		bor[x+2][y+2] = ' '
		bor[x+2][y+3] = ' '
		bor[x+2][y+4] = '\\'

	@property
	def score(self):
		return self.__score
	@score.setter
	def score(self, a):
		self.__score = a

	@property
	def lives(self):
		return self.__lives
	@lives.setter
	def lives(self, a):
		self.__lives = a
	
	@property
	def shield(self):
		return self.__shield
	@shield.setter
	def shield(self, a):
		self.__shield = a

	@property
	def coins(self):
		return self.__coins
	@coins.setter
	def coins(self, a):
		self.__coins = a


	def fresh (self, bor, height, width, line, shield, gravity):	
		x1 = height
		y1 = width
		x6 = max(5,x1-13)
		x7 = min(49,x1+16)
		y6 = max(0,y1-13)
		y7 = min(299,y1+20)
		tx = x1
		ty = y1
		for x8 in range(x6,x7):
			for y8 in range(y6,y7):
				if bor[x8][y8] == 'M':
					gravity = 0
					if x8 <= x1+2 and x8 >= x1 and y8 >= y1 and y8 <= y1+6:
						tx = x8 -2
						ty = y8 
						break
					if y8 < y1:
						ty -= 1
						# x1 -= 1
					if y8 > y1 + 6:
						ty += 1
						tx -= 1
					if x8 > x1+2:
						# tx += 1
						tx = tx  
					if x8 < x1:
						tx -= 2

					break

		for x in range(height, height + 3):
			for y in range(max(0,width - 1),min(500,width + 8)):
				if bor[x][y] == '$':
					self.score += 1

				if bor[x][y] == 'F' and (self.lives >= 0 or shield == 1):
					if shield != 1:
						self.lives -= 1
					cnt = 1
					while x - cnt >= 5 and y - cnt >= 0 and bor[x-cnt][y-cnt] == 'F':
						bor[x-cnt][y-cnt] = ' '
						cnt += 1
					cnt = 1
					while x + cnt <= 48 and y + cnt <= 299 and bor[x+cnt][y+cnt] =='F':
						bor[x+cnt][y+cnt] = ' '
						cnt += 1
					cnt = 1
					while x - cnt >= 5 and bor[x-cnt][y] == 'F':
						bor[x-cnt][y] = ' '
						cnt += 1
					cnt = 1
					while x + cnt <= 48 and bor[x+cnt][y] == 'F':
						bor[x+cnt][y] = ' '
						cnt += 1
					cnt = 1
					while y - cnt >= 0 and bor[x][y-cnt] == 'F':
						bor[x][y-cnt] = ' '
						cnt += 1
					cnt = 1
					while y + cnt <= 299 and bor[x][y+cnt] == 'F':
						bor[x][y+cnt] = ' '
						cnt += 1 

				if bor[x][y] != 'M'	:
					bor[x][y] = ' '
		
		tx = min(tx,49)
		tx = max(5,tx)
		ty = min(ty,499)
		ty = max(line,ty)
		if ty == 299:
			return height, width, gravity;
		return tx, ty, gravity;

	def new(self,bor,x,y,shield):
		for x5 in range(max(6,x),min(x+3,29)):
			for y5 in range (max(0,y),min(349,y+7)):
				if bor[x5][y5] == '$':
					self.score += 1

				if bor[x5][y5] == 'F' :
				# and (self.lives > 0 or shield ==1):
					if shield != 1:
						self.lives -= 1
					cnt = 1
					while x5 - cnt >= 5 and y5 - cnt >= 0 and bor[x5-cnt][y5-cnt] == 'F':
						bor[x5-cnt][y5-cnt] = ' '
						cnt += 1
					cnt = 1
					while x5 + cnt <= 48 and y5 + cnt <= 299 and bor[x5+cnt][y5+cnt] =='F':
						bor[x5+cnt][y5+cnt] = ' '
						cnt += 1
					cnt = 1
					while x5 - cnt >= 5 and bor[x5-cnt][y5] == 'F':
						bor[x5-cnt][y5] = ' '
						cnt += 1
					cnt = 1
					while x5 + cnt <= 48 and bor[x5+cnt][y5] == 'F':
						bor[x5+cnt][y5] = ' '
						cnt += 1
					cnt = 1
					while y5 - cnt >= 0 and bor[x5][y5-cnt] == 'F':
						bor[x5][y5-cnt] = ' '
						cnt += 1
					cnt = 1
					while y5 + cnt <= 299 and bor[x5][y5+cnt] == 'F':
						bor[x5][y5+cnt] = ' '
						cnt += 1 

		tmx = -1
		tmy = -1
		for x9 in range (x,x+3):
			for y9 in range(y,y+7):
				if bor[x9][y9] == 'M':
					tmx = x9
					tmy = y9
		bor[x][y] = '('
		bor[x][y+1] ='*'
		bor[x][y+2] = '_'
		bor[x][y+3] = '_'
		bor[x][y+4] = '*'
		bor[x][y+5] = ')'
		bor[x][y+6] = '/'
		bor[x+1][y] = '<'
		bor[x+1][y+1] = ')'
		bor[x+1][y+2] = ' '
		bor[x+1][y+3] = ' '
		bor[x+1][y+4] = ')'
		bor[x+1][y+5] = '_'
		bor[x+1][y+6] = '_'
		bor[x+2][y] = '_'
		bor[x+2][y+1] = '/'
		bor[x+2][y+2] = ' '
		bor[x+2][y+3] = ' '
		bor[x+2][y+4] = '\\'
		bor[x+2][y+5] = '_'
		bor[x+2][y+6] = '_'
 		
		if tmx != -1 :
			bor[tmx][tmy] = 'M'


class coins:
	def __init__(self, bor, x, y):
		self.__x1 = random.randint(1,7)
		self.__y1 = random.randint(1,7)

	@property
	def x1(self):
		return self.__x1
	@x1.setter
	def x1(self, a):
		self.__x1 = a

	@property
	def y1(self):
		return self.__y1
	@y1.setter
	def y1(self, a):
		self.__y1 = a

	def place (self, bor, x, y):
		x3 = min(x+self.x1,48)
		y3 = min(399, y + self.y1)
		for x2 in range (x,x3):
			for y2 in range (y,y3):
				bor[x2][y2] = '$'

class beam:
	def __init__(self,bor,x,y):
		self.__leng = random.randint(4,7)
		self.__z = random.randint(1,3)

	@property
	def leng(self):
		return self.__leng
	@leng.setter
	def lives(self, a):
		self.__leng = a

	@property
	def z(self):
		return self.__z
	@z.setter
	def z(self, a):
		self.__z = a	


	def place (self,bor,x,y):
		if self.z == 1 : 
			x3 = min(49-x,self.leng)
			y3 = min(300-y,self.leng)
			y3 = min(x3,y3)
			for x2 in range(y3):
				bor[x+x2][y+x2] = 'F'

		if self.z == 2:
			y3 = min(300-y,self.leng)
			for x2 in range(y3):
				bor[x][y+x2] = 'F'

		if self.z == 3:
			y3 = min(49-x,self.leng)
			for x2 in range(y3):
				bor[x+x2][y] = 'F'

class magnet:
	def __init__ (self, bor, x, y):
		self.__range1 = 3

	@property
	def range1(self):
		return self.__range1
	@range1.setter
	def range1(self, a):
		self.__range1 = a

	def place (self, bor, x, y):
		bor[x][y] = 'M'

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


class manbullet(bullet):
	def __init__(self, bor, x, y):
		bullet.__init__(self,bor,x,y)
	def place (self, bor):
		bor[self.x][self.y] = '>'


class bossbullet(bullet):
	def __init__(self, bor, x, y):
		bullet.__init__(self,bor,x,y)
	def place (self,bor,x,y):
		bor[x][y] = '<'

def checkbullets(bullets, bor, boss, y1, m1):
	bullets1 = []
	for bul in bullets:
		flag = 0
		if bor[bul.x][bul.y] == '>' :
			bor[bul.x][bul.y] = ' '
		elif bor[bul.x][bul.y] == '<':
			bor[bul.x][bul.y] =' '
			continue
		if bor[bul.x][bul.y+1]=='F' or bor[bul.x][bul.y+2] == 'F' or bor[bul.x][bul.y+3]=='F':
			x5 = bul.x
			if bor[bul.x][bul.y+1]=='F':
				y5 = bul.y + 1
			elif bor[bul.x][bul.y+2] =='F' : 
				y5 = bul.y + 2
			else:
				y5 = bul.y+3
			cnt = 1
			while x5 - cnt >= 5 and y5 - cnt >= 0 and bor[x5-cnt][y5-cnt] == 'F':
						bor[x5-cnt][y5-cnt] = ' '
						cnt += 1
			cnt = 1
			while x5 + cnt <= 48 and y5 + cnt <= 299 and bor[x5+cnt][y5+cnt] =='F':
				bor[x5+cnt][y5+cnt] = ' '
				cnt += 1
			cnt = 1
			while x5 - cnt >= 5 and bor[x5-cnt][y5] == 'F':
				bor[x5-cnt][y5] = ' '
				cnt += 1
			cnt = 1
			while x5 + cnt <= 48 and bor[x5+cnt][y5] == 'F':
				bor[x5+cnt][y5] = ' '
				cnt += 1
			cnt = 1
			while y5 - cnt >= 0 and bor[x5][y5-cnt] == 'F':
				bor[x5][y5-cnt] = ' '
				cnt += 1
			cnt = 1
			while y5 + cnt <= 299 and bor[x5][y5+cnt] == 'F':
				bor[x5][y5+cnt] = ' '
				cnt += 1
			bor[x5][y5] = ' '
			m1.coins += 1
		elif bor[bul.x][bul.y+1]=='|' or bor[bul.x][bul.y+2] == '|' or bor[bul.x][bul.y+3]=='|' or bor[bul.x][bul.y+1] =='/' or bor[bul.x][bul.y+2] =='/'or bor[bul.x][bul.y+3] =='/':
			boss.health -= 1

		# elif bor[bul.x][bul.y+2] == '<' :
		# 	bor[bul.x][bul.y+2] = ' '
		# 	flag =1

		# elif bor[bul.x][bul.y+1] == '<' :
		# 	bor[bul.x][bul.y+1] = ' '
		# 	flag = 1

		# elif bor[bul.x][bul.y+3] == '<':
		# 	bor[bul.x][bul.y+3] = ' '
		# 	flag =1

		# elif bor[bul.x][bul.y+4] == '<' :
		# 	bor[bul.x][bul.y+4] = ' '
		# 	flag =1


		# elif bor[bul.x][bul.y+5] == '<' :
		# 	bor[bul.x][bul.y+5] = ' '
		# 	flag =1


		# elif bor[bul.x][bul.y+6] == '<':
		# 	bor[bul.x][bul.y+6] = ' '
		# 	flag =1


		elif bor[ bul.x ][bul.y + 3] == ' ' and flag == 0:
			bor[bul.x][bul.y + 3] = '>'
			bul.y += 3

			if bul.y < y1 + 193:
				bullets1.append(bul)
			else :
				bor[bul.x][bul.y] = ' '

		else :
			bul.y += 3
			if bul.y < y1 + 193:
				bullets1.append(bul)
			else:
				bor[bul.x][bul.y] = ' '
	return bullets1, boss;
