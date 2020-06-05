#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Filter Taps
# Generated: Thu Jun  4 18:31:51 2020
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
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class filter_taps(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Filter Taps")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.transition = transition = 1000
        self.samp_rate = samp_rate = 32000
        self.cutoff_low = cutoff_low = 2000
        self.cutoff_high = cutoff_high = 14000
        self.bp_low = bp_low = 6000
        self.bp_high = bp_high = 10000

        self.lp_taps = lp_taps = firdes.low_pass(1.0, samp_rate, cutoff_high, transition, firdes.WIN_HAMMING, 6.76)


        self.hp_taps = hp_taps = firdes.high_pass(1.0, samp_rate, cutoff_low, transition, firdes.WIN_HAMMING, 6.76)


        self.bp_taps = bp_taps = firdes.band_pass(1.0, samp_rate, bp_low, bp_high, transition, firdes.WIN_HAMMING, 6.76)


        ##################################################
        # Blocks
        ##################################################
        self.notebook = self.notebook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "lp")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "hp")
        self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "bp")
        self.Add(self.notebook)
        self.wxgui_fftsink2_0_0_1_0_1 = fftsink2.fft_sink_f(
        	self.notebook.GetPage(2).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=4096,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='filtro pasa banda',
        	peak_hold=False,
        	win=window.flattop,
        )
        self.notebook.GetPage(2).Add(self.wxgui_fftsink2_0_0_1_0_1.win)
        self.wxgui_fftsink2_0_0_1_0_0 = fftsink2.fft_sink_f(
        	self.notebook.GetPage(1).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=4096,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='filtro pasa altas',
        	peak_hold=False,
        	win=window.flattop,
        )
        self.notebook.GetPage(1).Add(self.wxgui_fftsink2_0_0_1_0_0.win)
        self.wxgui_fftsink2_0_0_1_0 = fftsink2.fft_sink_f(
        	self.notebook.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=4096,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='filtro pasa bajas',
        	peak_hold=False,
        	win=window.flattop,
        )
        self.notebook.GetPage(0).Add(self.wxgui_fftsink2_0_0_1_0.win)
        self.lp_filter = filter.fir_filter_fff(1, (lp_taps))
        self.lp_filter.declare_sample_delay(0)
        self.hp_filter = filter.fir_filter_fff(1, (hp_taps))
        self.hp_filter.declare_sample_delay(0)
        self.bp_filter = filter.fir_filter_fff(1, (bp_taps))
        self.bp_filter.declare_sample_delay(0)
        self.blocks_throttle_0_1_0_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_1_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_throttle_0_1 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_f(analog.GR_GAUSSIAN, 1, 0, 8192)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.bp_filter, 0))
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.hp_filter, 0))
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.lp_filter, 0))
        self.connect((self.blocks_throttle_0_1, 0), (self.wxgui_fftsink2_0_0_1_0, 0))
        self.connect((self.blocks_throttle_0_1_0, 0), (self.wxgui_fftsink2_0_0_1_0_0, 0))
        self.connect((self.blocks_throttle_0_1_0_0, 0), (self.wxgui_fftsink2_0_0_1_0_1, 0))
        self.connect((self.bp_filter, 0), (self.blocks_throttle_0_1_0_0, 0))
        self.connect((self.hp_filter, 0), (self.blocks_throttle_0_1_0, 0))
        self.connect((self.lp_filter, 0), (self.blocks_throttle_0_1, 0))

    def get_transition(self):
        return self.transition

    def set_transition(self, transition):
        self.transition = transition

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_fftsink2_0_0_1_0_1.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0_1_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_0_0_1_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_1_0_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_1_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0_1.set_sample_rate(self.samp_rate)

    def get_cutoff_low(self):
        return self.cutoff_low

    def set_cutoff_low(self, cutoff_low):
        self.cutoff_low = cutoff_low

    def get_cutoff_high(self):
        return self.cutoff_high

    def set_cutoff_high(self, cutoff_high):
        self.cutoff_high = cutoff_high

    def get_bp_low(self):
        return self.bp_low

    def set_bp_low(self, bp_low):
        self.bp_low = bp_low

    def get_bp_high(self):
        return self.bp_high

    def set_bp_high(self, bp_high):
        self.bp_high = bp_high

    def get_lp_taps(self):
        return self.lp_taps

    def set_lp_taps(self, lp_taps):
        self.lp_taps = lp_taps
        self.lp_filter.set_taps((self.lp_taps))

    def get_hp_taps(self):
        return self.hp_taps

    def set_hp_taps(self, hp_taps):
        self.hp_taps = hp_taps
        self.hp_filter.set_taps((self.hp_taps))

    def get_bp_taps(self):
        return self.bp_taps

    def set_bp_taps(self, bp_taps):
        self.bp_taps = bp_taps
        self.bp_filter.set_taps((self.bp_taps))


def main(top_block_cls=filter_taps, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
