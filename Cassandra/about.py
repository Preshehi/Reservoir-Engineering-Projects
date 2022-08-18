import tkinter
from tkinter.font import Font

def About(frame, window, message):
	aboutfile=tkinter.Toplevel(frame, bg="white")
	aboutfile.grab_set()
	myfont=Font(family="Lucida Sans Typewriter", size=10)
	aboutlabel=tkinter.Label(aboutfile, text=message, bg="white")
	aboutlabel.place(x=25, y=35)
	aboutlabel.configure(font=myfont)
	aboutfile.resizable(0,0)
	x=window.winfo_x()
	y=window.winfo_y()
	aboutfile.geometry("600x350+{}+{}".format(100+x,158+y))
	aboutfile.title(string="About Cassandra")

message="""
Cassandra is a software that simulates the sand production
environment of a typical petroleum reservoir. It operates
based on the model designed by the developer of the simulator,
Ehihamen Precious. The model modifies that of Oluyemi and
Oyeneyin (2010) and produces results of considerably impeccable
accuracy, having only 8% absolute error after validation with
5 different reservoirs.


The full details of the working principles can be obtained in
the project authored by the aforementioned developer of the
simulator titled "CRITICAL DRAWDOWN ESTIMATION AT THE ONSET OF
SAND PRODUCTION USING IMPROVED GEOMECHANICAL MODEL AND DEVELOPMENT
OF SAND PRODUCTION SIMULATOR" or the SPE paper still written by the
said author titled "CASSANDRA: A MODEL AND SIMULATOR DEVELOPED FOR
CRITICAL DRAWDOWN ESTIMATION IN UNCONSOLIDATED RESERVOIRS".
"""
