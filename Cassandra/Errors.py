import tkinter
from tkinter.font import Font

class Error(Exception):
	pass

def ErrorTopLevel(frame, window, message):
	errorfile=tkinter.Toplevel(frame, bg="white")
	errorfile.grab_set()
	myfont=Font(family="Lucida Sans Typewriter", size=10)
	errorlabel=tkinter.Label(errorfile, bg="white", text=message, wraplength=350)
	errorlabel.place(x=25, y=35)
	errorlabel.configure(font=myfont)
	errorfile.resizable(0,0)
	x=window.winfo_x()
	y=window.winfo_y()
	errorfile.geometry("400x100+{}+{}".format(200+x,283+y))
	errorfile.title(string="Error Message")

def TypeResponse(frame,window,x):
	message= "Type Error: %s must be a real number." % (x)
	ErrorTopLevel(frame, window, message)

def RangeResponse(frame, window,x,y,z,w=''):
	message= "Range Error: %s can only be within the range of %s to %s%s" % (x,y,z,w)
	ErrorTopLevel(frame, window,message)

def BlankParameters(frame, window,x):
	message= "Blank Parameter: %s is an essential parameter and must be provided" % (x)
	ErrorTopLevel(frame, window,message)

def LessThan(frame,window):
	message="Maximum Principal Stress cannot be less than Minimum Principal Stress"
	ErrorTopLevel(frame,window,message)

def DepletedRes(frame,window):
	message="The reservoir seems depleted. If you want to assume a new reservoir, leave the depleted section blank"
	ErrorTopLevel(frame,window,message)

def ResPresError(frame,window):
	message="Present reservoir pressure cannot be more than initial reservoir pressure"
	ErrorTopLevel(frame,window,message)
