from black_scholes import BS
import numpy as np
from tkinter import *

root=Tk()
root.configure(background="black")
root.title("HC BS")
root.geometry("200x400")

call_price = Label()
call_delta = Label()
call_gamma = Label()
call_vega = Label()
call_theta = Label()
call_rho = Label()

put_price = Label()
put_delta = Label()
put_gamma = Label()
put_vega = Label()
put_theta = Label()
put_rho = Label()

multiplier = Label ()


def bs_calc(event=None):
    global call_price, call_delta,call_gamma, call_vega, call_theta, call_rho, put_price, put_delta, put_gamma, put_vega, put_theta, put_rho, multiplier

    call_price.pack_forget()
    call_delta.pack_forget()
    call_gamma.pack_forget()
    call_vega.pack_forget()
    call_theta.pack_forget()
    call_rho.pack_forget()
    
    put_price.pack_forget()
    put_delta.pack_forget()
    put_gamma.pack_forget()
    put_vega.pack_forget()
    put_theta.pack_forget()
    put_rho.pack_forget()

    multiplier.pack_forget()

    option = BS(float(spot.get()), 
                int(strike.get()),
                float(rate.get()),
                int(days.get()),
                float(vol.get()),
                float(multiplier.get()))
    

    call_price = Label(call_frame,text=option.call_price(),fg="yellow",bg="purple")
    call_delta = Label(call_frame,text=option.call_delta(),fg="yellow",bg="purple")
    call_gamma = Label(call_frame,text=option.call_gamma(),fg="yellow",bg="purple")
    call_vega = Label(call_frame,text=option.call_vega(),fg="yellow",bg="purple")
    call_theta = Label(call_frame,text=option.call_theta(),fg="yellow",bg="purple")
    call_rho = Label(call_frame,text=option.call_ro(),fg="yellow",bg="purple")
  
    put_price = Label(put_frame,text=option.put_price(),fg="yellow",bg="purple")
    put_delta = Label(put_frame,text=option.put_delta(),fg="yellow",bg="purple")
    put_gamma = Label(put_frame,text=option.put_gamma(),fg="yellow",bg="purple")
    put_vega = Label(put_frame,text=option.put_vega(),fg="yellow",bg="purple")
    put_theta = Label(put_frame,text=option.put_theta(),fg="yellow",bg="purple")
    put_rho = Label(put_frame,text=option.put_ro(),fg="yellow",bg="purple")
    
    call_price.pack()
    call_delta.pack()
    call_gamma.pack()
    call_vega.pack()
    call_theta.pack()
    call_rho.pack()
    
    put_price.pack()
    put_delta.pack()
    put_gamma.pack()
    put_vega.pack()
    put_theta.pack()
    put_rho.pack()
    
    
root.bind('<Return>', bs_calc)

#Spot
spot_name = Label(root, text="Spot", bg = "purple", fg="white", font = 16, padx=15)
spot_name.grid(row=0, column=0, padx = 0, pady=5)

spot = Entry(root, fg="red", bg="yellow", borderwidth=5, font= 16, width = 10)
spot.grid(row=0,column=1)
spot.insert(0,1800)

# Strike
strike_name = Label(root,text="Strike",bg="black", fg="white", font = 16)
strike_name.grid(row = 1, column=0, padx = 0, pady=0)

strike=Entry(root,fg="white", bg="black", borderwidth=5, font = 16, width=10)
strike.grid(row=1,column=1)
strike.insert(0,1800)

#Rate
rate_name = Label(root, text='Risk-free rate ( decimal )', bg='black', fg='white', font=('Helvetica', 16))
rate_name.grid(row=2, column=0, pady=0)

rate = Entry(root, fg='white', bg='black', borderwidth=5, font=('Helvetica', 16), width=10)
rate.grid(row=2, column=1)
rate.insert(0, 0.01)

#Days
days_name = Label(root, text='Time to maturity (days)', bg='black', fg='white', font=('Helvetica', 16))
days_name.grid(row=3, column=0, pady=0)

days = Entry(root, fg='white', bg='black', borderwidth=5, font=('Helvetica', 16), width=10)
days.grid(row=3, column=1)
days.insert(0, 30)

#Vol
vol_name = Label(root, text='Volatility ( decimal )', bg='black', fg='white', font=('Helvetica', 16))
vol_name.grid(row=4, column=0, pady=0)

vol = Entry(root, fg='white', bg='black', borderwidth=5, font=('Helvetica', 16), width=10)
vol.grid(row=4, column=1)
vol.insert(0, 0.20)

#Multyplier
mult_name = Label(root, text='Option Multiplier', bg='black', fg='white', font=('Helvetica', 16))
mult_name.grid(row=5, column=0, pady=0)

multiplier = Entry(root, fg='white', bg='black', borderwidth=5, font=('Helvetica', 16), width=10)
multiplier.grid(row=5, column=1)
multiplier.insert(0, 100)

"------------------------------------------------"  

calculate_btn = Button(root,text="Calculate",
                         fg="green",
                         bg="purple",
                         font=16,
                         command=bs_calc)
calculate_btn.grid(row=6, column=1, pady=60)

"------------------------------------------------"
frame1=LabelFrame(root,padx=0,pady=0)
frame1.grid(row=7, column=1, rowspan=6)

call = Label(frame1,
              text="Call",
              width=5,
              font=("Ariel", 15, "underline"),
              fg="white",
              bg="purple")
call.grid(row=0, column=0)

put = Label(frame1,
          text="Put",
          width=5,
          font=("Ariel",15, "underline"), 
          fg="white",
          bg="purple")
put.grid(row=0,column=3)

"------------------------------------------"

call_frame = LabelFrame(frame1, width=40, height=20, bg="black")
call_frame.grid(row=1, column=0,rowspan=6)

put_frame = Label(frame1, width=40, height=20, bg="black")
put_frame.grid(row=1, column =3,rowspan=6)

"------------------------------------------"

price = Label(frame1, text="Price", font=16,fg="white",bg="purple")
price.grid(row=1, column=2)

delta = Label(frame1, text="Delta", font=16,fg="white",bg="purple")
delta.grid(row=2, column=2)

gamma = Label(frame1, text="Gamma", font=16,fg="white",bg="purple")
gamma.grid(row=3, column=2)

vega = Label(frame1, text="Vega", font=16,fg="white",bg="purple")
vega.grid(row=4, column=2)

theta = Label(frame1, text="Theta", font=16,fg="white",bg="purple")
theta.grid(row=5, column=2)

ro = Label(frame1, text="Ro", font=16,fg="white",bg="purple")
ro.grid(row=6, column=2)

"--------------------------------------"
marking=Label(root,
              text="Made by Harry Canty",
              fg="White",
              bg="orange",
              font=("Georgia",15),
              pady=12)

marking.grid(row=14,column=1)

def bs_calc ():
    a = 1


root.mainloop()