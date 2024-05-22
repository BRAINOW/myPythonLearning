#un "handler" permite configurar y personalizar los loggers
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler_consola = logging.StreamHandler() 
formato_logs = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler_consola.setFormatter(formato_logs)

#Definimos el logger al que pertenece
logger.addHandler(handler_consola)

handler_archivo = logging.FileHandler(filename="archivo.log")
handler_archivo.setLevel(logging.ERROR) #Solo va a escribir en el archivo a partir del nivel de "ERROR"
handler_archivo.setFormatter(formato_logs)

logger.addHandler(handler_archivo)

logger.info("Registro informativo")
