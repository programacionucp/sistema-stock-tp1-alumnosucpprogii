#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 14, 2020 05:17:19 PM -03  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global spinbox
    spinbox = tk.StringVar()
    global EntryDis
    EntryDis = tk.StringVar()
    global EntryPre
    EntryPre = tk.StringVar()
    global R2_tur
    R2_tur = tk.StringVar()
    global R3_prim
    R3_prim = tk.StringVar()
    global R3_vip
    R3_vip = tk.StringVar()
    global R1_ida
    R1_ida = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def calculo():
    print('Viajero01_support.calculo')
    sys.stdout.flush()

def destroy_window():
    print('Viajero01_support.destroy_window')
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import Viajero01
    Viajero01.vp_start_gui()




