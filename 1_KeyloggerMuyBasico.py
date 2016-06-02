import pyHook, pythoncom

def eventoTeclado(evento):
	print str(evento.Ascii)
	print chr(evento.Ascii)
controlador = pyHook.HookManager()
controlador.KeyDown = eventoTeclado
controlador.HookKeyboard()

pythoncom.PumpMessages()