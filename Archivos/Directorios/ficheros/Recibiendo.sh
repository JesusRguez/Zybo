#!/bin/bash

DIR_TO_CHECK=$PWD/recibir #Directorio que queremos inspeccionar

DIR_TO_SEND=$PWD/desencriptar #Directorio donde enviar

OLD_STAT_FILE=$PWD/backups/ViejoRecibir.txt #Fichero "hash" con el estado del directorio antiguo

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
		cp $fichero $DIR_TO_SEND #Copiamos el fichero a $DIR_TO_SEND
	fi

        echo $NEW_STAT > $OLD_STAT_FILE
fi
