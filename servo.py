import serial
from tkinter import *
import time

ser = 0
def open_serial_port():
	global ser
	get_txt = textentry.get()
	ser = serial.Serial(get_txt, 300, timeout=1)
	print(ser.name)         # check which port was really used
	
def close_serial_port():
	global ser
	print(ser.name)         # check which port was really used
	ser.close()
	
def inc_deg():
	global ser
	ser.write(b'+')
	
def dec_deg():
	global ser
	ser.write(b'-')
	
def set_servo_0():
	global ser
	ser.write(b'0\r')
	
def set_servo_90():
	global ser
	ser.write(b'90\r')
	
def set_servo_180():
	global ser
	ser.write(b'180\r')
	
def set_servo_210():
	global ser
	ser.write(b'210\r')
	
def set_servo_deg():
	global ser
	deg = degentry.get()
	deg = deg.encode()
	ser.write(deg)
	ser.write(b'\r')

window = Tk()
window.title("Servo Controle")
window.geometry("800x400")

Label(window,text = "Select Serial Port:",bg="white",fg="black").grid(row=0,column=0)
textentry = Entry(window,width = 20,bg="white")
textentry.grid(row=0,column=1)

Label(window,text = "Set Servo Degree:",bg="white",fg="black").grid(row=4,column=0)
degentry = Entry(window,width = 20,bg="white")
degentry.grid(row=4,column=1)

Button(window,text = "Open",bg="green",fg="black",font = ('Sans','10','bold'),command=open_serial_port).grid(row=0,column=2)
Button(window,text = "Close",bg="red",fg="black",font = ('Sans','10','bold'),command=close_serial_port).grid(row=0,column=3)

Button(window,text = "Step Up",bg="gray",fg="black",font = ('Sans','10','bold'),command=inc_deg,height = 5, width = 10).grid(row=1,column=0)
Button(window,text = "Step Down",bg="gray",fg="black",font = ('Sans','10','bold'),command=dec_deg,height = 5, width = 10).grid(row=1,column=1)

Button(window,text = "servo 0",bg="magenta",fg="black",font = ('Sans','10','bold'),command=set_servo_0,height = 5, width = 10).grid(row=2,column=0)
Button(window,text = "servo 90",bg="magenta",fg="black",font = ('Sans','10','bold'),command=set_servo_90,height = 5, width = 10).grid(row=2,column=1)
Button(window,text = "servo 180",bg="magenta",fg="black",font = ('Sans','10','bold'),command=set_servo_180,height = 5, width = 10).grid(row=2,column=2)
Button(window,text = "servo 210",bg="magenta",fg="black",font = ('Sans','10','bold'),command=set_servo_210,height = 5, width = 10).grid(row=2,column=4)

Button(window,text = "Set!",bg="green",fg="black",command=set_servo_deg).grid(row=4,column=2)
window.mainloop()

ser.close()