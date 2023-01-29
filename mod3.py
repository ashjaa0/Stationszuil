from tkinter import *
import psycopg2
import requests
import tkinter as tk
from tkinter import messagebox

con = psycopg2.connect(
    host="localhost",
    database="zuil",
    user="postgres",
    password="12345")
def time_now():
    from datetime import datetime
    time = datetime.now()
    timenow = time.strftime("%D  %H:%M")
    return timenow



def ST():
    import random
    STR_list = ['Arnhem', 'Almere', 'Amersfoort', 'Almelo', 'Alkmaar', 'Apeldoorn', 'Assen', 'Amsterdam', 'Boxtel',
                'Breda', 'Dordrecht', 'Delft', 'Deventer', 'Enschede', 'Gouda', 'Groningen', 'Den Haag', 'Hengelo',
                'Haarlem', 'Helmond', 'Hoorn', 'Heerlen', 'Den Bosch', 'Hilversum', 'Leiden', 'Lelystad', 'Leeuwarden',
                'Maastricht',
                'Nijmegen', 'Oss','Roermond', 'Roosendaal',
                'Sittard', 'Tilburg', 'Utrecht', 'Venlo', 'Vlissingen', 'Zaandam', 'Zwolle', 'Zutphen']
    STR = (random.choice(STR_list))
    return STR
sh=ST()


url='https://api.openweathermap.org/data/2.5/weather?q={}&appid=7bc0f0159719a1ecb3fd3a3d524fbfaa'.format(ST())
res=requests.get(url)
data=res.json()

temp=round(float(data["main"]["temp"] - 273.15))
currentFeelsLike = round(float(data["main"]["feels_like"] - 273.15))
wither=data['weather'][0]['description']


window=tk.Tk()
window.title("NS SH")
window.configure(background="#FFD533")
window.geometry("1300x900")
photo1=PhotoImage(file="NS1.gif")
photo2=PhotoImage(file="img_pr.png")
photo3=PhotoImage(file="img_lift.png")
photo4=PhotoImage(file="img_toilet.png")
photo5=PhotoImage(file="img_ovfiets.png")
pho=Label (master=window, image=photo1, bg="#FFD533")
pho.pack(pady=10,padx=10,fill=tk.X)
sti=Label(master=window, text=f"Welkom in ST {sh} ",background="#FFD533",fg="black",font="none 45 bold")
sti.pack(anchor=CENTER)

time=Label(window, text=( f'{time_now()}') ,font=('NS Sans Regular', 25),background='#FFD533',)
time.pack(anchor=W)
weer1=Label(window, text=( f'weer:{temp}°C ') ,font=('NS Sans Regular', 25),background='#FFD533',)
weer2=Label(window, text=( f'voelt als:{currentFeelsLike}°C') ,font=('NS Sans Regular', 25),background='#FFD533',)
weer3=Label(window, text=( f'beschrijving weer:{wither}') ,font=('NS Sans Regular', 25),background='#FFD533',)
weer1.pack(anchor=W)
weer2.pack(anchor=W)
weer3.pack(anchor=W)

# fas:
cur = con.cursor()
cur.execute(f"SELECT * FROM station_service WHERE station_city='{sh}';")
rijen = cur.fetchall()
for fa in rijen:
    ov_bike = fa[2]
    elevator = fa[3]
    toilet = fa[4]
    park_and_ride = fa[5]
def ov():
     messagebox.showinfo("fiets", f"{ov_bike}")
def eleva():
    messagebox.showinfo("lift", f"{elevator}")
def toi():
    messagebox.showinfo("toilet", f"{toilet}")
def park():
    messagebox.showinfo("pr", f"{park_and_ride}")



def berchten():
    cur = con.cursor()
    cur.execute(f"SELECT naam,bericht FROM berichten ORDER BY datum DESC LIMIT 5;")
    rijen = cur.fetchall()
    for review in rijen:
        name = review[0]
        message = review[1]
        # messagebox.showinfo("berchten", f"{name}- review: {message}")
        review_label = Label(window, text=". "+f"{name} - review: {message}",font=('NS Sans Regular', 23,),background='#FFD533',)
        review_label.pack(ipadx=5, ipady=5,anchor=W)
    cur.close()
    con.close()




btn=Button(window, text="Berichten",font=('NS Sans Regular', 25,), command=berchten, padx=20, pady=20)
btn.pack(anchor=CENTER)
btn1=tk.Button(window, image=photo5,command=ov,width=100, height=100)
btn1.pack(ipadx=5, ipady=5 ,side=tk.RIGHT,anchor=SE)
btn2=tk.Button(window, image=photo2,command=park,width=100, height=100)
btn2.pack(ipadx=5, ipady=5 ,side=tk.RIGHT,anchor=SE)
btn3=tk.Button(window, image=photo4,command=toi,width=100, height=100)
btn3.pack(ipadx=5, ipady=5 ,side=tk.RIGHT,anchor=SE)
btn4=tk.Button(window, image=photo3, command=eleva,width=100, height=100)
btn4.pack(ipadx=5, ipady=5 ,side=tk.RIGHT,anchor=SE)

window.mainloop()



