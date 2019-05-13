#!/bin/bash

DIR_TO_CHECK=$PWD/recibir #Directorio que queremos inspeccionar

DIR_TO_SEND=$PWD/desencriptar #Directorio donde enviar

OLD_STAT_FILE=$PWD/backups/ViejoRecibir.txt #Fichero "hash" con el directorio antiguo

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
#		echo Copiado el fichero $fichero a $DIR_TO_SEND
		cp $fichero $DIR_TO_SEND
	fi

        echo $NEW_STAT > $OLD_STAT_FILE
fi
