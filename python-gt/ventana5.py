import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def __init__(self, *args, **Kwargs):
		super(MiVentana, self).__init__(*args, **Kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event', Gtk.main_quit)

  		self.agregar_texto()
    		self.agregar_boton()
		self.agregar_contenedor()
		self.agregar_entrada()




	def agregar_lista(self):
		self.modelo = Gtk.ListStore(str, float)
  		self.lista_activos = Gtk.TreeView(self.modelo)
    		descripcion = Gtk.CellRendererText()
      		columna_descripcion = Gtk.TreeViewColumn(
      		    'Descripcion',
            	descripcion,
             	text=0
      		)
		monto = Gtk.CellRendererText()
  		columna_monto = Gtk.TreeViewColumn('Monto', monto, text=1)

		self.lista_activos.append_column(columna_descripcion)
		self.lista_activos.append_column(columna_monto)

		self.agregar_contenedor.attach_next_to(
		self.lista_activos,
		self.boton,
		Gtk.PositionType.BOTTOM,
		1,
		1

		)

	def agregar_fila(self, btn):
     		texto = self.entrada.get_text()
       		self.modelo.append([texto, 1.5])



	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
  		self.entrada_monto = Gtk.Entry()

		self.agregar_contenedor.attach(self.entrada, 0, 0, 2, 1)
             	self.agregar_contenedor.attach_next_to(
		self.entrada_monto,
		self.entrada,
		Gtk.PositionType.RIGHT,
  		1,
		1
             	)

	def agregar_fila(self, btn):
     		texto= self.entrada.get_text()
		monto = self.entrada_monto.get_text()
		self.modelo.append([texto, float(monto)])

	def agregar_texto(self):
		self.texto = Gtk.Entry()
	def agregar_label(self):
		self.label_1 = Gtk.Label('mostrar el texto')
	def agregar_salida(self):
		self.btnexit = Gtk.Button('finalizar')
		self.btnexit.connect('clicked',Gtk.main_quit)
	def agregar_contenedor(self):
		self.box = Gtk.VBox()
		self.box.pack_start(self.texto, True, False, 0)
		self.box.pack_start(self.boton, True, False, 0)
		self.box.pack_start(self.label_1, True, False,0)
		self.box.pack_start(self.btnexit, True, False,0)
  	def agregar_boton(self):
		self.boton = Gtk.Button('Agregar')
		self.agregar_contenedor.attach_next_to(
		self.boton,
		self.entrada,
		Gtk.PositionType.BOTTOM,
		1,
		1

		)

  		self.boton.connect('clicked', self.agregar_fila)

if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()

	Gtk.main()
