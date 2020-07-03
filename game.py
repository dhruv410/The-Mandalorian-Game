import signal
import os
import time
import random
import math
import colorama
from colorama import Back, Fore, Style
from alarmexception import AlarmException
import obj
from obj import *
import board
from board import *
import numpy as np 
from getch import _getChUnix as getChar
import boss
from boss import *
# po = 

# bosscheckbullets has polymorphism, do ctrl + F

x = 46		#man coordinates
y = 0		#man coordinates
x1 = 50		#current length
y1 = 0	#current length
x2 = 50		#game length
y2 = 500 	 #game length
lives = 3
score = 0
flag = 0
b1 = board1(x2,y2)

pv = 0
i = random.randint(10,15) #coins
# i = 0
j = random.randint(10,15) #beams
for p1 in range (0,i):  #generating coins
	x4 = random.randint(6,48)
	y4 = random.randint(pv+20,pv+40)
	if y4 >= 299:
		break
	c = coins(b1.br,x4,y4)
	c.place(b1.br,x4,y4)
	pv += 40

pv = 20
for p1 in range (0,j): #generating beams
	x4 = random.randint(6,48)
	y4 = random.randint(pv+20,pv+40)
	if y4 >= 299:
		break
	o2 = beam(b1.br,x4,y4)
	o2.place(b1.br,x4,y4)
	pv += 40

pv = 10

k = random.randint(3,5) #placing magnets
for p1 in range(0,k):
	x4 = random.randint(6,48)
	y4 = random.randint(pv+30,pv+60)
	if y4 >= 299:
		break
	mg = magnet(b1.br,x4,y4)
	mg.place(b1.br,x4,y4)
	pv += 60

boss1 = boss(b1.br, 25,449)
boss1.place(b1.br,25,449)

bossx = 25
bossy = 448
leveltime = 150 + time.time()
bullets = []
shield = 0
flag = 0
shieldtime = time.time()
shieldlosetime = time.time() - 60
fastime = time.time() - 10
m1 = man(b1.br,x,y)
bosstage = 0
bossbulletime = time.time()
bossbullets = []
bonus = 0
gravity = 0


def moveman(x,y):
	global bosstage
	global boss1
	global flag
	global shield
	global bossx
	global bossy
	global shieldtime
	global fastime
	global bossbulletime
	global gravity

	def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException

	def user_input(timeout=0.04):
		''' input method '''
		signal.signal(signal.SIGALRM, alarmhandler)
		signal.setitimer(signal.ITIMER_REAL, timeout)
		
		try:
			text = getChar()()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''

	char = user_input()
	if y == 340 or y1 == 300 and boss1.health > 0:

		if bosstage == 0:
			bossbulletime = time.time()
		bosstage = 1

	if bosstage == 1 and time.time() - bossbulletime >= 1.5:

		bossbulletime = time.time()
		bull2 = bosscheckbullets(b1.br,bossx,bossy)

		for x0 in bull2:
			bossbullets.append(x0)

	if char == 'd' and (y < 340 or bosstage==0) :

		gravity += 1
		times = math.ceil(0.5*9.8*gravity*gravity/4000)
		x = min(46,x+gravity)
		y = min(y+1,y1+200-7)


	elif char == 'w':

		gravity = 0
		x = max(x-1,6)
		bossx = max(6,x-12)


	elif char == 'a':
		gravity += 1
		times = math.ceil(0.5*9.8*gravity*gravity/4000)
		x = min(46,x+gravity)
		y = max(y-1,y1)


	elif char == 'q':
		quit()


	elif char == 's':
		x = min(46,x+3)
		bossx = min(6,x-12)
		bossx = min(25,x+12)


	elif char == 'f':
		flag = 1
		fastime = time.time()


	elif char == 'e':
		bul = manbullet(b1.br,x+1,y+7)
		bul.place(b1.br)
		bullets.append(bul)


	elif char == ' ' and time.time() - shieldlosetime >= 60:
		shield = 1
		shieldtime = time.time()


	else :
		gravity += 1
		times = math.ceil(0.5*9.8*gravity*gravity/4000)
		x = min(46,x+gravity)
		bossx = min(25,x+12)

	return x, y, flag;

z = time.time()
os.system('clear')
while True: 
	timeleft = leveltime - time.time()
	if leveltime - time.time() < 0:
		print('YOU LOSE ON TIME!!')
		quit()
	if flag == 1 and time.time() - fastime <= 10:
		if(time.time() - z >= 0.05): #move basic enemies every 0.5 sec
			z=time.time()
			m1.new(b1.br,x,y,shield)
			if bosstage == 1:
				boss1.printboss(b1.br,bossx,bossy)
			if time.time() - shieldtime >=  10 and shield == 1:
				shield = 0
				shieldlosetime = time.time()
			b1.pri(x1,y1, m1.lives, m1.score, shield,z, shieldtime, shieldlosetime,flag, fastime, boss1, bosstage, m1.coins,timeleft)
			bullets, boss1 = checkbullets(bullets, b1.br,boss1, y1, m1)
			bossbullets = bosscheckbullets(b1.br,bossx,bossy,m1, shield,bossbullets)
			if m1.lives == -1:
				quit()
			if boss1.health <= 0:
				if bonus == 0:
					m1.coins += 10
					bonus = 1
				bosstage = 0
			y1 = min(y1+1,y2-200)
			if (y <= 340 or boss1.boss==0) or bosstage == 0:
				y = min(y+1,y1+200-7)

	else:
		flag = 0
		if(time.time() - z >= 0.2): #move basic enemies every 0.5 sec
			z=time.time()
			m1.new(b1.br,x,y,shield)
			if bosstage == 1:
				boss1.printboss(b1.br,bossx,bossy)
			if time.time() - shieldtime >=  10 and shield == 1:
				shield = 0
				shieldlosetime = time.time()
			b1.pri(x1,y1, m1.lives, m1.score, shield,z, shieldtime, shieldlosetime,flag, fastime, boss1, bosstage, m1.coins,timeleft)
			bullets, boss1 = checkbullets(bullets, b1.br, boss1, y1, m1)
			bossbullets = bosscheckbullets(b1.br,bossx,bossy,m1,shield,bossbullets)
			if boss1.health <= 0:
				if bonus == 0:
					m1.coins += 10
					bonus = 1
				bosstage = 0			
			if m1.lives == -1:
				quit()
			y1 = min(y1+1,y2-200)
			if (y <= 340 or boss1.boss == 0) or bosstage == 0:
				y = min(y+1,y1+200-7)

	boss1.fresh(b1.br,bossx,bossy)
	x, y, gravity = m1.fresh(b1.br,x,y,y1,shield,gravity)

	x, y, flag = moveman(x,y)

	if x < 18:
		bossx = 6
	elif x > 37:
		bossx = 25
	else:
		bossx = x - 12

	if y == 499-6:
		print("YOU WIN!!")
		quit()