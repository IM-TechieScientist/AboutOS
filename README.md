# AboutOS
This is an "about OS" application that is inspired by Mac OS's About this Mac feature..but for linux(debian)
THis works on ARM(Raspberry Pi) and on x86 linux as long as it's debian based(raspberry pi os, ubuntu etc)
It is coded on python and uses Gtk so incredibly light-weight and fast on low resource Computers..

x86:

<img src="https://user-images.githubusercontent.com/84835176/125392090-31e2b100-e3c3-11eb-9636-c9fc7cbbd818.png">

<br>

Raspberry Pi(Raspberry Pi OS+XFCE here):

![Screenshot_2021-07-11_16-43-39](https://user-images.githubusercontent.com/84835176/125395127-66a53700-e3c8-11eb-90b9-387c1f07f413.png)

<br>

# Installation:
<br>
`git clone https://github.com/IM-TechieScientist/AboutOS/`
<br>
`cd AboutOS`
<br>
`sudo mv * /home/pi/Desktop`
<br>
`cd Desktop`
<br>
`sudo chmod +x sys.py`
<br>
`pip3 install psutil(this might fail as it might be pre-installed)`
<br>
`pip3 install py-cpuinfo gpiozero`
<br>
`./sys.py`
<br>
`Or if you are on a debian based system (ubuntu doesn't work with .desktop files) click on the About_Amog_OS.desktop` 
<br>
<br>
**This Project was originally created for the Amog OS project..requested by Moon1789**


