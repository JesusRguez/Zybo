#!/bin/bash

while :
do
	./Recibiendo.sh
	./Cristian.sh  #Este script simula el tratamiento del archivo
	sleep 5
	./Enviando.sh
	sleep 1
done
