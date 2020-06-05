#!/usr/bin/python
# -- coding: utf-8 --
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
	El programa al ser ejecutado en el terminal, el usuario podra escuchar un sonido similar al de un tono de llamada y en la pantalla  		ver un mensaje de ejecucion.

	El dial tone ("tono de marcación" por su traducción al español) es la señal enviada por una central telefónica a un dispositivo cuando se 		detecta que esta descolgado y listo para realizar una llamada. 

	Los servicios de telefonía celular no generan tonos de marcado, ya que no se realiza ninguna conexión hasta que se haya especificado y 		transmitido el numero completo.

	El Dial Tone presenta variaciones según el lugar, estas son las siguientes:
		* US Dial Tone = Utiliza combinación de una señal de 350 Hz y una de 440 Hz.
		* UK Dial Tone = Utiliza combinación de una señal de 350 Hz y una de 450 Hz.
		* European Dial Tone = Utiliza una única señal de 425 Hz.
		* Japanese Dial Tone = Utiliza una única señal de 400 Hz.
		* Singapore Dial Tone = Utiliza combinación de una señal de 270 Hz y una de 320 Hz.



Parámetros
----------

-O --audio-output:Options = selección del dispositivo de salida.

-r --sample-rate:args = Tasa de muestreo del programa.


produce
-------

Se escucha el tono de marcación estadounidense.

Ejemplo
-------
* Positivo
La ejecución del programa se hace desde el terminal y accediendo a la ubicación del archivo, como se muestra  en el ejemplo

     XXXXX@XXXX:~/Escritorio/microondas/python$ python dial_tone.py 
     gr::log :INFO: audio source - Audio sink arch: alsa
     ^C 
Para finalizar el programa se debe oprimir ctrl+c  (^C)

* valor retornado: 0

referencias
----------
* https://wiki.gnuradio.org/index.php/TutorialsWritePythonApplications
* https://en.wikipedia.org/wiki/Dial_tone
* https://en.wikipedia.org/wiki/Dial_tone#:~:text=The%20modern%20dial%20tone%20varies,a%20modulation%20at%2090%20Hz.
* https://help.genesys.com/pureconnect/mergedprojects/wh_ia/desktop/dial_tone,_busy_and_ringback_signals_by_country.htm

"""

from gnuradio import gr
from gnuradio import audio
from gnuradio.eng_option import eng_option
from optparse import OptionParser

try:
    from gnuradio import analog
except ImportError:
    sys.stderr.write("Error: Program requires gr-analog.\n")
    sys.exit(1)

class my_top_block(gr.top_block):
    """
    Se deriva de otra clase, gr.top_block. Esta clase es básicamente un contenedor para el grafico de flujo. Derivando de gr.top_block, obtienes
    todos los enlaces y funciones que necesitas para agregar bloques y conectarlos.
	
    """

    def __init__(self):
	"""
        Contructor de la clase de my_top_block con el argumento self y servirá para cualquier proceso de inicializacion. En este caso se combina 		la señal de un generador senosoidal con una frecuencia de 350 Hz y la de un generador senosoidal de 440 Hz. Con esta combinación es 		posible obtener el dial tone.
	
	  +------------------------+

	  | Sine generator (350Hz) +---+

	  +------------------------+   |   +------------+
		                       +---+            |

		                           | Audio sink |

		                       +---+            |

	  +------------------------+   |   +------------+

  	  | Sine generator (440Hz) +---+

	  +------------------------+

	
	
	"""

        gr.top_block.__init__(self)

        parser = OptionParser(option_class=eng_option)
        parser.add_option("-O", "--audio-output", type="string", default="",
                          help="pcm output device name.  E.g., hw:0,0 or /dev/dsp")
        parser.add_option("-r", "--sample-rate", type="eng_float", default=48000,
                          help="set sample rate to RATE (48000)")
        (options, args) = parser.parse_args()
        if len(args) != 0:
            parser.print_help()
            raise SystemExit, 1

        sample_rate = int(options.sample_rate)
        ampl = 0.1

        ###################################################################################
	###     Para reproducir diferentes dial tone se debe tener en cuenta que:	###
	###										###
	###     Tipo de Dial tone		f1		f2			###
	###            US                       350             440			###					
	###            UK                       350             450			###
	###         European                     0              425			###
	###         Japanese                     0              400			###
	###         Singapure                   270             320			###
	###										###
	###################################################################################

	f1=350;
	f2=440;

	src0 = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, f1, ampl) 

	# analog.GR_SIN_WAVE = es un tipo de onde la la libreria gr y hace referencia una senosoidal
        src1 = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, f2, ampl)

	# Se crea un sumidero de audio. Los parametros son (Tasa de muestreo, Eleccion del dispositivo para la salida del audio)
        dst = audio.sink(sample_rate, options.audio_output) 
        self.connect(src0, (dst, 0))
        self.connect(src1, (dst, 1))

if __name__ == '__main__':
    try:
        my_top_block().run()
    except KeyboardInterrupt:
        pass
