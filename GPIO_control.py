import tkinter as tk
import RPi.GPIO as GPIO
from time import sleep

GPIO12 = 12
GPIO16 = 16

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM) IN BCM MODE IT DOES NOT WORK
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GPIO12, GPIO.OUT)
GPIO.setup(GPIO16, GPIO.OUT)

master = tk.Tk()
master.title("GPIO_Control")
master.geometry("300x100")

GPIO12state = False
GPIO16State = False

def GPIO12button():
        global GPIO12state
        if GPIO12state == True:
            GPIO.output(12, GPIO12state)
            GPIO12state = False
            ONlabel = tk.Label(master, text="Turned ON", fg="green")
            ONlabel.grid(row=0, column=1)
        
        else:
             
             GPIO.output(12, GPIO12state)
             GPIO12state = True
             ONlabel = tk.Label(master, text="Turned OFF", fg="green")
             ONlabel.grid(row=0, column=1)
             
def GPIO16button():
        global GPIO16State
        if GPIO16State == True:
            GPIO.output(16, GPIO16State)
            GPIO16State = False
            ONlabel = tk.Label(master, text="Turned ON", fg="green")
            ONlabel.grid(row=1, column=1)
        
        else:
             
             GPIO.output(16, GPIO16State)
             GPIO16State = True
             ONlabel = tk.Label(master, text="Turned OFF", fg="green")
             ONlabel.grid(row=1, column=1)
             
ONbutton = tk.Button(master, text="GPIO12", bg="blue", command=GPIO12button)
ONbutton.grid(row=0, column=0)

OFFbutton = tk.Button(master, text="GPIO16", bg="blue", command=GPIO16button)
OFFbutton.grid(row=1, column=0)

Exitbutton = tk.Button(master, text="Exit", bg="red", command=master.destroy)
Exitbutton.grid(row=2, column=0)
master.mainloop()
GPIO.cleanup()
            