#!/bin/bash

DIR_TO_CHECK=$PWD/enviar #Directorio que queremos inspeccionar

OLD_STAT_FILE=$PWD/backups/ViejoEnviar.txt #Fichero "hash" con el directorio antiguo

if [ -e $OLD_STAT_FILE ]
then
        OLD_STAT=`cat $OLD_STAT_FILE`
else
        OLD_STAT="nothing"
fi

NEW_STAT=`stat -t $DIR_TO_CHECK`

if [ "$OLD_STAT" != "$NEW_STAT" ]
then
#        echo 'Directory has changed. Do something!'

        #Si ha habido algún cambio en el directorio a inspeccionar te dice esto y aquí podemos hacer lo que sea, por ejemplo el mandar el fichero que queramos a la fpga para que haga lo que tenga que hacer y luego ir haciendo comprobaciones.
        # do whatever you want to do with the directory.
        #Podemos lanzarlo con el comando: watch -n 1 ./Estado.sh y cada segundo, comprobará si ha cambiado el directorio "Ficheros" y en función de eso, podremos programar la fpga o lanzar el scp

        # update the OLD_STAT_FILE

	cd $DIR_TO_CHECK

	n=$(ls | wc -l)
	cero=0

	if [[ n -ne cero ]]
	then
		fichero=$(ls -t | head -1) #Obtenemso el fichero más reciente

		#actual=$USER
		#nActual=$(echo ${actual##*o}) #Cogemos el número de la tarjeta
		#let nSiguiente=nActual+1 #Esto es para el envío secuencial a la siguiente tarjeta

		enviado=0

		while [[ enviado -eq cero ]]
		do

			nSiguiente=$(echo $(($RANDOM%4))) #Esto es para el envio aleatorio entre 3 tarjetas (se pone uno más por ser el módulo)

			if [[ nSiguiente -eq cero  ]] #Si sale 0, lo enviaremos al ordenador central
			then
				sshpass -p 1997 scp -o StrictHostKeyChecking=no $fichero jesus@192.168.1.39:/home/jesus/Vídeos #Estos son los datos de mi casa, ponerlo bien
				enviado=1
				echo He enviado el archivo al ordenador central
			else #Si sale distinto de 0, tendremos que ver si está conectada dicha tarjeta, si no, volver a generar un número
				siguiente=zybo$nSiguiente

				string=$(ping -c 3 $siguiente)
				if [[ $string != *100%\ packet\ loss* ]]
	        	        then
		                        siguienteZybo=$siguiente
	        	                siguienteZybo+=@
	                	        siguienteZybo+=$siguiente
	                        	siguienteZybo+=:/home/
		                        siguienteZybo+=$siguiente
		                        siguienteZybo+=/ficheros/recibir

	        	                sshpass -p $siguiente scp -o StrictHostKeyChecking=no $fichero $siguienteZybo

					enviado=1
					echo He enviado el archivo a $siguiente
		                fi
			fi
		done




		#string=$(ping -c 3 $siguiente)
#Para que tire el ping debemos cambiar los permisos del propio comando porque no
#está hecho por defecto. Hacemos lo siguiente como su: chmod u+s /bin/ping y ya
#nos deja hacer ping como usuarios normales
		#if [[ $string == *100%\ packet\ loss* ]]
		#then
		#	sshpass -p 1997 scp -o StrictHostKeyChecking=no $fichero jesus@192.168.1.39:/home/jesus/Vídeos #Estos son los datos de mi casa, ponerlo bien
#		else
#			siguienteZybo=$siguiente
#			siguienteZybo+=@
#			siguienteZybo+=$siguiente
#			siguienteZybo+=:/home/
#			siguienteZybo+=$siguiente
#			siguienteZybo+=/ficheros/recibir
#
#			sshpass -p $siguiente scp -o StrictHostKeyChecking=no $fichero $siguienteZybo
#		fi
	fi

        echo $NEW_STAT > $OLD_STAT_FILE
fi
