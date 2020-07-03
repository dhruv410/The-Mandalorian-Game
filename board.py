import numpy as np 
from colorama import Fore, Back, Style
class board1:
	def __init__(self, height, width):
		self.__br = np.full((height,width),' ')
		self.__width = width
		self.__height = height
		for x in range(height):
			for y in range(width):
				self.br[x][y] = ' '
		for x in range(width):
			self.br[5][x] = ' '
		for x in range(width):
			self.br[height-1][x] = ' '

	@property
	def br(self):
		return self.__br
	@br.setter
	def br(self, a):
		self.__br = a

	@property
	def width(self):
		return self.__width
	@width.setter
	def width(self, a):
		self.__width = a

	@property
	def height(self):
		return self.__height
	@height.setter
	def height(self, a):
		self.__height = a

	def pri(self,height,width, lives, score, shield,z, shieldtime, shieldlosetime,flag, fastime, boss, bosstage, coins, timeleft):

		s = ""
		s += "\033[0;0H"
		if lives < 0:
			s += 'TIME LEFT = ' + str(int(timeleft)) + '      LIVES = ' + str(0) + '     ' + 'SCORE = ' + str(coins) +     '      COINS = ' + str(score) + '       GAME OVER!                             '	
		elif shield == 0 and 60 >= int(z-shieldlosetime) : 
			s += 'TIME LEFT = ' + str(int(timeleft)) + '      LIVES = ' + str(lives) + '     ' + 'SCORE = ' + str(coins) + '      COINS = ' + str(score) + '       SHIELD REACTIVATES IN : ' + str(60-int(z-shieldlosetime)) +                              '                        '
		elif shield == 0:
			s += 'TIME LEFT = ' + str(int(timeleft)) + '      LIVES = ' + str(lives) + '     ' + 'SCORE = ' + str(coins) + '      COINS = ' + str(score) + '       YOU CAN REACTIVATE THE SHIELD                     '
		else :
			s += 'TIME LEFT = ' + str(int(timeleft)) + '      LIVES = ' + str(lives) + '     ' + 'SCORE = ' + str(coins) + '      COINS = ' + str(score) + '       SHIELD TIME : '  + str(int(z - shieldtime)) + '                     '

		if bosstage == 1:
			s += '               ' + 'BOSS HEALTH : ' + str(boss.health) + '        '
		else:
			s += '                                                                                '
		s += "\n"

		for x in range(5,height):
			for x1 in range(width, width+200):
				var = self.br[x][x1]
					# print(self.br[x][x1], end = '')
				if var == 'F':
					s += Back.RED + Fore.YELLOW + var + Style.RESET_ALL
				elif var == '$':
					s += Fore.BLUE + var + Style.RESET_ALL
				elif var == '*' and shield == 0:
					s += Back.GREEN + Fore.GREEN + var + Style.RESET_ALL 
				elif var == '*':
					s += Back.YELLOW + Fore.YELLOW + var + Style.RESET_ALL 
				elif var == 'M':
					s += Back.YELLOW + Style.BRIGHT + Fore.YELLOW + Style.BRIGHT +  var + Style.RESET_ALL 
				elif x == 5:
					s += Back.BLUE+ Style.BRIGHT + Fore.BLUE + Style.BRIGHT + var + Style.RESET_ALL 
				elif x == height - 1:
					s += Back.BLUE+ Style.BRIGHT + Fore.BLUE + Style.BRIGHT + var + Style.RESET_ALL 	
				else:
					s += var
			s += "\n"

		print(s)