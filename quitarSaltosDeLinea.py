-*- coding: utf-8 *-*
originalFile = raw_input("Introduce aquí el nombre del fichero del que quieres eliminar los saltos de línea\n>>> ")
newFile = raw_input("Escribe aquí el nombre del nuevo fichero que se creará sin saltos de línea\n>>> ")

inputFile = open(originalFile, 'r')
outputFile = open(newFile, 'w')

while True:
	charac = inputFile.read(1)
	if charac == '': break
	elif charac == '\n': pass
	else: outputFile.write(charac)

inputFile.close()
outputFile.close()
