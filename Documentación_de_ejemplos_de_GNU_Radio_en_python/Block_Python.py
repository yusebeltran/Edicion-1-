"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""
# SE IMPORTAN LAS LIBRERIAS PARA LA REALIZACION DEL PROCESO.
import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, example_param=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            # EN ESTE APARTADO SE TIENEN LOS PARAMETROS DE LA CAJA PARA TRABAJAR
            name='Embedded Python Block',   # EN ESTA LINEA SE LA ASIGNA NOMBRE A LA CAJA
            in_sig=[np.complex64],          # EN ESTA LINEA SE OBTIENE LA SEÑAL DE ENTREDA
            out_sig=[np.complex64]          # EN ESTA LINEA SE OBTIENE LA SEÑAL DE SALIDA 
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.example_param = example_param  # EN ESTA LINEA SE OBTIENE EL PARAMETRO DE GANANCIA
                                            # O CONSTANTE QUE SE MULTIPLICA POR LA SEÑAL DE ENTREDA 

    def work(self, input_items, output_items):
        """AQUI SE REALIZA LA ACCION LA CAUL ES MULTIPLICAR LA SEÑAL DE ENTRADA POR LA CONSTANTE DADA POR LA CAJA"""
        output_items[0][:] = input_items[0] * self.example_param
        # SE RETORNA LA SEÑAL DE SALIDA.
        return len(output_items[0])