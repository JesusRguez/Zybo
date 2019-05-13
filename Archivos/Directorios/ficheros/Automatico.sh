#!/bin/bash

while :
do
	./Recibiendo.sh 
#	./Desencriptando.sh & #Simulan el tratamiento del archivo
#	./Trabajando.sh & #Simulan el tratamiento del archivo
	./Cristian.sh  #Este ponerlo solo para hacer el tratamiento del archivo
#	./Enviando.sh & #Este ponerlo para el envío secuencial
	./EnviandoCasa.sh  #Este ponerlo solo para trabajar en casa porque tiene la ip y contraseña de mi sobremesa
#	./EnviandoRandom.sh & #Este ponerlo para el envío random
	sleep 1
done
