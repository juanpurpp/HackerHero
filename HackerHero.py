import pygame, os, math, random, string

#Videojuego creado por
	#Juan Sandoval
	#Francisco Monsalve
	#Yonatan Velasquez
	#Gabriel Gallardo

acierto = False
contid= 0
tiempopas = [0]
def rangode(pointx, pointy, objx, objy):
	#formula de distancia entre dos puntos en un plano cartesiano
	#√((x2 - x1)^2 + (y2 - y1^2))

	dist = math.sqrt((objx - pointx)**2 +(objy - pointy)**2)
	return dist
def randomtext(secuencia):
	if secuencia == ' ':
		secuenciaf = random.choice(string.ascii_letters)
	else:
		secuenciaf = secuencia + random.choice(string.ascii_letters)
	return secuenciaf
def validarletra(teclaget, texto):
	texto = texto.lower()
	#print("validando: ", texto)
	if teclaget[ord(texto[len(texto)-1])] == True:
		return True
	return False
def inittime():
	global contid
	global tiempopas
	contid += 1
	tiempopas.append(pygame.time.get_ticks())
	return contid
def gettime(idcont):
	tiempof = pygame.time.get_ticks() - tiempopas[idcont]
	return tiempof
def adtime(idcont, tiempo):
	tiempopas[idcont] -= tiempo
def formatomin(tiempo):
	print("entra", tiempo)
	tiempo = tiempo/1000
	tiempo = int(round(tiempo, 0))
	minu = 0
	seg = 0
	print("quedo ", tiempo)
	while(tiempo >= 60):
		tiempo -= 60
		minu+=1
	while(tiempo >= 1):
		tiempo -= 1
		seg+=1
	if(minu <10 and seg < 10):
		res = "0%d: 0%d" % (minu,seg)
	elif(minu < 10):
		res = "0%d:%d" % (minu,seg)
	elif(seg < 10):
		res = "%d:0%d" %(minu, seg)
	else: 
		res = "%d:%d" %(minu, seg)
	print("quedo", res)
	return res

blanco = (255, 255, 255 )
negro = (0,0,0)
verde = (51, 245, 66 )
rojo = (204, 50, 52)
print("Ejecutando HackerHero")
pygame.font.init()
#texto iniciar juego?
fconsola = pygame.font.SysFont('Consolas', 30)
finiciar = pygame.font.SysFont('Comic Sans MS', 30)
textinit = finiciar.render('¿Iniciar partida?', True, (0, 0, 0))
#texto jeguo iniciado
#finiciado = pygame.font.SysFont('Comic Sans MS', 30)
#textjuego = finiciar.render('Juego iniciado', False, (0, 0, 0))
#texto puntos
fpuntos = pygame.font.SysFont('Franklin Gothic', 30)
#texto mensaje
fmsg = pygame.font.SysFont('Franklin Gothic', 30)
txtmsg = fmsg.render('', True, (0, 0, 0)) 

textdos = fconsola.render('', True, rojo)
#texto put
fput = pygame.font.SysFont('Consolas', 30)
fletra= pygame.font.SysFont('Consolas', 30)
textoput = fput.render('>', True, verde)
#texto ayda
txthelp = pygame.image.load('texturas/txtapret.png')

#texto juegil
fjuego = pygame.font.SysFont('Consolas', 30)


pygame.init()


#sonidos y musica

sonentrar = pygame.mixer.Sound('musica/audioentrar.ogg')
fallo = pygame.mixer.Sound('musica/fallo.ogg')
perder = pygame.mixer.Sound('musica/perder.ogg')
ganar = pygame.mixer.Sound('musica/ganar.ogg')
cancion = pygame.mixer.music.load("musica/cancionmodelo.mp3")
#caracteristicas de objetos
prejuego = 1
juegoprincipal = 2
finb = 3
finm = 4
modo = 1

tab = 2
notab = 1
submodo = 1
#Sector computadora
comp_an = 300
comp_alt = 250
comp_x =200
comp_y = 0
#pantalla
fondo = pygame.image.load('texturas/Habitacion.png')

inittxt = pygame.image.load('texturas/iniciarpartidatxt.png')
savetxt = pygame.image.load('texturas/guardarpartidatxt.png')
vx = 1280
vy = 650
#imagen jugador
jug_png = pygame.image.load('texturas/jugador.png')
jug_vel= 15
jug_alt= jug_png.get_height()
jug_an= jug_png.get_width()
jug_x = (vx- jug_an)//2
jug_y = vy- jug_alt

#imagenes servidores y proce

servidor = pygame.image.load('texturas/servidor.png')
servidor2 = pygame.image.load('texturas/servidor.png')
core = pygame.image.load('texturas/core.png')

server1 = True;
server2 = True;

bitcoin = pygame.image.load('texturas/bitcoin.png')
x = 0
y = 30
ganadas = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
ventana = pygame.display.set_mode((vx, vy))
pygame.display.set_caption("HackerHero")
tiempoprueba = inittime()
reloj = pygame.time.Clock()
juego = True
textorand = ' '
letra = ' '
textotab = ''
encendido = inittime()
sonentrar.play()
txtmsg = pygame.image.load('texturas/nada.png')
libro = pygame.image.load('texturas/libro.png')
while juego:
	textorand = ' '
	letra = ' '
	textotab = ''
	jugando = True
	ayuda = False
	control = False
	while jugando:
		reloj.tick(50)
		ventana.blit(fondo, (0,0))
		keys = pygame.key.get_pressed()
		#Reconocimiento de teclas
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				quit()
			if evento.type == pygame.KEYDOWN:
				if((evento.key > 65 and evento.key < 125) or evento.key == 32) and len(textotab) <= 23:
					letra = chr(evento.key)
					if submodo == tab:
						textotab+= chr(evento.key)
						print(textotab)
				elif(evento.key == 8):
						textotab = textotab[:-1]
				if evento.key == 27:
					print('presiona esto')
					if ayuda:
						ayuda = False
					else:
						ayuda = True
				if evento.key == 13 and submodo == tab and modo == juegoprincipal:
					if(textotab == "puntosxd"): puntos += 500
					if(textotab == "crear ddos"):
						if(server2 == False):
							textdos = fletra.render("Ya murieron 2 servidores", True, rojo)
						elif(puntos >= 200):
							if(gettime(contador) - 10000) < 0:
								adtime(contador, -gettime(contador))
							else:
								adtime(contador, -10000)
							textdos = fletra.render("Colapsó un servidor", True, verde)
							txtmsg = pygame.image.load('texturas/txtddos.png')
							if server1 == True:
								server1 = False	
								servidor = pygame.image.load('texturas/servidorno.png')
								puntos -= 200
							else:
								server2 = False
								servidor2 = pygame.image.load('texturas/servidorno.png')
								puntos -= 200
						else:
							textdos = fletra.render('Necesitas 200 bitcoin', True, rojo)
							fallo.play()
					elif(textotab == "crear virus"):
						if(proce == False):
							textdos = fletra.render("Ya creó un virus", True, rojo)
						elif(puntos >= 500):
							textdos = fletra.render("Destruyó un core", True, verde)
							txtmsg = pygame.image.load('texturas/txtvirus.png')
							core = pygame.image.load('texturas/coreno.png')
							puntos -= 500
							proce = False
						else: 
							textdos = fletra.render("Necesitas 500 pts", True, rojo)
							fallo.play()
					elif(textotab == "overclock true"):
						if(puntos>= 100):
							txtmsg = pygame.image.load('texturas/txtover.png')
							if len(textorand ) + 5 > 27:  
								for i in range(27 - len(textorand)): 
									textorand = randomtext(textorand)
							else:
								for i in range(5):
									textorand = randomtext(textorand)
							puntos -= 100
						else:
							textdos = fletra.render("Necesitas 100 bitcoin", True, rojo)
					elif(textotab == "ola mundo"):
						if(puntos >= 0):
							textdos = fletra.render("ola mundo XD", True, verde)
							puntos += 5000
						else: 
							textdos = fletra.render("Necesitas 700 pts", True, rojo)
							fallo.play()
					else:
						textdos = fletra.render("No se encontró comando", True, rojo)
						fallo.play()
					if server1 == False and server2 == False and proce == False:
						modo = finb
						contfin = inittime()
						ganadas+=1
						fondo = pygame.image.load('texturas/ganar.png')
						ganar.play()
					textotab = ''
				print("guardando ", letra )
				if(evento.key == 9):
					if(submodo == tab):
						submodo = notab
						print("modo no tab activado")
						textotab = ''
					elif(submodo == notab): 
						submodo = tab
						print("modo tab activado")

		if(modo == prejuego):
			leti = 0
			#movimiento jugador
			if keys[pygame.K_LEFT] and jug_x-jug_vel > 0:
				jug_x-=jug_vel
				jug_png = pygame.image.load("texturas/jugadorizq.png")
			if keys[pygame.K_RIGHT] and jug_x+jug_vel < vx - jug_an:
				jug_x+=jug_vel
				jug_png = pygame.image.load("texturas/jugadorder.png")
			if keys[pygame.K_UP] and jug_y-jug_vel > 0:
				jug_y-=jug_vel
				jug_png = pygame.image.load("texturas/jugadortras.png")
			if keys[pygame.K_DOWN] and jug_y+jug_vel < vy - jug_alt:
				jug_y+=jug_vel
				jug_png = pygame.image.load("texturas/jugadorfrente.png")
			#render jugador
			ventana.blit(jug_png,(jug_x, jug_y))
			ventana.blit(txthelp, (200, 600))
			#jugador en computadora
			if rangode(comp_x, comp_y, jug_x, jug_y) < 150:
				print("cerca del objetivo")
				ventana.blit(inittxt, (0, 0)) #texto de iniciar juego

				if keys[pygame. K_RETURN ]:
					modo = juegoprincipal
					fondo = pygame.image.load('texturas/computadores.png') 
					servidor = pygame.image.load('texturas/servidor.png')
					servidor2 = pygame.image.load('texturas/servidor.png')
					core = pygame.image.load('texturas/core.png')
					txtmsg = pygame.image.load('texturas/nada.png')
					if(ganadas == 0):
						nivel = pygame.image.load('texturas/txtnivel1.png')
					if(ganadas == 1):
						nivel = pygame.image.load('texturas/txtnivel2.png')
					if(ganadas == 2):
						nivel = pygame.image.load('texturas/txtnivel3.png')
					textdos = fmsg.render(" ", True, rojo)
					textorand = ''
					textorand = randomtext(textorand)
					puntos = 0
					server1 = True
					server2 = True
					proce = True
					sonentrar.play()
					pygame.mixer.music.play(-1)
					contador = inittime()
					print("pasaron", gettime(tiempoprueba), "desde el inicio\n\n\n")
					if(ganadas == 0):
						jefe = pygame.image.load('texturas/jefe1.png')
					elif(ganadas == 1):
						jefe = pygame.image.load('texturas/jefe2.png')
					elif(ganadas >= 2):
						jefe = pygame.image.load('texturas/jefe3.png')

			else:
				print("se alejo")
		#juego principalp
		if(modo == juegoprincipal):
			if (gettime(contador) >= (60*1000)*2 and ganadas == 0) or (gettime(contador) >= (60*1000)*1 + 30*1000 and ganadas == 1) or (gettime(contador) >= (60*1000) and ganadas >= 2):
				jug_x = 1000
				jug_y = 400
				fondo = pygame.image.load('texturas/perder.png')
				perder.play()
				modo = finb
				contfin = inittime()
			longtext = len(textorand)
			#modo notab
			if(submodo == notab):
				if validarletra(keys, textorand):
					if (textorand.lower()[longtext-2] == textorand.lower()[longtext-1] ) and longtext >1:
						puntos += 100
						txtmsg = fmsg.render('Ha conseguido un doble y sumar 50 pts', True, (0, 0, 0))
						txtmsg = pygame.image.load('texturas/txtdoble.png')
					textorand = randomtext(textorand)
				if(longtext > 27): #revisar si completo una linea
					puntos += 300
					txtmsg = pygame.image.load('texturas/txtdeco.png')
					textorand = ' '
					textorand = randomtext(textorand)
				textoletra = fletra.render(letra, True, verde)
				ventana.blit(textoletra,(720, 370))
			elif(submodo == tab):
				#textotab = textad(textotab)
				textmostrar = fput.render(textotab, True, verde)
				ventana.blit(textmostrar, (148, 325))
				ventana.blit(textdos, (150, 360))
			#tiempo partida
			ton = gettime(encendido)
			if ton >= 0  and ton < 500:
				if submodo == tab:
					ventana.blit(textoput, (130, 325))
				else:
					ventana.blit(textoput,(700, 370))
			elif ton >= 1000:
				encendido = inittime()
			#impresiones
			txtjuego = fjuego.render(textorand, True, verde)

			ventana.blit(txtjuego,(680, 320))
			textopuntos = '   : %d' % puntos 
			txtpuntos = fpuntos.render(textopuntos, True, blanco)
			timecont = formatomin(gettime(contador))
			txtcont = fmsg.render(timecont, True, blanco)
			ventana.blit(jefe, (600,20))
			ventana.blit(txtcont, (1180, 50))
			ventana.blit(txtmsg, (680, 230))
			ventana.blit(txtpuntos, (1180,110))
			ventana.blit(servidor, (0, 20))
			ventana.blit(core, (150, 20))
			ventana.blit(servidor2, (300, 20))
			ventana.blit(bitcoin, (1152, 96))
			ventana.blit(nivel, (100, 600))
		if(modo == finb):
			pygame.mixer.music.stop()	
			jug_y = 500
			jug_x = 900
			print("pasaron", gettime(contfin), "de la wea" )
			if(gettime(contfin) >= 4000):
				fondo = pygame.image.load('texturas/habitacion.png')
				modo = prejuego
				jugando = False
		if ayuda:
			ventana.blit(libro, (0,0))
		#actualizacion del frame
		# pygame.draw.rect(ventana,blanco, (350, 0, 300, 250)) #cuadrado de visulizacion de ayuda
		pygame.display.update()
pygame.time.delay(2000)
pygame.quit()
