segundos = float (input('Segudos?'))
dias = segundos // 86400
horas = segundos // 3600
segundos_sobra = segundos / 3600
minutos = segundos_sobra // 60 
segundos_final = segundos_sobra % 3600
if(horas >= 24):
    dias = int(horas // 24)
    horas = int(horas % 24)

print (dias, 'dias', horas, 'horas', minutos, 'minutos', 'e', segundos_final, 'segundos.')