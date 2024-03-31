import pygame as p # initialisation and constants
import math as m
import random

WIDTH = 800
HEIGHT = 800
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (20, 180, 20)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

p.init()
screen = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption("orbit")
clock = p.time.Clock()
run = True

class Planet: 
	def __init__(self,size,colour,radius,centre):
		self.size = size # radius of planet
		self.colour = colour 
		self.radius=radius # orbit radius
		self.x=centre[0]+radius # starting location
		self.y=centre[1]+radius
		self.centre=centre # centre of orbit
		self.angle = random.randint(1,360)
		period=m.sqrt(radius**3) # keplers third law 
		d=5*2*m.pi*radius # the 5 here increases the speed, 2*pi*r is the circumference
		self.speed = d/period # speed = distance/time
	def update(self,centre):
		self.angle+=self.speed 
		self.centre=centre # updates centre, for moons
		self.x=self.centre[0]+self.radius*m.sin(m.radians(self.angle)) # maths is cool sometimes
		self.y=self.centre[1]+self.radius*m.cos(m.radians(self.angle))
		p.draw.circle(screen,self.colour,(self.x,self.y),self.size)

stars=[] # spacey background
for i in range(200):
	stars.append((random.randint(1,WIDTH),random.randint(1,HEIGHT)))


planets=( # size, colour, orbital radius, centre (here always the "sun")
Planet(2,(150,150,150),80,(int(WIDTH/2),int(HEIGHT/2))), # Mercury
Planet(5,(255,100,0),100,(int(WIDTH/2),int(HEIGHT/2))), # Venus
Planet(5,GREEN,120,(int(WIDTH/2),int(HEIGHT/2))), # Earth
Planet(3,RED,150,(int(WIDTH/2),int(HEIGHT/2))), # Mars
Planet(12,(168, 105, 50),200,(int(WIDTH/2),int(HEIGHT/2))), # Jupiter
Planet(10,(204, 171, 63),250,(int(WIDTH/2),int(HEIGHT/2))), # Saturn 
Planet(8,(0,255,255),320,(int(WIDTH/2),int(HEIGHT/2))), # Uranus
Planet(8,(0,0,255),380,(int(WIDTH/2),int(HEIGHT/2))) # Neptune
)
moons=((),(), # each array corresponds to a planet, hence the empty arrays
[Planet(2,(100,100,100),10,(planets[2].x,planets[2].y))],(), # Earth's moon
[Planet(3,(100,100,100),24,(planets[4].x,planets[4].y)), # Ganmede, Io, Callisto, Europa
Planet(2,(79, 76, 72),28,(planets[4].x,planets[4].y)), # (I forgot which order tbh )
Planet(1,(176, 171, 97),17,(planets[4].x,planets[4].y)),
Planet(2,(181, 181, 181),20,(planets[4].x,planets[4].y))],
[Planet(3,(235, 178, 87),20,(planets[5].x,planets[5].y))],(), # Titan (no moons for uranus)
[Planet(2,(148, 115, 125),12,(planets[7].x,planets[7].y))] # Triton
)
while run: # main loop
	clock.tick(FPS)
	for event in p.event.get():
		if event.type == p.QUIT:
			run=False

	screen.fill(BLACK)
	
	for i in stars: # display "stars" and sun
		p.draw.circle(screen,WHITE,(i[0],i[1]),1)
	p.draw.circle(screen,YELLOW,(int(WIDTH/2),int(HEIGHT/2)),50) #
	
	for i in planets: # display planets and moons
		i.update((int(WIDTH/2),int(HEIGHT/2)))
	for i in range(len(moons)):
		for j in range(len(moons[i])):
			moons[i][j].update((planets[i].x,planets[i].y))
	p.display.update()

p.quit()
quit()
