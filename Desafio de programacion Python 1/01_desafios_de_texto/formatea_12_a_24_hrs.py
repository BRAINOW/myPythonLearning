def formatoMilitar(text):

    text = text.lower() #Pasamos todo a minuscula

    if "pm" in text: #En caso de ser pm
        if text[0:2] == "12": 
            #Si son las 12 retornamos la hora si el sufijo
            return text[:-2]
        else:
            hora = int(text[0:2]) #obtenemos las horas
            hora = 12 + hora #Aumentamos en 12 las horas
            return str(hora) + text[2:5] #Concatenamos la hora con los minutos sin sufijo
        
    elif "am" in text: #En caso de ser "am"
        if text[0:2] == "12": 
            #Si son las "12 am" lo remplazamos por "00"
            return "00" + text[2:5]
        else:
            #Si es "am" y antes de las 12 retornamos la hora sin el sufijo
            return text[0:5]
        
    else: 
        return None
    
print(formatoMilitar("12:40 AM"))
print(formatoMilitar("12:40 PM"))
print(formatoMilitar("10:30 AM"))
print(formatoMilitar("04:59 PM"))


#########################Solucion del curso #########################
print("\n\n\n")

def convertir_horario(hora):
    hora_lista = hora.split(":") #Separamos la hora por ":"
    if hora[-2:].lower() == "pm": #En casp de qie los dos ultimos caracteres sean "pm"
        if hora_lista[0] != "12": #Si es diferente de "12" unicamente
            hora_lista[0] = str(int(hora_lista[0])+12) #Anadimos 12 horas a la hora
    else:
        if hora_lista[0] == "12": #Si no es "pm" pero son las "12 am" cambiamos las horas a "00"
            hora_lista[0] = "00"

    hora_convertida = ":".join(hora_lista) #unimos la lista con ":" entre cada elemento
    return hora_convertida[:-2] #Retornamos la lista menos los dos ultimos caracteres

print(convertir_horario("12:40 AM"))
print(convertir_horario("12:40 PM"))
print(convertir_horario("10:30 AM"))
print(convertir_horario("04:59 PM"))

#####################################################################