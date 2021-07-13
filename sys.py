#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gi.repository import Gtk
import os
import platform
import psutil
import cpuinfo
import subprocess

#Uncomment this line on raspberry pi's
#from gpiozero import CPUTemperature

class Handler:
  def b2cl(self,button):
   window.hide()
   win2.show()
  def b1cl(self,button):
   pass
  def b3cl(self,button):
   win2.hide()
   window.show()
  def b4cl(self,button):
   pass
  def dcl(self,button):
   window.hide()
   win3.show()
  def d1cl(self,button):
   win2.hide()
   win3.show()
  def s1cl(self,button):
   win3.hide()
   window.show()
  def s2cl(self,button):
   win3.hide()
   win2.show()
  def s3cl(self,button):
   pass
builder = Gtk.Builder()
builder.add_from_file("sys.glade")
builder.connect_signals(Handler())
Host = builder.get_object("l2")
uname=platform.uname()
part=psutil.disk_partitions()
h=uname.node
Host.set_label("<b>Hostname</b> : "+h)
cpu=builder.get_object("l3")
p=uname.processor
cpu.set_label("<b>CPU</b> : "+str(p))
machine=builder.get_object("l4")
m=uname.machine
machine.set_label("<b>Architecture</b> : "+m)
c=psutil.cpu_count()
ca=builder.get_object("l5")
ca.set_label("<b>Cores</b> : "+str(c))
cpufreq=psutil.cpu_freq()
b=builder.get_object("l6")
b.set_label("<b>CPU Frequency</b> : "+str(cpufreq.current))
bu=builder.get_object("l7")
mem=psutil.virtual_memory()
bu.set_label("<b>Total RAM</b> : "+str(mem.total)[0:4]+" MB")
br=builder.get_object("l8")
br.set_label("<b>RAM used</b> : "+str(mem.percent)+"%")


#Uncomment these lines on Raspberry Pi's
#temp = CPUTemperature()
#bh = builder.get_object("l9")
#bh.set_label("<b>Temperature</b> : "+str(temp.temperature)+" C")


for partition in part:
 ab=builder.get_object("1")
 ab.set_label("<b>Device</b> : "+str(partition.device))
 bc=builder.get_object("2")
 bc.set_label("<b>Mountpoint</b> : "+str(partition.device))
 cd=builder.get_object("3")
 cd.set_label("<b>File System</b> : "+str(partition.fstype))
 de=builder.get_object("4")
 parti=psutil.disk_usage(partition.mountpoint)
 de.set_label("<i><b>Stats (in MB)</b></i>")
 ef=builder.get_object("5")
 ef.set_label("<b>Used</b> : "+str(parti.used)[0:5])
 gh=builder.get_object("6")
 gh.set_label("<b>Free</b> : "+str(parti.free)[0:5])
 hi=builder.get_object("7")
 hi.set_label("<b>Used Percentage</b> : "+str(parti.percent)+"%")
 

window=builder.get_object("win1")
win2=builder.get_object("win2")
win3=builder.get_object("win3")
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()


