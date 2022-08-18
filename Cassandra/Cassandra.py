import tkinter
import Errors
from tkinter.font import Font
import About
import Help
import math

class Cassandra(tkinter.Tk):
	def __init__(self,parent):
		tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()
		self.CreateWidgets()
		self.trackList()

	def initialize(self):
		self.grid()
		
	def CreateWidgets(self):
		#This section creates the frames
		_ribbon_frame=tkinter.Frame(self.parent, relief="raised", height="0.6c", width=1200)
		_ribbon_frame.grid_propagate(0)
		_ribbon_frame.grid()

		_input_frame=tkinter.Frame(self.parent, bg="gray", borderwidth=3, relief="groove", height="14.5c", width="10c")
		_input_frame.grid_propagate(0)
		_input_frame.grid(row=1, column=0, sticky="N")
		_input_frame.place(x="0.5c",y="2.2c")

		_frate_frame=tkinter.Frame(self.parent, bg="gray", borderwidth=3, relief="groove", height="11.2c", width="10c")
		_frate_frame.grid_propagate(0)
		_frate_frame.grid(row=1, column=0, sticky="N")
		_frate_frame.place(x="11.5c",y="2.2c")

		_frate_frame1=tkinter.Frame(_frate_frame, bg="gray", borderwidth=3, relief="groove", height="2.2c", width="9.8c")
		_frate_frame1.grid_propagate(0)
		_frate_frame1.place(x="0.03c", y="1.2c")

		_frate_frame2=tkinter.Frame(_frate_frame, bg="gray", borderwidth=3, relief="groove", height="5.1c", width="9.8c")
		_frate_frame2.grid_propagate(0)
		_frate_frame2.place(x="0.03c", y="3.6c")

		_frate_frame3=tkinter.Frame(_frate_frame, bg="gray", borderwidth=3, relief="groove", height="2c", width="9.8c")
		_frate_frame3.grid_propagate(0)
		_frate_frame3.place(x="0.03c", y="8.8c")

		_unit_frame=tkinter.Frame(_input_frame, bg="gray", borderwidth=3, relief="groove", height="2.2c",width="9.8c")
		_unit_frame.grid_propagate(0)
		_unit_frame.grid(row=1, pady=2.5)

		_reservoirdata_frame=tkinter.Frame(_input_frame, bg="gray", borderwidth=3, relief="groove", height="5.4c", width="9.8c")
		_reservoirdata_frame.grid_propagate(0)
		_reservoirdata_frame.grid(row=2, pady=2.5)

		_depletedreservoir_frame=tkinter.Frame(_input_frame, bg="gray", bd=3, relief="groove", height="4.2c", width="9.8c")
		_depletedreservoir_frame.grid_propagate(0)
		_depletedreservoir_frame.grid(row=3, pady=2.5)

		_results_frame=tkinter.Frame(self.parent, bg="gray", borderwidth=3, relief="groove", height="8c", width="8c")
		_results_frame.grid_propagate(0)
		_results_frame.place(x="22.5c",y="2.2c")

		_dialog_frame=tkinter.Frame(self.parent, bg="gray", borderwidth=3, relief="groove", height="5.5c", width="8c")
		_dialog_frame.grid_propagate(0)
		_dialog_frame.place(x="22.5c", y="11c")

		_dialogbox_frame=tkinter.Frame(_dialog_frame, bg="white", borderwidth=3, relief="sunk", height="4.5c", width="7.8c")
		_dialogbox_frame.grid_propagate(0)
		_dialogbox_frame.place(y="0.8c")

		_output_frame=tkinter.Frame(_results_frame, bg="gray", bd=3, relief="groove", height="6.3c", width="7.6c")
		_output_frame.grid_propagate(0)
		_output_frame.place(x="0.1c", y="1.2c")

		#------------------------------------------------------------------------------------------------------

		#This section places widgets in the root window
		_applogo_label=tkinter.Label(self.parent, bg="gray", text="CASSANDRA",
					fg="black")
		_applogo_label.place(x="12c",y="0.6c")
		_applogo_font=Font(family="Cooper Black", size=30, weight="bold")
		_applogo_label.configure(font=_applogo_font)

		_copyright_label=tkinter.Label(self.parent, text="\xa9 Ehihamen Precious 2018")
		_copyright_label.place(x='27.5c',y="17c")

		#------------------------------------------------------------------------------------------------------
		
		#This is for validation
		validation= self.register(self.checkValidation)

		#------------------------------------------------------------------------------------------------------
		#This section places widgets in the created frames
		_reset_button=tkinter.Button(_ribbon_frame, text="Reset", relief="flat",command=self.ResetCassandra)
		_reset_button.grid(row=0, column=0, padx=3)

		_about_button=tkinter.Button(_ribbon_frame, text="About", relief="flat", command=self.AboutCassandra)
		_about_button.grid(row=0, column=1, padx=3)

		_help_button=tkinter.Button(_ribbon_frame, text="Help", relief="flat", command=self.HelpCassandra)
		_help_button.grid(row=0, column=2, padx=3)

		_calc_button=tkinter.Button(_ribbon_frame, text="Calculate", relief="flat", command=self.SolveCassandra)
		_calc_button.grid(row=0, column=3, padx=3)

		_input_label=tkinter.Label(_input_frame, bg="gray", text="PRESSURE PARAMETERS")
		_input_label.grid(column=0, row=0, sticky="N", pady=10)
		_input_font=Font(family="Times New Roman", size=11, weight="bold")
		_input_label.configure(font=_input_font)

		self._unit_label=tkinter.Label(_unit_frame, text="Preferred unit")
		self._unit_label.grid(column=0, row=1, sticky="W", pady=6)
		self._units_list=tkinter.Listbox(_unit_frame, height=2, exportselection=0)
		self._units_list.grid(column=0, row=2, sticky="W")
		self._units_list.insert(0, "psi")
		self._units_list.insert(1, "MPa")

		_UCS_label=tkinter.Label(_reservoirdata_frame, text="Uniaxial Comp. Strength")
		_UCS_label.place(y="0.2c")
		self._UCS_entry=tkinter.Entry(_reservoirdata_frame, validate="key", validatecommand=(validation, '%S'))
		self._UCS_entry.place(y="0.9c")
		
		_min_label=tkinter.Label(_reservoirdata_frame, text="Min principal stress")
		_min_label.place(y="1.9c")
		self._min_entry=tkinter.Entry(_reservoirdata_frame, validate="key", validatecommand=(validation, '%S'))
		self._min_entry.place(y="2.5c")

		_max_label=tkinter.Label(_reservoirdata_frame, text="Max principal stress")
		_max_label.place(x="4.0c", y="1.9c")
		self._max_entry=tkinter.Entry(_reservoirdata_frame, validate="key", validatecommand=(validation, '%S'))
		self._max_entry.place(x="4.0c", y="2.5c")

		_reservoirtype_label=tkinter.Label(_reservoirdata_frame, text="Reservoir type")
		_reservoirtype_label.place(y="3.4c")
		self._reservoirtype_list=tkinter.Listbox(_reservoirdata_frame, height=2, exportselection=0)
		self._reservoirtype_list.place(y="4.1c")
		self._reservoirtype_list.insert(0,"New reservoir")
		self._reservoirtype_list.insert(1,"Depleted reservoir")

		_depletedreservoir_label=tkinter.Label(_depletedreservoir_frame, bg="gray", text="For depleted reservoir only")
		_depletedreservoir_label.place(x="2.5c")
		_depletedreservoir_font=Font(family="Times New Roman", size=10, weight="bold")
		_depletedreservoir_label.configure(font=_depletedreservoir_font)

		_porepressure_label=tkinter.Label(_depletedreservoir_frame, text="Pore Press. Coeefficient")
		_porepressure_label.place(y="0.8c")
		self._porepressure_entry=tkinter.Entry(_depletedreservoir_frame, validate="key", validatecommand=(validation, '%S'))
		self._porepressure_entry.place(y="1.5c")

		_initialpressure_label=tkinter.Label(_depletedreservoir_frame, text="Initial Reservoir Pressure")
		_initialpressure_label.place(y="2.4c")
		self._initialpressure_entry=tkinter.Entry(_depletedreservoir_frame, validate="key", validatecommand=(validation, '%S'))
		self._initialpressure_entry.place(y="3.1c")

		_presentpressure_label=tkinter.Label(_depletedreservoir_frame, text="Present Reservoir Pressure")
		_presentpressure_label.place(x="4c", y="2.4c")
		self._presentpressure_entry=tkinter.Entry(_depletedreservoir_frame, validate="key", validatecommand=(validation, '%S'))
		self._presentpressure_entry.place(x="4c", y="3.1c")

		self._askrateVar_check=tkinter.IntVar(self.parent)
		self._askrate_check=tkinter.Checkbutton(_input_frame, bg="gray", text="Estimate critical rate?", variable=self._askrateVar_check, command=self.activateRate)
		self._askrate_check.grid(row=4, pady=5)
		#End of pressure parameters------------------------

		#Rate parameters begin-----------------------------
		_rate_label=tkinter.Label(_frate_frame, bg="gray", text="RATE PARAMETERS")
		_rate_label.grid(row=0)
		_rate_label.configure(font=_input_font)
		_rate_label.place(x="2.9c", y="0.2c")
		
		_fluidtype_label=tkinter.Label(_frate_frame1, text="Fluid Type")
		_fluidtype_label.place(y="0.2c")
		self._fluid_list=tkinter.Listbox(_frate_frame1, height=2, exportselection=0)
		self._fluid_list.place(y="1c")
		self._fluid_list.insert(0, "Oil")
		self._fluid_list.insert(1, "Gas")
		self._fluid_list.configure(state="disabled")

		_perm_label=tkinter.Label(_frate_frame2, text="Avg. Permeability (md)")
		_perm_label.place(y="0.2c")
		self._perm_entry=tkinter.Entry(_frate_frame2, state="disabled", validate="key", validatecommand=(validation, '%S'))
		self._perm_entry.place(y="0.9c")

		_temp_label=tkinter.Label(_frate_frame2, text="Reservoir Temperature")
		_temp_label.place(x="4c", y="0.2c")
		self._temp_entry=tkinter.Entry(_frate_frame2, state="disabled", validate="key", validatecommand=(validation, '%S'))
		self._temp_entry.place(x="4c", y="0.9c")
		
		_pay_label=tkinter.Label(_frate_frame2, text="Net Pay (ft)")
		_pay_label.place(y="1.8c")
		self._pay_entry=tkinter.Entry(_frate_frame2, state="disabled", validate="key", validatecommand=(validation, '%S'))
		self._pay_entry.place(y="2.5c")

		_drad_label=tkinter.Label(_frate_frame2, text="Drainage Radius (ft)")
		_drad_label.place(y="3.4c")
		self._drad_entry=tkinter.Entry(_frate_frame2, state="disabled", validate="key", validatecommand=(validation, '%S'))
		self._drad_entry.place(y="4.1c")

		_wrad_label=tkinter.Label(_frate_frame2, text="Well Radius (ft)")
		_wrad_label.place(x="4c", y="3.4c")
		self._wrad_entry=tkinter.Entry(_frate_frame2, state="disabled", validate="key", validatecommand=(validation, '%S'))
		self._wrad_entry.place(x="4.0c", y="4.1c")

		_fvf_label=tkinter.Label(_frate_frame3, text="FVF")
		_fvf_label.place(y="0.2c")
		self._fvf_entry=tkinter.Entry(_frate_frame3, state="disabled", validate="key", validatecommand=(validation, '%S'))
		self._fvf_entry.place(y="0.9c")

		_visc_label=tkinter.Label(_frate_frame3, text="Viscosity (cp)")
		_visc_label.place(x="4c", y="0.2c")
		self._visc_entry=tkinter.Entry(_frate_frame3, state="disabled", validate="key", validatecommand=(validation, '%S'))
		self._visc_entry.place(x="4c", y="0.9c")
		#End of rate parameters--------------------------------
		
		#Result output begins----------------------------------
		self._results_label=tkinter.Label(_results_frame, bg="gray", text="RESULTS")
		self._results_label.place(x="2.9c", y="0.2c")
		self._results_label.configure(font=_input_font)

		self._reservoiroutput_label=tkinter.Label(_output_frame, bg="gray", text="Reservoir: ")
		self._reservoiroutput_label.grid(column=0, row=0, sticky="W", pady=6)
	
		self._fluidoutput_label=tkinter.Label(_output_frame, bg="gray", text="Flowing Fluid: ")
		self._fluidoutput_label.grid(column=0, row=1, sticky="W", pady=6)

		self._initialpress_output=tkinter.Label(_output_frame, bg="gray", text="Initial Res. Press.: ")
		self._initialpress_output.grid(column=0, row=2, sticky="W", pady=6)

		self._presentpress_output=tkinter.Label(_output_frame, bg="gray", text="Present Res. Press.: ")
		self._presentpress_output.grid(column=0, row=3, sticky="W", pady=6)

		self._cddresult=tkinter.Label(_output_frame, bg="gray", text="Critical Drawdown: ")
		self._cddresult.grid(column=0, row=4, sticky="W", pady=6)

		self._rateoutput_label=tkinter.Label(_output_frame, bg="gray", text="Critical Flowrate: ")
		self._rateoutput_label.grid(column=0, row=5, sticky="W", pady=6)

		self._comment_label=tkinter.Label(_output_frame, bg="gray", text="Comment: ")
		self._comment_label.grid(column=0, row=6, sticky="W", pady=6)

		_dialog_label=tkinter.Label(_dialog_frame, bg="gray", text="Dialog Box")
		_dialog_label.place(x="0.5c", y="0.2c")
		_dialog_label.configure(font=_input_font)

	def trackList(self):
		now = self._fluid_list.curselection()
		if now != ():
			if now[0] == 1:
				self._temp_entry.configure(state="normal")
			else:
				self._temp_entry.configure(state="disabled")

	def checkValidation(self, char):
		return char.isdigit()

	def activateRate(self):
		if self._askrateVar_check.get() == 1:
			self._fluid_list.configure(state="normal")
			self._perm_entry.configure(state="normal")
			self._pay_entry.configure(state="normal")
			self._drad_entry.configure(state="normal")
			self._wrad_entry.configure(state="normal")
			self._fvf_entry.configure(state="normal")
			self._visc_entry.configure(state="normal")
		else:
			self._fluid_list.configure(state="disabled")
			self._perm_entry.configure(state="disabled")
			self._pay_entry.configure(state="disabled")
			self._drad_entry.configure(state="disabled")
			self._wrad_entry.configure(state="disabled")
			self._fvf_entry.configure(state="disabled")
			self._visc_entry.configure(state="disabled")

	def SolveCassandra(self):
		"""This function solves for the critical drawdown of a reservoir
		when given the geomechanical parameters"""

		m=15

		#Get input data from the GUI
		if self._units_list.curselection()==():
			Errors.BlankParameters(self.parent,app,"Preferred unit")
			return
		else:
			_unit=self._units_list.get(self._units_list.curselection())
		_UCS=self._UCS_entry.get()
		_min=self._min_entry.get()
		_max=self._max_entry.get()
		_porepress=self._porepressure_entry.get()
		_inipress=self._initialpressure_entry.get()
		_prepress=self._presentpressure_entry.get()
		if self._reservoirtype_list.curselection()==():
			Errors.BlankParameters(self.parent,app,"Reservoir type")
			return
		else:
			_restype=self._reservoirtype_list.get(self._reservoirtype_list.curselection())

		#First check for possible errors that could hinder the computation and report if found
		L={"Uniaxial Compressive Strength":_UCS, "Minimum Principal Stress":_min, "Maximum Principal Stress":_max}
		M={"Preferred unit":_unit, "Reservoir type":_restype}
		N={"Pore Pressure Coefficient":_porepress, "Initial Reservoir Pressure":_inipress, "Present Reservoir Pressure":_prepress}
		for i in L:
			if L[i]=="":
				Errors.BlankParameters(self.parent,app,i)
				return
			try:
				y=float(L[i])
			except ValueError:
				Errors.TypeResponse(self.parent,app,i)
				return
			if _unit=="MPa" and (y<0 or y>100):
				Errors.RangeResponse(self.parent,app,i,"0","100",_unit)
				return
			elif _unit=="psi" and (y<10 or y>15000):
				Errors.RangeResponse(self.parent,app,i,"10","15000",_unit)
				return

		for j in N:
			if N[j]!="":
				try:
					z=float(N[j])
				except ValueError:
					Errors.TypeResponse(self.parent,app,j)
					return
				if j=="Pore Pressure Coefficient":
                                        if (z<0 or z>1):
                                                Errors.RangeResponse(self.parent,app,j,"0","1")
                                                return
				elif _unit=="MPa" and (z<0 or z>100):
					Errors.RangeResponse(self.parent,app,j,"0","100",_unit)
					return
				elif _unit=="psi" and (z<10 or z>15000):
					Errors.RangeResponse(self.parent,app,j,"10","15000",_unit)
					return
		if float(_max)<float(_min):
			Errors.LessThan(self.parent,app)
			return

		if _inipress != '' and _prepress != '':
			if float(_inipress)-float(_prepress)<0:
				Errors.ResPressError(self.parent,app)
				return
			elif float(_inipress)!=float(_prepress) and self._reservoirtype_list.get(0)==_restype:
				Errors.DepletedRes(self.parent,app)
				return

		#Now attempt to solve for CDD
		UCS=float(_UCS)
		A=(3*float(_max))-float(_min)
		num1=((0.5*m)/UCS)+(2/UCS)
		num2=(0.5*(m/UCS)**2)*((A/UCS)-1)
		den=(0.25*(m/UCS)**2)
		self._CDD=(num1+(((num1)**2)+num2)**0.5)/den
		rate=self.SolveRate()

		#Make necessary adjustments if reservoir is depleted and output results
		if self._reservoirtype_list.get(1)==_restype:
			for m in N:
				if N[m]=="":
					Errors.BlankParameters(self.parent,app,m)
					return	
			self._CDD= self._CDD-((float(_porepress))*(float(_inipress)-float(_prepress)))
		if _inipress=="":
			self._initialpress_output.config(text="Initial Res. Press.: \t\t{0}".format("N/A"))
		else:
			self._initialpress_output.config(text="Initial Res. Press.: \t\t{0}{1}".format(_inipress,_unit))
		if _prepress=="":
			self._presentpress_output.config(text="Present Res. Press.: \t{0}".format("N/A"))
		else:
			self._presentpress_output.config(text="Present Res. Press.: \t{0}{1}".format(_prepress,_unit))
		self._fluidoutput_label.config(text="Flowing Fluid: \t\t{0}{1}".format("Sort this ", "out"))
		self._rateoutput_label.config(text="Critical Rate: \t\t{0}".format(rate))
		self._reservoiroutput_label.config(text="Reservoir: \t\t{}".format(_restype))
		self._cddresult.config(text="Critical Drawdown: \t{0:.2f}{1}".format(self._CDD,_unit))
		self._comment_label.config(text="Comment: \t{0}{1}".format("Comment", "here"))

	def SolveRate(self):
		ftype=self._fluid_list.curselection()[0]
		k=float(self._perm_entry.get())
		h=float(self._pay_entry.get())
		T=float(self._temp_entry.get())
		rd,rw=float(self._drad_entry.get()),float(self._wrad_entry.get())
		b,u=float(self._fvf_entry.get()), float(self._visc_entry.get())
		if ftype==0:
			num=0.00708*k*h*self._CDD
			den=2.303*u*b*math.log10(rd/rw)
		else:
			num=k*h*self._CDD
			den=1638*2.303*T*b*u*math.log10(rd/rw)
		rate= num/den
		return rate

	def ResetCassandra(self):
		self._UCS_entry.delete(0, len(self._UCS_entry.get()))
		self._min_entry.delete(0, len(self._min_entry.get()))
		self._max_entry.delete(0, len(self._max_entry.get()))
		self._porepressure_entry.delete(0, len(self._porepressure_entry.get()))
		self._initialpressure_entry.delete(0, len(self._initialpressure_entry.get()))
		self._presentpressure_entry.delete(0, len(self._presentpressure_entry.get()))
		self._units_list.selection_clear(self._units_list.curselection())
		self._reservoirtype_list.selection_clear(self._reservoirtype_list.curselection())

		self._initialpress_output.config(text="Initial Res. Press.:")
		self._presentpress_output.config(text="Present Res. Press.:")
		self._minoutput_label.config(text="Min Stress:")
		self._maxoutput_label.config(text="Max Stress:")
		self._UCSoutput_label.config(text="Uniaxial Comp. Strength:")
		self._reservoiroutput_label.config(text="Reservoir type:")
		self._cddresult.config(text="Critical Drawdown:")

	def AboutCassandra(self):
		About.About(self.parent, app, About.message)

	def HelpCassandra(self):
		Help.Help(self.parent,app, Help.message)


if __name__== "__main__":
	app= Cassandra(None)
	app.configure(background='gray')
	app.title('Cassandra v2.0.2')
	win_height=665
	win_width=1200
	screen_width=app.winfo_screenwidth()
	screen_height=app.winfo_screenheight()
	x=int((screen_width/2)-(win_width/2))
	y=int((screen_height/2)-(win_height/2))-30
	app.geometry("{}x{}+{}+{}".format(win_width, win_height, x,y))
	"""app.resizable(False, False)"""
	app.mainloop()
