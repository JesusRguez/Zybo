# Zybo
Trabajo de Fin de Grado de Jesús Rodríguez Heras, alumno del grado de Ingeniería Informática de la Escuela Superior de Ingeniería de la Universidad de Cádiz.

En este proyecto se ha trabajado en el diseño de una estructura de red que conecta un ordenador con unos nodos cifradores/descifradores basados en tecnología programable ApSoC.Para tal fin, los nodos incluyen un periférico hardware de cifrado/descifrado AES-128 implementado en la lógica programable ApSoC. Cada nodo de la red recibe información del nodo anterior, la descifra, agrega información vuelve a cifrar el conjunto para enviarlo al siguiente nodo. De este modo se recolecta información de todos los nodos de forma colectiva, enviándose al monitor central al finalizar.

Para la conexión de todos los dispositivos de red se han usado cables de red UTP de categoría 5E y un switch TP-Link TL-SG1024D. Se ha desarrollado un conjunto de scripts que automatizan el proceso al completo, encargándose por tanto de la recepción, cifrado/descifrado y envío del conjunto de información mediante el protocolo de comunicación SSH. Este proceso ha sido automatizado con el objetivo de conseguir una mayor independencia del agente humano por parte del sistema.

La red montada para el proceso de test y verificación del sistema, usa un total de tres nodos, sin embargo, el diseño permite aumentar el número de dispositivos en base a las necesidades y capacidades físicas de la red.
