#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class usrp_testing(gr.basic_block):
    """
    docstring for block usrp_testing
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="usrp_testing",
            in_sig=[numpy.complex64],
            out_sig=None,
            )

        self.acc1 = 0
        self.acc2 = 0
        
    def general_work(self, input_items, output_items):
        in0 = input_items[0]
        nread = self.nitems_read(0)
        ninput_items = len(input_items[0])
        
        self.acc1 = float(self.acc1 + ninput_items)
        if self.acc2 < numpy.floor(self.acc1/1000000.0):
            print "---------> time %i" %(numpy.floor(self.acc1/1000000.0))
            print "---------> nread/32e3 %i ninput_items %f " %(numpy.floor(nread/1000000.0), ninput_items)
            self.acc2 = numpy.floor(self.acc1/1000000.0)

        #out = output_items[0]
        # <+signal processing here+>
        #out[:] = in0
        return len(input_items[0])

