#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon May 18 20:03:42 2020
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
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.frec_3 = frec_3 = 1e3
        self.frec_2 = frec_2 = 1e3
        self.frec_1 = frec_1 = 1e3
        self.Amp_3 = Amp_3 = 25
        self.Amp_2 = Amp_2 = 50
        self.Amp_1 = Amp_1 = 10

        ##################################################
        # Blocks
        ##################################################
        _frec_3_sizer = wx.BoxSizer(wx.VERTICAL)
        self._frec_3_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_frec_3_sizer,
        	value=self.frec_3,
        	callback=self.set_frec_3,
        	label='Frec_trian',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._frec_3_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_frec_3_sizer,
        	value=self.frec_3,
        	callback=self.set_frec_3,
        	minimum=0,
        	maximum=3e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_frec_3_sizer)
        _frec_2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._frec_2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_frec_2_sizer,
        	value=self.frec_2,
        	callback=self.set_frec_2,
        	label='Frec_Seno',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._frec_2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_frec_2_sizer,
        	value=self.frec_2,
        	callback=self.set_frec_2,
        	minimum=0,
        	maximum=4e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_frec_2_sizer)
        _frec_1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._frec_1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_frec_1_sizer,
        	value=self.frec_1,
        	callback=self.set_frec_1,
        	label='Frec_Cuadrada',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._frec_1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_frec_1_sizer,
        	value=self.frec_1,
        	callback=self.set_frec_1,
        	minimum=0,
        	maximum=7e3,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_frec_1_sizer)
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_f(
        	self.GetWin(),
        	title='add signal',
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
        self.Add(self.wxgui_scopesink2_0_0.win)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_float*1, (1, 1,1))
        self.analog_sig_source_3 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, frec_3, Amp_3, 0)
        self.analog_sig_source_2 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, frec_2, Amp_2, 0)
        self.analog_sig_source_1 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, frec_1, Amp_1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_1, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.analog_sig_source_2, 0), (self.blocks_throttle_0, 0))
        self.connect((self.analog_sig_source_3, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.blocks_stream_mux_0, 0), (self.wxgui_scopesink2_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_mux_0, 1))
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_stream_mux_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.blocks_stream_mux_0, 2))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.analog_sig_source_3.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_1.set_sampling_freq(self.samp_rate)

    def get_frec_3(self):
        return self.frec_3

    def set_frec_3(self, frec_3):
        self.frec_3 = frec_3
        self._frec_3_slider.set_value(self.frec_3)
        self._frec_3_text_box.set_value(self.frec_3)
        self.analog_sig_source_3.set_frequency(self.frec_3)

    def get_frec_2(self):
        return self.frec_2

    def set_frec_2(self, frec_2):
        self.frec_2 = frec_2
        self._frec_2_slider.set_value(self.frec_2)
        self._frec_2_text_box.set_value(self.frec_2)
        self.analog_sig_source_2.set_frequency(self.frec_2)

    def get_frec_1(self):
        return self.frec_1

    def set_frec_1(self, frec_1):
        self.frec_1 = frec_1
        self._frec_1_slider.set_value(self.frec_1)
        self._frec_1_text_box.set_value(self.frec_1)
        self.analog_sig_source_1.set_frequency(self.frec_1)

    def get_Amp_3(self):
        return self.Amp_3

    def set_Amp_3(self, Amp_3):
        self.Amp_3 = Amp_3
        self.analog_sig_source_3.set_amplitude(self.Amp_3)

    def get_Amp_2(self):
        return self.Amp_2

    def set_Amp_2(self, Amp_2):
        self.Amp_2 = Amp_2
        self.analog_sig_source_2.set_amplitude(self.Amp_2)

    def get_Amp_1(self):
        return self.Amp_1

    def set_Amp_1(self, Amp_1):
        self.Amp_1 = Amp_1
        self.analog_sig_source_1.set_amplitude(self.Amp_1)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
