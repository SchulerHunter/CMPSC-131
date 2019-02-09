# This program prompts the user to input a calculate the temperature in fahrenheit and the wind speed
# It then returns the wind chill
# Now featuring a GUI

# Author: Hunter Schuler

import tkinter


class WindChillCalc:
    def __init__(self):
        # Create the main window
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title('Windchill Calculator')

        # Create five frames
        self.titleFrame = tkinter.Frame(self.mainWindow)
        self.tempFrame = tkinter.Frame(self.mainWindow)
        self.speedFrame = tkinter.Frame(self.mainWindow)
        self.buttonFrame = tkinter.Frame(self.mainWindow)
        self.chillFrame = tkinter.Frame(self.mainWindow)

        # Create and pack the title frame
        self.title = tkinter.Label(self.titleFrame, text='Windchill Calculator', fg='Red', bg='Yellow')
        self.title.pack()

        # Create and pack the widget for temperature
        self.tempLabel = tkinter.Label(self.tempFrame, text='Enter the temperature in degrees Fahrenheit:')
        self.tempEntry = tkinter.Entry(self.tempFrame, width=10)
        self.tempLabel.pack(side='left')
        self.tempEntry.pack(side='left')

        # Create and pack the widget for speed
        self.speedLabel = tkinter.Label(self.speedFrame, text='Enter the wind speed in mph:')
        self.speedEntry = tkinter.Entry(self.speedFrame, width=10)
        self.speedLabel.pack(side='left')
        self.speedEntry.pack(side='left')

        # Create and pack the widget for the button
        self.calcButton = tkinter.Button(self.buttonFrame, text='Calculate Windchill',
                                         command=self.windchill)
        self.calcButton.pack(side='left')

        # Create and pack the widget for the calculated windchill
        self.resultLabel = tkinter.Label(self.chillFrame, text='The windchill temperature is:')
        self.chillTemp = tkinter.StringVar()
        self.chillTempLabel = tkinter.Label(self.chillFrame, textvar=self.chillTemp)
        self.resultLabel.pack(side='left')
        self.chillTempLabel.pack(side='left')

        # Pack the frame
        self.titleFrame.pack()
        self.tempFrame.pack()
        self.speedFrame.pack()
        self.buttonFrame.pack()
        self.chillFrame.pack()

        # Start the loop
        tkinter.mainloop()

    def windchill(self):
        temp = float(self.tempEntry.get())
        speed = float(self.speedEntry.get())
        chill = 35.74 + .6215 * temp - 35.75 * speed ** .16 + .4275 * temp * speed ** .16
        self.chillTemp.set(format(chill, '.1f') + ' degrees Fahrenheit')


# Create an instance of the object
windChill = WindChillCalc()
