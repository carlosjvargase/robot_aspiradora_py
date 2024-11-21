from IPython.display import display
import ipywidgets as widgets
import time

class Tablero:
  def __init__(self, tamano_celda=(50, 50), n_celdas=(5,5)):
    self.out = widgets.HTML()
    display(self.out)
    self.tamano_celda = tamano_celda
    self.n_celdas = n_celdas

  def dibujar(self, objetos):
    tablero = "{}"
    filas = ""

    for i in range(self.n_celdas[0]):
      s = ""
      for j in range(self.n_celdas[1]):
        contenido =""
        for o in objetos:
          if o.x == j and o.y == i:
            contenido = \
            "{emoticon}".\
            format(angulo = o.angulo, tamano_emoticon = o.tamano_emoticon, emoticon = o.emoticon)
        s += "{contenido}".\
          format(alto = self.tamano_celda[0], ancho = self.tamano_celda[1],
                contenido = contenido)
      filas += "{}".format(s)
    tablero = tablero.format(filas)
    self.out.value = tablero
     

class Agente:
  def __init__(self, x=0, y=0, angulo=0, emoticon="🤖", tamano_emoticon=30):
    self.x = x
    self.y = y
    self.angulo = angulo
    self.emoticon = emoticon
    self.tamano_emoticon = tamano_emoticon
    self.energia = 5

  def abajo(self):
    if self.y < 4 : self.y += 1
     

agente = Agente()
basura1 = Agente(2, 2, 0, emoticon="🍂", tamano_emoticon=30)
basura2 = Agente(3, 3, 0, emoticon="🍂", tamano_emoticon=30)
basura3 = Agente(3, 2, 0, emoticon="🍂", tamano_emoticon=30)

objetos = [agente, basura1, basura2, basura3]


escenario = Tablero()

for i in range(agente.energia):
  escenario.dibujar(objetos)
  time.sleep(1)
  agente.abajo()
     