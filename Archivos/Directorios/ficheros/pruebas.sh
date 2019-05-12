#!/bin/bash

actual=$USER
echo Actual: $actual
nActual=$(echo ${actual##*o})
echo nActual: $nActual
let nSiguiente=nActual+1
echo nSiguiente: $nSiguiente
siguiente=zybo$nSiguiente
echo siguiente: $siguiente

siguienteZybo=$siguiente
siguienteZybo+=@
siguienteZybo+=$siguiente
siguienteZybo+=:/home/
siguienteZybo+=$siguiente
siguienteZybo+=/ficheros/recibir

echo Directorio: $siguienteZybo
