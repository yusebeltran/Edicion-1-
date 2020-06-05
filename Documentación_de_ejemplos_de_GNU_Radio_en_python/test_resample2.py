# -*- coding: utf-8 -*-
#! /usr/bin/python2
#
# Copyright 2004,2005,2007,2012 Free Software Foundation, Inc.
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
RESUMEN
---------------------------------------------------------------------
al ejecutar el programa se escucha un ruido pseudo aleatorio hasta que se detiene el programa tambien se visuaiza la interpolacion y decimacion del bloque rational resampler 

PARAMETROS
---------------------------------------------------------------------
-i input: señal de entrada con una tasa de muestreo por defecto(8000)
-O output: señal de salida para audio con tasa de muestreo
-o output: señal de salida por defecto (48000)

RETORNA
---------------------------------------------------------------------
interp = 6
decim  = 1
gr::log :INFO: audio source - Audio sink arch: alsa

valor retornado: 0

EJEMPLO
---------------------------------------------------------------------
Positivo

python test_resample.py
interp = 6
decim  = 1
gr::log :INFO: audio source - Audio sink arch: alsa
 
-echo --$? test_resampler\ \(1\).py
0 test_resampler (1).py

    andres@andres:~/Documentos$ python test_resample.py -i 16000 -o 32000
    interp = 2
    decim  = 1
    gr::log :INFO: audio source - Audio sink arch: alsa

andres@andres:~/Documentos$ python test_resample.py -i 48000 -o 48000
interp = 1
decim  = 1
gr::log :INFO: audio source - Audio sink arch: alsa

Candres@andres:~/Documentos$ python test_resample.py -i 20000 -o 30000
interp = 3
decim  = 2
gr::log :INFO: audio source - Audio sink arch: alsa
 

NOTAS
---------------------------------------------------------------------
lo primero que hace el código es importar los módulos necesarios
Los dos módulos más importantes aquí son  gr  y  audio . El primero contiene la clase de bloque superior para implementar nuestro diagrama de flujo y los bloques de procesamiento de señal para nuestra fuente, el segundo contiene un bloque de sumidero para enviar una forma de onda de audio a la tarjeta de sonido de nuestra computadora

REFERENCIAS
--------------------------------------------------------------------
* https://numpydoc.readthedocs.io/en/latest/format.html
* https://en.wikipedia.org/wiki/Docstring

"""

from gnuradio import gr, gru
from gnuradio import audio
from gnuradio import filter
from gnuradio.eng_option import eng_option
from optparse import OptionParser

try:
    from gnuradio import analog
except ImportError:
    sys.stderr.write("Error: Program requires gr-analog.\n")
    sys.exit(1)

try:
    from gnuradio import blocks
except ImportError:
    sys.stderr.write("Error: Program requires gr-blocks.\n")
    sys.exit(1)

class my_top_block(gr.top_block):
    """
    Define una clase llamada "my_top_block" que se deriva de otra clase, gr.top_block.
    Esta clase es basicamente un contenedor para el grafo. Al derivar de gr.top_block, 
    obtenemos todos los enlaces y funciones que necesitamos para agregar bloques e interconectarlos.
	El siguiente fragmento de código simplemente verifica para asegurarse de que el usuario no haya agregado la entrada de la línea de comandos sin relación con las opciones disponibles.
 
	Las siguientes instrucciones definen la tasa de muestreo (obtenida de options) y la amplitud

	retorna los datos de interpolacion y estimacion calculados

	src es una fuente de datos una onda sinusoidal generada por la computadora

	Finalmente, con : self.connect(src0, rr, (dst, 0))conectamos los bloques que hemos definido juntos para completar nuestra aplicación:

	    +------------------------+     +------------------------+     +--------------------+
	    |   Signal Source 0      +-----+  rational resampler    +-----+  Audio Sink 0      |
	    +------------------------+     +------------------------+     +--------------------+
    """
    def __init__(self):
	"""
        Con gr.top_block.__init__(self) se llama a la funcion inicial del modulo top_block del
        paquete gr y se pasa como argumento el objeto creado.

	A continuación, podemos agregar diferentes PARAMETROS que el usuario puede especificar en la línea de comando 

	La siguiente línea: (options, args) = parser.parse_args(), se utiliza para analizar la entrada del usuario y proporcionarla en un formato fácil de usar
        """
        gr.top_block.__init__(self)
        parser = OptionParser(option_class=eng_option)
        parser.add_option("-O", "--audio-output", type="string", default="",
                          help="pcm output device name.  E.g., hw:0,0 or /dev/dsp")
        parser.add_option("-i", "--input-rate", type="eng_float", default=8000,
                          help="set input sample rate to RATE (%default)")
        parser.add_option("-o", "--output-rate", type="eng_float", default=48000,
                          help="set output sample rate to RATE (%default)")
        (options, args) = parser.parse_args()

        if len(args) != 0:
	
 

            parser.print_help()
            raise SystemExit, 1
        input_rate = int(options.input_rate)
        output_rate = int(options.output_rate)

        interp = gru.lcm(input_rate, output_rate) / input_rate
        decim = gru.lcm(input_rate, output_rate) / output_rate

        print "interp =", interp
        print "decim  =", decim
        ampl = 0.1
        src0 = analog.sig_source_f(input_rate, analog.GR_SIN_WAVE, 650, ampl)
        rr = filter.rational_resampler_fff(interp, decim)
        dst = audio.sink(output_rate, options.audio_output)
	self.connect(src0, rr, (dst, 0))

if __name__ == '__main__':
    """
	
	La primera linea sirve para ejecutar el programa directamente, es decir, a traves de una
    Terminal con el comando ./test_resampler.py ya que en ese caso la variable __name__ y __main__
    seran iguales y se ejecutara el contenido del bucle.

	Ambos crean una instancia de nuestro bloque superior personalizado usando  my_top_block() y comienzan a ejecutarla llamando  al método  run () de top_block, para ello se realiza el intento con try y permanece a menos que se genere la excepcion KeyboardInterrupt (Control+C)

    """
    try:

        my_top_block().run()
    except KeyboardInterrupt:
        pass
