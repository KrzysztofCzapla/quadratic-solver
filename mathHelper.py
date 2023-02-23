import PySimpleGUI as sg
import math

sg.theme('Material1')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Delta: Ax² + Bx + C',key='Text1')],
			[sg.InputText(0, size = (5,1), key = 'A'),sg.Text('x² +'),
			 sg.InputText(0, size = (5,1), key = 'B'),sg.Text('x +'),
			 sg.InputText(0, size = (5,1), key = 'C'),
			 sg.Combo(['=', '<','>'],default_value='=',key="Zero"),
			 sg.Text('0',key='Text1')],
			[sg.Button('Ok'), sg.Button('Cancel')], 
			[sg.Text('Delta: ',key='delta'),
			 sg.Text('x1: ',key='x1'),
			 sg.Text('x2: ',key='x2')],
			 [sg.Text('x: ',key='x')],
			

		 ] 

# Create the Window
window = sg.Window('Quadratic solver', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
		break
	
	# if Ok is clicked
	if event == "Ok":
		# taking the values to the variables
		a = int(values["A"])
		b = int(values["B"])
		c = int(values["C"])
		delta = b*b - 4*a*c
		# two Xs
		if delta >0:
			delta = math.sqrt(delta)
			x1 = (delta-b)/(2*a)
			x2 = (-delta-b)/(2*a)
			window['x1'].update("x1: "+str(x1))
			window['x2'].update("x2: "+str(x2))
			xF = 0 # X First
			xS = 0 # X Second

			# Spaghetti sort
			if x1 < x2:
				xF = x1
				xS = x2
			else:
				xF = x2
				xS = x1

			if values["Zero"] == ">":
				
				if a > 0:
					window['x'].update("x: (-∞,"+str(xF)+")u("+str(xS)+",+∞)")
				elif a < 0:
					window['x'].update("x: ("+str(xF)+","+str(xS)+")")

			elif values["Zero"] == "<":
				
				if a < 0:
					window['x'].update("x: (-∞,"+str(xF)+")u("+str(xS)+",+∞)")
				elif a > 0:
					window['x'].update("x: ("+str(xF)+","+str(xS)+")")

			else:
				window['x'].update("x: {"+str(xF)+","+str(xS)+"}")

		# one X		
		elif delta == 0:
			delta = math.sqrt(delta)
			x1 = -b/2*a
			window['x1'].update("x1: "+str(x1))
			window['x2'].update("x2: None")
		# if delta < 0 there are no Xs
		else:
			window['x1'].update("x1: None")
			window['x2'].update("x2: None")


		window['delta'].update("Delta: "+str(delta))


window.close()