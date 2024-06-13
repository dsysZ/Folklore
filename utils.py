import pygame

tela_width = 800
tela_height = 600
blk_width = int(tela_width // 42)
blk_height = int(tela_height // 20)
tela = pygame.display.set_mode((tela_width, tela_height))
#function to scale images 2x
def scale2x(imagem):
	imgscaled = pygame.transform.scale2x(imagem)
	return imgscaled
#function to load tiles in size
def image_load(img_set, x, y):
	img = img_set.subsurface((x, y), (32, 32))
	img_scaled = pygame.transform.scale(img, (blk_width, blk_height))
	return img_scaled
#function to draw map
def desenha_mapa(map, caracter_img):
	#loop to draw sprites
	for id_linha, linha in enumerate(map):
		for id_coluna, caractere in enumerate(linha):
			if caractere in caracter_img:
				x = id_coluna * blk_width
				y = id_linha * blk_height
				img = caracter_img[caractere]
				tela.blit(img, (x, y))
#this function gives a image from a specific spritesheet
def get_frame_by_gid(sprite, gid, columns, w, h, spc_h, spc_v, top, margin):
	linha = gid // columns
	coluna = gid % columns 
	x = (coluna * (w + spc_h)) + margin
	y = (linha * (h + spc_v)) + top
	quadro = sprite.subsurface(pygame.Rect((x, y), (w, h)))
	return quadro

#variables and sprites local
PISCANDO = [1, 8, 9] 
ANDANDO_DEVAGAR = [16, 17, 18]
ANDANDO = [19, 20, 21, 22, 23]
CORRENDO = [24, 25, 26, 27, 28, 29, 30, 31]
ABAIXANDO = [32, 33, 34, 35, 36, 37]
PULANDO = [41, 42, 43, 44, 45, 46, 47, 48]
DESAPARECENDO = [49, 50, 51]
MORRENDO = [56, 57, 58, 59, 60, 61, 62, 63]
ATACANDO = [64, 65, 66, 67, 68, 69, 70, 71]
char = pygame.image.load('C:\\Users\\Lenovo\\OneDrive\\Área de Trabalho\\scripts\\Game\\game-env\\sprites\\Char.png').convert_alpha()
grass = pygame.image.load("C:\\Users\\Lenovo\\OneDrive\\Área de Trabalho\\scripts\\Game\\game-env\\sprites\\PixelTexturePack\\Textures\\Elements\\TALLGRASS.PNG").convert_alpha()
tiles = pygame.image.load("C:\\Users\\Lenovo\\OneDrive\\Área de Trabalho\\scripts\\Game\\game-env\\sprites\\tilesmap1.png").convert_alpha()
assets = pygame.image.load("C:\\Users\\Lenovo\\OneDrive\\Área de Trabalho\\scripts\\Game\\game-env\\sprites\\tiles.png").convert_alpha()
door = pygame.image.load("C:\\Users\\Lenovo\\OneDrive\\Área de Trabalho\\scripts\\Game\\game-env\\sprites\\PixelTexturePack\\Textures\\Doors\\SPOOKYDOOR.PNG").convert_alpha()
cat = pygame.image.load('C:\\Users\\Lenovo\\OneDrive\\Área de Trabalho\\scripts\\Game\\game-env\\sprites\\champs\\FreeCatCharacterAnimations\\gatitorun.png').convert_alpha()
wall = image_load(tiles, 135, 0)
terra = image_load(tiles, 160, 64)
path = image_load(tiles, 180, 289)
