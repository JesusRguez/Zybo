#!/bin/bash

while :
do
	./Recibiendo.sh &
#	./Desencriptando.sh & #Simulan el tratamiento del archivo
#	./Trabajando.sh & #Simulan el tratamiento del archivo
	./Cristian.sh & #Este ponerlo solo para hacer el tratamiento del archivo
#	./Enviando.sh &
	./EnviandoCasa.sh & #Este ponerlo solo para trabajar en casa porque tiene la ip y contraseña de mi sobremesa
	sleep 1
done
