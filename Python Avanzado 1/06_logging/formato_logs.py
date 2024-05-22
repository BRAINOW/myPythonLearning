import logging 

logging.basicConfig( #Solo se define una vez
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s", #la "s" indica que la variable es un string
    datefmt="%H:%M:%S" #Nos retorna solo la hora 
) 

nombre = "Paco"
logging.error(f"{nombre} creo el error")

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error critico")

try:
    division = 2/0
except: 
    logging.exception("Division por 0") #Muestra tanto el mensaje como el error ocurrido

"""
21:47:21 - ERROR - Paco creo el error
21:47:21 - WARNING - Log de advertencia
21:47:21 - ERROR - Log de error
21:47:21 - CRITICAL - Log de error critico
21:47:21 - ERROR - Division por 0
"""