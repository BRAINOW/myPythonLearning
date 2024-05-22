import logging 

#Configuramos los niveles del logging
#Creamos un archivo donde se guardaran los logs
#Filemode = esta en "a" por defecto de append, "w" el archivo se sobreescribe en cada corrida
logging.basicConfig( #Solo se define una vez
    level=logging.DEBUG
    , filename="ejemplo_logs.log"
    , filemode="w"
) 

logging.debug("Log de debugging")
logging.info("Log Informativo")
logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error critico")

"""
DEBUG:root:Log de debugging
INFO:root:Log Informativo
WARNING:root:Log de advertencia
ERROR:root:Log de error
CRITICAL:root:Log de error critico
"""
