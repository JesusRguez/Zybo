#!/bin/bash

#Automatico.sh

while :
do
	./Recibiendo.sh &
	./Cristian.sh &
	./Enviando.sh &
	sleep 1
done
