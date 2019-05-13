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
		#echo $fichero
#		echo Copiado el fichero $fichero a Monitor

		actual=$USER
#		echo Actual: $actual
		nActual=$(echo ${actual##*o})
#		echo nActual: $nActual
		let nSiguiente=nActual+1
#		echo nSiguiente: $nSiguiente
		siguiente=zybo$nSiguiente
#		echo siguiente: $siguiente

		string=$(ping -c 3 $siguiente)
#Para que tire el ping debemos cambiar los permisos del propio comando porque no
#está hecho por defecto. Hacemos lo siguiente como su: chmod u+s /bin/ping y ya
#nos deja hacer ping como usuarios normales
		if [[ $string == *100%\ packet\ loss* ]]
		then
			sshpass -p zybomonitor scp -o StrictHostKeyChecking=no $fichero zybo@monitor:/home/zybo/Vídeos #Estos son los datos de mi casa, ponerlo bien
		else
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
