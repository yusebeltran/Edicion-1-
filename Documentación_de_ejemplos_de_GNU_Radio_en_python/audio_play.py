#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright 2004,2005,2007 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

"""
Reproduce un audio con extensión '.wav' que se le proporcione
a la tasa de muestreo que se ajuste en 'sample_rate'.

Parámetros
-------------------------

-F --file-name: audio.wav
-r --sample-rate: 44100
-R --repeat

Para consultar la tasa de muestreo se digita el siguiente comando en la terminal:

file audio.wav
audio.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, stereo 48000 Hz

No se entiende si tiene tasa de muestreo inferior

gonzalo@gonzalo-X455LJ:~/Documentos/Microondas$ file audio.wav

En nuestro caso, el audio tiene una tasa de muestreo de "48000Hz"
audio.wav: RIFF (little-endian) data, WAVE audio, Microsoft PCM, 16 bit, stereo 48000Hz


Retorna
-------------------------

* Ejecutar el programa: './audio_play.py -F audio.wav -r 48000'
* Valor retornado: ::log :INFO: audio source - Audio sink arch: alsa

IMPORTANTE: Antes de ejecutar el programa se debe digitar el siguiente comando en la terminal:
gonzalo@gonzalo-X455LJ:~/Documentos/Microondas$ chmod +x audio_play.py

Produce
-------------------------

Comienza a reproducir el archivo "audio.wav" que se le indica.

Ejemplo
-------------------------

Positivo


Para ejecutar el programa se debe digitar en la terminal:

jorge@jorge-ENVY-15:~/Documentos/audio-py$ ./audio_play.py -F audio.wav -r 48000gr
::log :INFO: audio source - Audio sink arch: alsa

jorge@jorge-ENVY-15:~/Documentos/audio-py$ echo $?
0

El valor retornado a "echo" es 0, lo que indica que el programa se ejecutó sin problemas. 

Negativo

Este programa compila unicamente en python3, si se ejecuta con python2, mostrará el siguiente error:

gonzalo@gonzalo-X455LJ:~/Documentos/Microondas$ ./audio_play.py -F audio.wav -r 48000
Traceback (most recent call last):
  File "./audio_play.py", line 22, in <module>
    from gnuradio import gr 
ImportError: No module named gnuradio

gonzalo@gonzalo-X455LJ:~/Documentos/Microondas$ echo $?
130

El valor retornado a "echo" es 130, lo que indica que el programa no se ejecutó bien. 

Otro error que se presenta es en la sintaxis del codigo, que orginalmente viene para python2 pero que usa 
librerias de python3, entonces se debe quitar ", 1" como se muestra en el error a continuación:

gonzalo@gonzalo-X455LJ:~/Documentos/Microondas$ python3 audio_play.py
  File "audio_play.py", line 126
    raise SystemExit, 1 
                    ^
SyntaxError: invalid syntax


referencias
-----------

* https://wiki.gnuradio.org/index.php/Guided_Tutorial_GNU_Radio_in_Python
* https://wiki.gnuradio.org/index.php/TutorialsWritePythonApplications


1.Importación de bibliotecas
----------------------------

1.1. import gr: Biblioteca importada para ejecutar aplicaciones de GNU radio en python.
1.2. import audio: Bilioteca que incluyen los modulos de audio.
1.3. import blocks: Biblioteca necesaria para usar los bloques de GNU, como por ejemplo my_top_block.
1.4. from gnuradio.eng_option import eng_option: Se usa para extender el modulo optparse para comprender la notación de ingeniería.
1.5. from optparse import OptionParser: Permite especificar opciones en la sintaxis de GNU.
"""

from gnuradio import gr 
from gnuradio import audio 
from gnuradio import blocks 
from gnuradio.eng_option import eng_option
from optparse import OptionParser

class my_top_block(gr.top_block):

    """
    Define una clase con el nombre my_top_block que proviene de otra clase con el nombre gr.top_block. Esta clase es básicamente un 
    contenedor para el gráfico de flujo. Al derivar de gr.top_block, obtenemos todos los enlaces y funciones que necesitamos para agregar bloques e interconectarlos.
    """

    def __init__(self): 
        """       
        Es una biblioteca más conveniente, flexible y poderosa para analizar opciones de línea de comandos que el getoptmódulo anterior. Utiliza un 
        estilo más declarativo de análisis de línea de comando: crea una instancia de OptionParser, la llena con opciones y analiza la línea de comando. 

        Permite a los usuarios especificar opciones en la sintaxis convencional de GNU / POSIX, y además genera mensajes de uso y ayuda para usted. En la 
        terminal al ejecutar, se puede escoger las diferentes opciones tecleando -F, -r, -R, -O, cada uno con las funciones que se indican en la función.

        sample_rate: Define el sample_rate con el numero de muestras del add option
        """
        gr.top_block.__init__(self)
        
        parser = OptionParser(option_class=eng_option)


        parser.add_option("-F", "--filename", type="string", default="audio.dat", 
                          help="read input from FILE")
        parser.add_option("-r", "--sample-rate", type="eng_float", default=48000,#El valor de sample rate es de 48000(Tasa de muestras)
                          help="set sample rate to RATE (48000)")
        parser.add_option("-R", "--repeat", action="store_true", default=False)
        parser.add_option("-O", "--audio-output", type="string", default="",
                          help="pcm output device name.  E.g., hw:0,0 or /dev/dsp")

        (options, args) = parser.parse_args()
        if len(args) != 0:
            parser.print_help() 
            raise SystemExit #Hice un cambio, se quitó ", 1"

        sample_rate = int(options.sample_rate)
        src = blocks.file_source (gr.sizeof_float, options.filename, options.repeat)
        dst = audio.sink (sample_rate, options.audio_output)

        self.connect(src, dst)
        """
        La sintaxis general para conectar bloques es self.connect (bloque1, bloque2, bloque3, ...) que conectaría la salida del bloque1 con 
        la entrada del bloque2, la salida del bloque2 con la entrada del bloque3 y así sucesivamente. Podemos conectar tantos bloques como queramos con 
        una llamada connect (). Sin embargo, esto solo funciona cuando hay una correspondencia uno a uno. Los bloques conectados quedarían de la siguiente forma:

                     +---------+       +------------+
                     | Source  +-------+ audio.sink +
                     +---------+       +------------+  
        """

if __name__ == '__main__':
    try:                         
        my_top_block().run()    
    except KeyboardInterrupt:    
        pass
