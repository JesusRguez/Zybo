#!/bin/bash

#Inicio.sh

direcciones=(192.168.1.11 192.168.1.12 192.168.1.13 192.168.1.14)
tarjetas=(zybo1 zybo2 zybo3 zybo4)
a=0
for d in "${direcciones[@]}"
do
	if [[ $1 = "-v" ]]; then
		echo Comprobando la conexión con ${tarjetas[a]}.
		ping -c 4 $d
	else
		echo Comprobando la conexión con ${tarjetas[a]}.
		string=$(ping -c 4 $d)
		if [[ $string == *100%\ packet\ loss* ]]; then
			echo Tarjeta ${tarjetas[a]} desconectada. Compruebe la conexión.$'\n'
		else
			echo Tarjeta ${tarjetas[a]} conectada.$'\n'
		fi
	fi
	let a=a+1
done
