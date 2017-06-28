class Mascota(object):
    def __init__ (self, nombre):
        self.nombre = nombre

    def obtener_nombre(self):
        return '{nombre}'.format(
            nombre=self.nombre
            )

class MascotaPerro(Mascota):
    def __init__(self, raza ):
       super(Mascota,self).__init__(nombre)
       self.nombre = nombre
    def obtener_nombre(self):
        return self.nombre
       self.raza = raza
    def obtener_raza(self):
        return self.raza

class MascotaGato(Mascota):
    def __init__(self, raza ):
        self.raza = raza
    def obtener_raza(self):
        return self.raza

if __name__ == '__main__':
    perro = MascotaPerro('pitbull')
    perro_dos = MascotaPerro('pastor aleman')

    print 'Raza:'
    print perro.obtener_raza()
    print perro_dos.obtener_raza()

    print 'Nombres:'
    print perro.obtener_nombre()

