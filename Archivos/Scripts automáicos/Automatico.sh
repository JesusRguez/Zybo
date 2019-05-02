#!/bin/bash

while :
do
	./Recibiendo.sh &
#	./Desencriptando.sh & #Simulan el tratamiento del archivo
#	./Trabajando.sh & #Simulan el tratamiento del archivo
	./Cristian.sh & #Este ponerlo solo para hacer el tratamiento del archivo
	./Enviando.sh &
	sleep 1
done
