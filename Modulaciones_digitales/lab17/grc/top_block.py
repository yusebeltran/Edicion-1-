#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jun  4 18:49:37 2020
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
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import filter
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
        self.samp_rate = samp_rate = 200e3
        self.frec_portadora = frec_portadora = 1e3
        self.frec_moduladora = frec_moduladora = 500

        ##################################################
        # Blocks
        ##################################################
        self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "mod BPSK")
        self.nb.AddPage(grc_wxgui.Panel(self.nb), "demod  floatPSK")
        self.Add(self.nb)
        _frec_portadora_sizer = wx.BoxSizer(wx.VERTICAL)
        self._frec_portadora_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_frec_portadora_sizer,
        	value=self.frec_portadora,
        	callback=self.set_frec_portadora,
        	label='frec_portadora',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._frec_portadora_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_frec_portadora_sizer,
        	value=self.frec_portadora,
        	callback=self.set_frec_portadora,
        	minimum=0,
        	maximum=15e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_frec_portadora_sizer)
        _frec_moduladora_sizer = wx.BoxSizer(wx.VERTICAL)
        self._frec_moduladora_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_frec_moduladora_sizer,
        	value=self.frec_moduladora,
        	callback=self.set_frec_moduladora,
        	label='frec_moduladora',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._frec_moduladora_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_frec_moduladora_sizer,
        	value=self.frec_moduladora,
        	callback=self.set_frec_moduladora,
        	minimum=0,
        	maximum=3e3,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_frec_moduladora_sizer)
        self.wxgui_scopesink2_0_0_0 = scopesink2.scope_sink_f(
        	self.nb.GetPage(1).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.nb.GetPage(1).Add(self.wxgui_scopesink2_0_0_0.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.nb.GetPage(0).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=2,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.nb.GetPage(0).Add(self.wxgui_scopesink2_0.win)
        self.low_pass_filter_0_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	10, samp_rate, 600, 280, firdes.WIN_HAMMING, 6.76))
        self.channels_quantizer_0 = channels.quantizer(16)
        self.blocks_throttle_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, frec_moduladora, 2, -1)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_SIN_WAVE, frec_portadora, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))    
        self.connect((self.analog_sig_source_x_1, 0), (self.blocks_throttle_1, 0))    
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_multiply_xx_1, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_abs_xx_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_xx_1, 1))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.wxgui_scopesink2_0, 0))    
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.blocks_throttle_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_throttle_1, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_throttle_1, 0), (self.wxgui_scopesink2_0, 1))    
        self.connect((self.blocks_throttle_1, 0), (self.wxgui_scopesink2_0_0_0, 1))    
        self.connect((self.channels_quantizer_0, 0), (self.wxgui_scopesink2_0_0_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.channels_quantizer_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_1.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(10, self.samp_rate, 600, 280, firdes.WIN_HAMMING, 6.76))
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0_0_0.set_sample_rate(self.samp_rate)

    def get_frec_portadora(self):
        return self.frec_portadora

    def set_frec_portadora(self, frec_portadora):
        self.frec_portadora = frec_portadora
        self._frec_portadora_slider.set_value(self.frec_portadora)
        self._frec_portadora_text_box.set_value(self.frec_portadora)
        self.analog_sig_source_x_0.set_frequency(self.frec_portadora)

    def get_frec_moduladora(self):
        return self.frec_moduladora

    def set_frec_moduladora(self, frec_moduladora):
        self.frec_moduladora = frec_moduladora
        self._frec_moduladora_slider.set_value(self.frec_moduladora)
        self._frec_moduladora_text_box.set_value(self.frec_moduladora)
        self.analog_sig_source_x_1.set_frequency(self.frec_moduladora)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
