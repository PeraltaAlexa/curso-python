import argparse
if __name__ =='__main__':
	parser=argparse.ArgumentParser()
	parser.add_argument('nombre')
	parser.add_argument('apellido')
	parser.add_argument('curso')
	parser.add_argument('edad')

	args = parser.parse_args()
	Estudiante={
	    'nombre':args.nombre,
	    'apellido':args.apellido,
	    'curso':args.curso,
	    'edad': args.edad,

	}
	for llave,valor in Estudiante.iteritems():
		print llave,valor
