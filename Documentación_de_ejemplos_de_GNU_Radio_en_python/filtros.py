#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2013 Free Software Foundation, Inc.
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
Este programa lo que busca crear y generar es un filtro FIR el cual tiene una respuesta
finita al impulso.

Tener en cuenta
-----------------

Verificar la version de phyton.

Es necesario realizar las descargas de los siguientes programas: Matplotlab y Scipy 
los cuales son complementos para Phyton.

Parámetros
----------

-N = numero de muestras.
-S = frecuencia de muestreo.
-B = ancho de banda 
-T = Transicion.
-A = Atenuación
-D = Decimación

Retorna
-------

ejecutar el programa : `python f.py`

Dos graficas.

1) grafica de ruido blanco

2) filtro pasabanda

Ejemplo
-------
Positivo

1) variacion del ancho de banda 

 parser = OptionParser(option_class=eng_option, conflict_handler="resolve")
    parser.add_option("-N", "--nsamples", type="int", default=10000,
                      help="Number of samples to process [default=%default]")
    parser.add_option("-s", "--samplerate", type="eng_float", default=8000,
                      help="System sample rate [default=%default]")
    parser.add_option("-B", "--bandwidth", type="eng_float", default=2000,
                      help="Filter bandwidth [default=%default]")
    parser.add_option("-T", "--transition", type="eng_float", default=100,
                      help="Transition band [default=%default]")
    parser.add_option("-A", "--attenuation", type="eng_float", default=80,
                      help="Stopband attenuation [default=%default]")
    parser.add_option("-D", "--decimation", type="int", default=1,
                      help="Decmation factor [default=%default]")

2) aumentar el numero de muestras

 parser = OptionParser(option_class=eng_option, conflict_handler="resolve")
    parser.add_option("-N", "--nsamples", type="int", default=20000,
                      help="Number of samples to process [default=%default]")
    parser.add_option("-s", "--samplerate", type="eng_float", default=8000,
                      help="System sample rate [default=%default]")
    parser.add_option("-B", "--bandwidth", type="eng_float", default=1000,
                      help="Filter bandwidth [default=%default]")
    parser.add_option("-T", "--transition", type="eng_float", default=100,
                      help="Transition band [default=%default]")
    parser.add_option("-A", "--attenuation", type="eng_float", default=80,
                      help="Stopband attenuation [default=%default]")
    parser.add_option("-D", "--decimation", type="int", default=1,
                      help="Decmation factor [default=%default]")


Negativo

1) no se puede varias la frecuencia de muestreo

parser = OptionParser(option_class=eng_option, conflict_handler="resolve")
    parser.add_option("-N", "--nsamples", type="int", default=10000,
                      help="Number of samples to process [default=%default]")
    parser.add_option("-s", "--samplerate", type="eng_float", default=1000,
                      help="System sample rate [default=%default]")
    parser.add_option("-B", "--bandwidth", type="eng_float", default=1000,
                      help="Filter bandwidth [default=%default]")
    parser.add_option("-T", "--transition", type="eng_float", default=100,
                      help="Transition band [default=%default]")
    parser.add_option("-A", "--attenuation", type="eng_float", default=80,
                      help="Stopband attenuation [default=%default]")
    parser.add_option("-D", "--decimation", type="int", default=1,
                      help="Decmation factor [default=%default]")

2) no se puede variar la decimación

parser = OptionParser(option_class=eng_option, conflict_handler="resolve")
    parser.add_option("-N", "--nsamples", type="int", default=10000,
                      help="Number of samples to process [default=%default]")
    parser.add_option("-s", "--samplerate", type="eng_float", default=1000,
                      help="System sample rate [default=%default]")
    parser.add_option("-B", "--bandwidth", type="eng_float", default=1000,
                      help="Filter bandwidth [default=%default]")
    parser.add_option("-T", "--transition", type="eng_float", default=100,
                      help="Transition band [default=%default]")
    parser.add_option("-A", "--attenuation", type="eng_float", default=80,
                      help="Stopband attenuation [default=%default]")
    parser.add_option("-D", "--decimation", type="int", default=5,
                      help="Decmation factor [default=%default]")


referencias
----------

https://www.python.org/downloads/
https://scipy-cookbook.readthedocs.io/items/FIRFilter.html
https://scipy-cookbook.readthedocs.io/items/ApplyFIRFilter.htmlue 
https://matplotlib.org/users/installing.html#installing-an-official-release

----------

"""
from gnuradio import gr, filter
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio.eng_option import eng_option
from optparse import OptionParser
import sys  # El módulo provee acceso a funciones y objetos

try:
    import scipy   # El Spicy es un paquete para uso en rutinas cientificas de Phyton
except ImportError:      # Se genera cuando una instrucción tiene problemas para importar con éxito el módulo especificado.
    print "Error: could not import scipy (http://www.scipy.org/)"
    sys.exit(1)    # Permite terminar la ejecución del script devolviendo un valor si termina bien, retornando o si se tuvieron algún problema

try:
    import pylab
except ImportError:
    print "Error: could not import pylab (http://matplotlib.sourceforge.net/)"
    sys.exit(1)

class example_fir_filter_ccc(gr.top_block): 
    """ 

    Constructor principal de Python.
    
                                 
    """

    def __init__(self, N, fs, bw, tw, atten, D):
        """
        Nombre de la funcion donde se implementaran las opraciones y 
        contendra todas las variables del programa, basicamente seria 
        el contenedor del programa.

        """

        gr.top_block.__init__(self)

        self._nsamps = N
        self._fs = fs
        self._bw = bw
        self._tw = tw
        self._at = atten
        self._decim = D
        taps = filter.firdes.low_pass_2(1, self._fs, self._bw, self._tw, self._at)
        print "Num. Taps: ", len(taps)

        self.src  = analog.noise_source_c(analog.GR_GAUSSIAN, 1)
        self.head = blocks.head(gr.sizeof_gr_complex, self._nsamps)

        self.filt0 = filter.fir_filter_ccc(self._decim, taps)

        self.vsnk_src = blocks.vector_sink_c()
        self.vsnk_out = blocks.vector_sink_c()

        self.connect(self.src, self.head, self.vsnk_src)
        self.connect(self.head, self.filt0, self.vsnk_out)


def main():
    """

    Estas intrucciones que estan acontinuacion determinan los
    valores de y el tipo (define valores) de cada proceso realizado.

    """
    parser = OptionParser(option_class=eng_option, conflict_handler="resolve")
    parser.add_option("-N", "--nsamples", type="int", default=10000,
                      help="Number of samples to process [default=%default]")
    parser.add_option("-s", "--samplerate", type="eng_float", default=8000,
                      help="System sample rate [default=%default]")
    parser.add_option("-B", "--bandwidth", type="eng_float", default=1000,
                      help="Filter bandwidth [default=%default]")
    parser.add_option("-T", "--transition", type="eng_float", default=100,
                      help="Transition band [default=%default]")
    parser.add_option("-A", "--attenuation", type="eng_float", default=80,
                      help="Stopband attenuation [default=%default]")
    parser.add_option("-D", "--decimation", type="int", default=1,
                      help="Decmation factor [default=%default]")
    (options, args) = parser.parse_args ()

    put = example_fir_filter_ccc(options.nsamples,
                                 options.samplerate,
                                 options.bandwidth,
                                 options.transition,
                                 options.attenuation,
                                 options.decimation)
    put.run()

    data_src = scipy.array(put.vsnk_src.data())
    data_snk = scipy.array(put.vsnk_out.data())

    # Plot the signals PSDs
    nfft = 1024
    f1 = pylab.figure(1, figsize=(12,10))
    s1 = f1.add_subplot(1,1,1)
    s1.psd(data_src, NFFT=nfft, noverlap=nfft/4,
           Fs=options.samplerate)
    s1.psd(data_snk, NFFT=nfft, noverlap=nfft/4,
           Fs=options.samplerate)

    f2 = pylab.figure(2, figsize=(12,10))
    s2 = f2.add_subplot(1,1,1)
    s2.plot(data_src)
    s2.plot(data_snk.real, 'g')

    pylab.show()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass

