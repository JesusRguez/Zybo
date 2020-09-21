#!/bin/bash

DIR_TO_CHECK=$PWD/desencriptar #Directorio que queremos inspeccionar

DIR_TEMP=$PWD/trabajar #Directorio temporal de trabajo

DIR_TO_SEND=$PWD/enviar #Directorio donde enviar

OLD_STAT_FILE=$PWD/backups/ViejoTrabajar.txt #Fichero "hash" con el estado del directorio antiguo

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
		cp $fichero $DIR_TEMP #Copiamos el fichero a $DIR_TEMP
		cd $DIR_TEMP #Entramos en $DIR_TEMP
		tarjeta=$(cat /etc/passwd | cut -d : -f1 | grep zybo)
		echo 'Archivo tratado en '$tarjeta >> $fichero #Actualizamos el coontenido del fichero
		cp $fichero $DIR_TO_SEND #Copiamos el fichero a $DIR_TO_SEND
	fi

        echo $NEW_STAT > $OLD_STAT_FILE
fi
