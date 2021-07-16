import pygame
import os

Width, Height = 900, 500
SpaceShip_Width, SpaceShip_Height = 55, 40
FPS = 60

Windows = pygame.display.set_mode((Width,Height))
pygame.display.set_caption('Test')

#Colors
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Yellow = (255, 255, 0)

#Velocity
Vel = 5
Bullets_Vel = 7

#Max qty of bullets in the screen
Max_Bullets = 3

BorderWidth = 10
Border = pygame.Rect(Width//2 - BorderWidth/2, 0, BorderWidth , Width)

#Yellow_SpaceShip
Yellow_SpaceShip = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))

Yellow_SpaceShip = pygame.transform.scale(Yellow_SpaceShip,(SpaceShip_Width, SpaceShip_Height))

Yellow_SpaceShip = pygame.transform.rotate(Yellow_SpaceShip,270)

#Red_SpaceShip
Red_SpaceShip = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

Red_SpaceShip = pygame.transform.scale(Red_SpaceShip,(SpaceShip_Width, SpaceShip_Height))

Red_SpaceShip = pygame.transform.rotate(Red_SpaceShip,90)

#BackGround
Space = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'nebula.jpg')), (Width, Height))

#Bullets

def Draw_Windows(Background,Yellow,Red):
	Windows.blit(Background,(0,0))
	pygame.draw.rect(Windows,Black,Border)
	Windows.blit(Yellow_SpaceShip,(Yellow.x,Yellow.y))
	Windows.blit(Red_SpaceShip,(Red.x,Red.y))
	pygame.display.update()

def KeyBoard(Yellow,Red):
	KeyPressed = pygame.key.get_pressed()

	#Yellow SpaceShip
	if KeyPressed[pygame.K_LEFT] and (Yellow.x - Vel) >= Border.x + Yellow.width:
		Yellow.x -= Vel
	if KeyPressed[pygame.K_RIGHT] and (Yellow.x + Vel) <= Width - Yellow.width + 15:
		Yellow.x += Vel
	if KeyPressed[pygame.K_UP] and (Yellow.y - Vel) >= 0:
		Yellow.y -= Vel
	if KeyPressed[pygame.K_DOWN] and (Yellow.y + Vel) <= Height - Yellow.height - 15:
		Yellow.y += Vel

	#Red SpaceShip
	if KeyPressed[pygame.K_a] and (Red.x - Vel) >= 0:
		Red.x -= Vel
	if KeyPressed[pygame.K_d] and (Red.x + Vel) <= Border.x - Red.width:
		Red.x += Vel
	if KeyPressed[pygame.K_w] and (Red.y - Vel) >= 0:
		Red.y -= Vel
	if KeyPressed[pygame.K_s] and (Red.y + Vel) <= Height - Red.height - 15:
		Red.y += Vel	#Red SpaceShip
	if KeyPressed[pygame.K_a] and (Red.x - Vel) >= 0:
		Red.x -= Vel
	if KeyPressed[pygame.K_d] and (Red.x + Vel) <= Border.x - Red.width:
		Red.x += Vel
	if KeyPressed[pygame.K_w] and (Red.y - Vel) >= 0:
		Red.y -= Vel
	if KeyPressed[pygame.K_s] and (Red.y + Vel) <= Height - Red.height - 15:
		Red.y += Vel


def main():
	run = True
	Clock = pygame.time.Clock()
	Bullets = {'Red':[],'Yellow':[]}

	Red = pygame.Rect(100,300,SpaceShip_Width, SpaceShip_Height)
	Yellow = pygame.Rect(700,300,SpaceShip_Width, SpaceShip_Height)

	while run:
		Clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
		
		KeyBoard(Yellow,Red)

		Draw_Windows(Space,Yellow,Red)

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LCTRL and len(Bullets['Red']) < Max_Bullets:
				Bullet = pygame.Rect(Red.x + Red.width,Red.y + Red.height//2,10,5)
				Bullets['Red'].append(Bullet)
			if event.key == pygame.K_RCTRL and len(Bullets['Yellow']) < Max_Bullets:
				Bullet = pygame.Rect(Yellow.x - Yellow.width,Yellow.y - Yellow.height//2,10,5)
				Bullets['Yellow'].append(Bullet)
				pygame.draw.rect(Windows,Yellow,Bullet)
			

if __name__=='__main__':
	main()
