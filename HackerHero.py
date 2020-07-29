import pygame, os, math, random, string


acierto = False
def rangode(pointx, pointy, objx, objy):
	#formula de distancia entre dos puntos en un plano cartesiano
	#√((x2 - x1)^2 + (y2 - y1^2))

	dist = math.sqrt((objx - pointx)**2 +(objy - pointy)**2)
	return dist
def randomtext(secuencia):
	if secuencia == '\0':
		secuencia = random.choice(string.ascii_letters)
	else:
		secuenciaf = secuencia + random.choice(string.ascii_letters)
	return secuenciaf
def validarletra(teclaget, texto):
	texto = texto.lower()
	print("validando: ", texto)
	if teclaget[ord(texto[len(texto)-1])] == True:
		return True
	return False
blanco = (233, 255, 134 )

print("Ejecutando HackerHero")
pygame.font.init()
#texto iniciar juego?
finiciar = pygame.font.SysFont('Comic Sans MS', 30)
textinit = finiciar.render('¿Iniciar partida?', False, (0, 0, 0))
#texto jeguo iniciado
finiciado = pygame.font.SysFont('Comic Sans MS', 30)
textjuego = finiciar.render('Juego iniciado', False, (0, 0, 0))
#texto juegil
fjuego = pygame.font.SysFont('Consolas', 30)

#caracteristicas de objetos
prejuego = 1
juegoprincipal = 2
modo = 1
#Sector computadora
comp_an = 300
comp_alt = 250
comp_x =450
comp_y = 0
#pantalla
fondo = pygame.image.load('texturas/Habitacion.png')

vx = 1280
vy = 650
#imagen jugador
jug_png = pygame.image.load('texturas/jugador.png')
jug_vel= 15
jug_alt= jug_png.get_height()
jug_an= jug_png.get_width()
jug_x = (vx- jug_an)//2
jug_y = vy- jug_alt

#

pygame.init()

x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

ventana = pygame.display.set_mode((vx, vy))
pygame.display.set_caption("WENAAA")

reloj = pygame.time.Clock()
juego = True
while juego:
	jugando = True
	while jugando:
		reloj.tick(50)
		ventana.blit(fondo, (0,0))
		keys = pygame.key.get_pressed()
		#Reconocimiento de teclas
		if(modo == prejuego):
			leti = 0
			#movimiento jugador
			if keys[pygame.K_LEFT] and jug_x-jug_vel > 0:
				jug_x-=jug_vel
			if keys[pygame.K_RIGHT] and jug_x+jug_vel < vx - jug_an:
				jug_x+=jug_vel
			if keys[pygame.K_UP] and jug_y-jug_vel > 0:
				jug_y-=jug_vel
			if keys[pygame.K_DOWN] and jug_y+jug_vel < vy - jug_alt:
				jug_y+=jug_vel
			#render jugador
			ventana.blit(jug_png,(jug_x, jug_y))
			#jugador en computadora
			if rangode(comp_x, comp_y, jug_x, jug_y) < 150:
				print("culiao serca xd")
				ventana.blit(textinit, (800, 100))

				if keys[pygame. K_RETURN ]:
					modo = juegoprincipal
					fondo = pygame.image.load('texturas/computadores.png')
					textorand = ''
					textorand = randomtext(textorand)
			else:
				print("se alejo")
		#juego principalp
		if(modo == juegoprincipal):
			print("edehola")
			ventana.blit(textjuego, (800, 200))
			txtjuego = fjuego.render(textorand, False, (51, 245, 66 ))
			ventana.blit(txtjuego,(710, 330))
			if validarletra(keys, textorand): 
				textorand = randomtext(textorand)
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit()
			if(modo == juegoprincipal):
				print 
		#actualizacion del frame
		# pygame.draw.rect(ventana,blanco, (350, 0, 300, 250)) #cuadrado de visulizacion rango de cama
		pygame.display.update()
pygame.time.delay(2000)
pygame.quit()
