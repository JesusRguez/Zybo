#!/bin/bash

#Cristian.sh

DIR_TO_CHECK=$PWD/desencriptar #Directorio que queremos inspeccionar

DIR_TEMP=$PWD/trabajar #Directorio temporal para trabajar

DIR_TO_SEND=$PWD/enviar #Directorio donde enviar

OLD_STAT_FILE=$PWD/backups/ViejoTrabajar.txt #Estado del directorio

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
        cp $fichero $DIR_TEMP
        cd $DIR_TEMP
        tarjeta=$(cat /etc/passwd | cut -d : -f1 | grep zybo)
        echo 'Archivo tratado en '$tarjeta >> $fichero
        cp $fichero $DIR_TO_SEND
    fi
    echo $NEW_STAT > $OLD_STAT_FILE #Actualiza el estado del directorio
fi
