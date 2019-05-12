#!/bin/bash

#Enviando.sh

DIR_TO_CHECK=$PWD/enviar #Directorio que queremos inspeccionar

OLD_STAT_FILE=$PWD/backups/ViejoEnviar.txt #Estado del directorio

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

        actual=$USER
        nActual=$(echo ${actual##*o})
        let nSiguiente=nActual+1
        siguiente=zybo$nSiguiente

        string=$(ping -c 3 $siguiente)

        if [[ $string == *100%\ packet\ loss* ]]
        then
            sshpass -p zybomonitor scp -o StrictHostKeyChecking=no $fichero zybo@monitor:/home/zybo/Documentos/Zybo
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
