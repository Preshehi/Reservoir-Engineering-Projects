#import important libraries
import tkinter
from tkinter.font import Font

#Create a frame to display instructions for how to use the app
def Help(frame, window, message):
	helpfile=tkinter.Toplevel(frame, bg="white")
	helpfile.grab_set()
	myfont=Font(family="Lucida Sans Typewriter", size=10)
	helplabel=tkinter.Label(helpfile, text=message, bg="white", anchor="w")
	helplabel.place(x=25, y=35)
	helplabel.configure(font=myfont)
	helpfile.resizable(0,0)
	x=window.winfo_x()
	y=window.winfo_y()
	helpfile.geometry("560x580+{}+{}".format(120+x,42+y))
	helpfile.title(string="Help")
	helplabelpage=tkinter.Label(helpfile, text='Page')
	helplabelpage.place(x=220, y=545)
	helpbutton1=tkinter.Button(helpfile, text="1", bg="white", fg="blue", activebackground="blue", relief="flat", command=lambda: flippage(1))
	helpbutton1.place(x=270, y=545)
	helpbutton2= tkinter.Button(helpfile, text="2", bg="white", fg="blue", activebackground="blue", relief="flat", command=lambda: flippage(2))
	helpbutton2.place(x=300, y=545)
	helpbutton3=tkinter.Button(helpfile, text="3", bg="white", fg="blue", activebackground="blue", relief="flat", command=lambda: flippage(3))
	helpbutton3.place(x=330, y=545)

	def flippage(x):
		if x==1:
			helplabel.config(text=message)
		elif x==2:
			helplabel.config(text=message1)
		elif x==3:
			helplabel.config(text=message2)

#Define messages to be displayed on the frame
message="""
Cassandra takes eight input parameters, 5 of which are 
always required while the last three are dependent on
the type of reservoir being analyzed. Each of these
parameters are explored here.


1) Preferred unit: This is a required parameter. Since
all the parameters being worked with, barring the pore
pressure co-efficient, are pressure/stress parameters,
Cassandra needs to know the unit in which pressure
readings were taken during testing so as to operate
within the required range.


2) Uniaxial Compressive Strength: This is a required
parameter. Usually obtained from core tests, this
parameter must be a real number else an error occurs.
If the unit of operation is MPa, the range Cassandra
allows is 0 to 100 while psi allows a range of 10 to
15000 thus, an error also occurs if the range is exceeded.


3) Minimum Principal stress: This is a required parameter.
Usually obtained from log analysis, this parameter must be
a real number else an error occurs. If the unit of operation
is MPa, the range of values Cassandra allows is 0 to 100
while psi allows a range of 10 to 15000 thus, an error also
occurs if the range is exceeded.


(1 of 3)
"""

message1="""
4) Maximum Principal stress: This is a required parameter.
Usually obtained from log analysis, this parameter must be
a real number else an error occurs. If the unit of operation
is MPa, the range Cassandra allows is 0 to 100 while for psi,
Cassandra allows a range of 10 to 15000. An error occurs if
the range is exceeded.


5) Reservoir type: This is a required parameter. Cassandra
must know the type of reservoir that is being analysed so as
to compute its critical drawdown appropriately. There are two 
choices to pick from:
	a) New reservoir: does not necessarily refer to newly
	opened reservoir. It refers to any reservoir that has
	not undergone significant reservoir pressure depletion
	compared to when it was initially opened.

	b) Depleted reservoir: refers to any reservoir that has
	undergone significant reservoir pressure depletion
	compared to when it was initially opened.


6) Pore Pressure Co-efficient: This parameter is only required
for depleted reservoirs, thus if left blank for new reservoirs,
no error occurs. Usually obtained from core analysis, this
parameter must be a real number ranging from 0 to 1. An error
occurs if this range is exceeded.


(2 of 3)
"""

message2="""
7) Initial Reservoir Pressure: This parameter is only required
for depleted reservoirs, thus if left blank for new reservoirs,
no error occurs. This parameter must be a real number. If the
unit of operation is MPa, the range Cassandra allows is 0 to 100
while for psi, Cassandra allows a range of 10 to 15000. An error
occurs if this range is exceeded.


8) Present Reservoir Pressure: This parameter is only required
for depleted reservoirs, thus if left blank for new reservoirs,
no error occurs. This parameter must be a real number. If the
unit of operation is MPa, the range Cassandra allows is 0 to 100
while for psi, Cassandra allows a range of 10 to 15000. An error
occurs if this range is exceeded.
















(3 of 3)
"""
