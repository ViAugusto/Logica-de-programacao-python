total = int(input("Por favor, entre com o número de segundos que deseja converter: "))


dias = total // 86400
seg_rest = total % 86400
horas = seg_rest // 3600
segrest = total % 3600
minutos = segrest // 60
final = segrest % 60

print (dias, "dias, ", horas, "horas, ", minutos, "minutos e", final, "segundos.")
