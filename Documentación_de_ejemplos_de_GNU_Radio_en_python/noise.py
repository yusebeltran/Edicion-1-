#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2007 Free Software Foundation, Inc.
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
# 
"""
Reproduce un sonido de ruido

Parameters
----------
-O --audio-output: Descripcion 
-r --sample-rate:  Descripcion

se aplica el método add_option (definido en la clase OptionParser ) para poder seleccionar
la salida de audio y la tasa de muestreo  (si no se definen tomarán los valores por defecto) 
Si al ejecutar el fichero se le añade “-O” o bien “-r”

Returns
-------
gr::log :INFO:
audio source - Audio sink arch: alsa

alsa:  
El sumidero y la fuente de GNU Radio Audio usan ALSA, esta ha sido la API  de sonido
estándar en Linux durante una década más o menos, por lo que básicamente todos los 
programas que producen audio saben cómo manejarlo


produce
-------

Se escucha un ruido..

Ejemplo
-------
Positivo

     system@:~/Documentos/noise2$ python noise.py
     gr::log :INFO: audio source - Audio sink arch: alsa

Negativo

     system@:~/Documentos/noise2$ python noise.py -r 200000
     gr::log :INFO: audio source - Audio sink arch: alsa
     gr::log :INFO: audio_alsa_sink0 - [default]: unable to support sampling rate 200000
     Card requested 192000 instead.
     
     descripción:
     Se cambia el parámetro sample rate a 200000 con -r
     Puesto que se supera la tasa de muestreo que soporta la tarjeta de audio, se toma el valor por defecto.
     
Referencias
----------
* https://numpydoc.readthedocs.io/en/latest/format.html
* https://en.wikipedia.org/wiki/Docstring
* http://bibing.us.es/proyectos/abreproy/11984/fichero/Volumen+8_Anexos%252FAnexos.pdf

Librerías
----------
from gnuradio import gr
    Le dice a Python los módulos a incluir. Siempre se debe tener gr para ejecutar aplicaciones de GNU Radio.

from gnuradio import audio
    El componente de audio gnuradio proporciona los bloques gr audio source y gr audio sink

from gnuradio import digital
    Este es el paquete gr-digital. Contiene todos los bloques de modulación digital, utilidades y ejemplos

from gnuradio.eng_option import eng_option
    Este módulo extiende el módulo Pythons optparser para comprender la notación de ingeniería
 
from optparse import OptionParser
    El módulo optparse es una alternativa moderna para el análisis de opciones de línea de comandos 
"""
from gnuradio import gr
from gnuradio import audio
from gnuradio import digital
from gnuradio.eng_option import eng_option
from optparse import OptionParser


class my_top_block(gr.top_block):
    """
    Esta clase es básicamente un contenedor para el grafo. Al derivar de gr.top_block, 
    se obtienen todos los enlaces y funciones que se necesitan para agregar bloques e interconectarlos.
    """

    def __init__(self):
        """
        Especifíca la primera función que se ejecutará al crear un objeto de la clase
        my_top_block con el argumento self, por lo que servirá para cualquier proceso de inicializacián,
        este se define como el constructor de la clase,la interconexión de los bloques es la siguiente:
          +------------------------+     +------------------------+     +--------------------+
	  |   GLFSR Source          +-----+   Chunks to Symbol bf  +-----+  Audio Sink        |
	  +------------------------+     +------------------------+     +--------------------+
        
        Con gr.top_block.__init__(self) se llama a la función inicial del modulo top_block del
        paquete gr y se pasa como argumento el objeto creado.
        
        digital.glfsr_sorce_b 
             Fuente pseudoaleatoria LFSR de Galois que genera salidas flotantes -1.0 - 1.0

        chunks_to_symbols_bf
             Asigna un flujo de índices de símbolos desempaquetados al flujo de puntos de        
              constelación flotantes o complejos en dimensiones D (D = 1 por defecto).

        audio.sink 
              Este módulo envía las señales a la tarjeta de audio para poder reproducirlas.
        
        
 
        """
        gr.top_block.__init__(self)

        parser = OptionParser(option_class=eng_option)
        parser.add_option("-O", "--audio-output", type="string", default="",
                          help="pcm output device name.  E.g., hw:0,0 or /dev/dsp")
        parser.add_option("-r", "--sample-rate", type="eng_float", default=48000,
                          help="set sample rate to RATE (48000)")
        (options, args) = parser.parse_args ()
        if len(args) != 0:
            parser.print_help()
            raise SystemExit, 1

        """
        Las siguientes instrucciones definen la tasa de muestreo (obtenida de options) y la amplitud
        """
        sample_rate = int(options.sample_rate)
        ampl = 0.1
        
       
        src = digital.glfsr_source_b(32)     # Pseudorandom noise source
        b2f = digital.chunks_to_symbols_bf([ampl, -ampl], 1)
        dst = audio.sink(sample_rate, options.audio_output)
        """
        se debe realizar la conexión entre los bloques que se han definido anteriormente paracompletar el grafo:
        Con esto se crea la conexión logica del grafo uniendo los puertos de entrada y salida 
        (src-fuente y dst-destino).
        """
        self.connect(src, b2f, dst)

if __name__ == '__main__':
    """
    La primera línea sirve para ejecutar el programa directamente, es decir, a través de una
    Terminal con el comando ./noise.py ya que en ese caso la variable __name__ y __main__
    seran iguales y se ejecutara el contenido del bucle.
    """
    try:
        """
        llama a la clase my_top_block y hace que se procese con el metodo run(), 
        para ello se realiza el intento con try y permanece a menos que se genere
        la excepción KeyboardInterrupt (Control+C)
        """
        my_top_block().run()
    except KeyboardInterrupt:
        pass
