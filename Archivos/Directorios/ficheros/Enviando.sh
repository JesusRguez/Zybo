#!/bin/bash

DIR_TO_CHECK=$PWD/enviar #Directorio que queremos inspeccionar

OLD_STAT_FILE=$PWD/backups/ViejoEnviar.txt #Fichero "hash" con el estadod del directorio antiguo

if [ -e $OLD_STAT_FILE ]
then
        OLD_STAT=`cat $OLD_STAT_FILE`
else
        OLD_STAT="nothing"
fi

NEW_STAT=`stat -t $DIR_TO_CHECK`

if [ "$OLD_STAT" != "$NEW_STAT" ]
then
	cd $DIR_TO_CHECK

	n=$(ls | wc -l)
	cero=0

	if [[ n -ne cero ]]
	then
		fichero=$(ls -t | head -1) #Obtenemos el fichero más reciente
		#echo Copiando el fichero al monitor
		actual=$(cat /etc/passwd | cut -d : -f1 | grep zybo)
		nActual=$(echo ${actual##*o})
		let nSiguiente=nActual+1
		siguiente=zybo$nSiguiente

		string=$(ping -c 3 $siguiente)
		#Comprobamos la conectivdad al siguiente nodo de la red
		if [[ $string == *100%\ packet\ loss* ]]
		then
			#Si no hay conexión, enviamos el fichero al ordenador central
			sshpass -p 1997 scp -o StrictHostKeyChecking=no $fichero jesus@monitor:/home/jesus/Vídeos
		else
			#Si hay conexión, enviamos el fichero al siguiente nodo de la red
			siguienteZybo=$siguiente
			siguienteZybo+=@
			siguienteZybo+=$siguiente
			siguienteZybo+=:/home/
			siguienteZybo+=$siguiente
			siguienteZybo+=/ficheros/recibir

			sshpass -p $siguiente scp -o StrictHostKeyChecking=no $fichero $siguienteZybo
		fi
	fi

        echo $NEW_STAT > $OLD_STAT_FILE
fi
