#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun May 31 15:22:51 2020
##################################################


if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 500000

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_1 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_1.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.wxgui_constellationsink2_0 = constsink_gl.const_sink_c(
        	self.GetWin(),
        	title='Constellation Plot',
        	sample_rate=samp_rate,
        	frame_rate=5,
        	const_size=2048,
        	M=4,
        	theta=0,
        	loop_bw=6.28/100.0,
        	fmax=0.06,
        	mu=0.5,
        	gain_mu=0.005,
        	symbol_rate=samp_rate/4.,
        	omega_limit=0.005,
        )
        self.Add(self.wxgui_constellationsink2_0.win)
        self.digital_qam_mod_0 = digital.qam.qam_mod(
          constellation_points=16,
          mod_code="gray",
          differential=True,
          samples_per_symbol=4,
          excess_bw=0.90,
          verbose=False,
          log=False,
          )
        self.digital_qam_demod_0 = digital.qam.qam_demod(
          constellation_points=16,
          differential=True,
          samples_per_symbol=4,
          excess_bw=0.90,
          freq_bw=6.28/100.0,
          timing_bw=6.28/100.0,
          phase_bw=6.28/100.0,
          mod_code="gray",
          verbose=False,
          log=False,
          )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_multiply_xx_0_2 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_complex_to_imag_0_0 = blocks.complex_to_imag(1)
        self.blocks_complex_to_imag_0 = blocks.complex_to_imag(1)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, 25000, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, 25000, 1, 0)
        self.analog_random_source_x_0 = blocks.vector_source_s(map(int, numpy.random.randint(0, 2, 2000000)), True)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_2, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_multiply_xx_0_2, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.blocks_char_to_float_1, 0), (self.wxgui_scopesink2_1, 0))
        self.connect((self.blocks_complex_to_imag_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_imag_0_0, 0), (self.blocks_multiply_xx_0_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.digital_qam_mod_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.digital_qam_demod_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_multiply_xx_0_2, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.digital_qam_demod_0, 0), (self.blocks_char_to_float_1, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.blocks_complex_to_imag_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.blocks_complex_to_imag_0_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.wxgui_constellationsink2_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_1.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_constellationsink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
