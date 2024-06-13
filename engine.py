import pygame
from mapas import mapa1, mapaobj
from utils import *
#initializing pygame and def collision
pygame.init()
def colisao(personagem, map, lista_caracteres):
	colisoes = []
	for id_linha, linha in enumerate(map):
		for id_coluna, caracteres in enumerate(linha):
			if caracteres in lista_caracteres:
				x = id_coluna * blk_width
				y = id_linha * blk_height
				#intention_x = personagem.rect.x + personagem.vel_x
				#intention_y = personagem.rect.y + personagem.vel_y
				r = pygame.Rect((x, y), (blk_width, blk_height))
				r2 = personagem.rect.copy()
				r2.move_ip(personagem.vel_x, personagem.vel_y)
				if r.colliderect(r2):
					colisao = {"linha": id_linha, "coluna": id_coluna}
					colisoes.append(colisao)
	return colisoes
#class character 
class Personagem(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.rect = pygame.Rect((350, 270), (blk_width, blk_height))
		self.vel_x = 0.0
		self.vel_y = 0.0
		self.cicle = 10
		self.count = 0
		self.idx = 0		
		self.frames = [56, 57, 58, 59, 60, 61, 62, 63]
		self.image = self.get_image(5)
#function get_image return a image from a specific sprite(its necessary set the values below)
# !!IMPORTANT!! dont remove get_image from Personagem, it works better here.
	def get_image(self, gid):
		img = get_frame_by_gid(sprite=char, gid=gid, columns=8, w=32, h=32, 
								spc_h=0, spc_v=0, top=0, margin=0)
		return img
#function update gives us update about the sprites, game and stats
	def update(self):
		self.count += 1
		if self.count > self.cicle:
			self.count = 0
			self.idx += 1
			if self.idx >= len(self.frames):
				self.idx = 0
			gid = self.frames[self.idx]
			self.image = scale2x(self.get_image(gid))
			self.rect.x += self.vel_x
			self.rect.y += self.vel_y
#function processar_evento return the events that we have in the game
	def processar_evento(self, e):
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_d:
				self.vel_x = + 5
			if e.key == pygame.K_a:
				self.vel_x = - 5
			if e.key ==	pygame.K_w:
				self.vel_y = - 5
			if e.key == pygame.K_s:
				self.vel_y =  + 5
		if e.type == pygame.KEYUP:
			if e.key in [pygame.K_a, pygame.K_d]:
				self.vel_x = 0.0
			if e.key in [pygame.K_w, pygame.K_s]:
				self.vel_y = 0.0
#here we call class Personagem in hero variable
hero = Personagem()
grupo_hero = pygame.sprite.Group(hero)
#this loop keeps game running, if user quit so exit
#inside the loop we draw the map and hero.
while True:
	desenha_mapa(mapa1, {"p": wall, " ": grass, "s": path, "t": terra})
	desenha_mapa(mapaobj, {"d": door})
	grupo_hero.draw(tela)
	pygame.display.update()
	grupo_hero.update()
		#loop to keep window active
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit()
		hero.processar_evento(e)
