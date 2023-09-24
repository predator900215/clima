import requests
from tkinter import Tk, Frame, Label, Entry, Button


def obtener_clima():
    apikey = "cf30d70617715c47c722a96024bd2340"
    ciudad = entrada.get()
    idioma = "es"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&APPID={}&lang={}".format(ciudad, apikey, idioma)
    res = requests.get(url)
    data = res.json()

    kelvin_temp = data["main"]["temp"]
    celsius_temp = kelvin_temp - 273.15

    descripcion = data["weather"][0]["description"]

    label_text = f"{celsius_temp:.2f} °C"
    label.configure(text=label_text)

    label2.configure(text=descripcion)


ventana = Tk()
ventana.title("CLIMA")
ventana.geometry("300x300")
frame = Frame(ventana, bg="#CAEDFF")
frame.place(x=0, y=0, width=300, height=300)

entrada = Entry(frame, justify="center", font=("Arial", 14, "bold"), borderwidth=3)
entrada.place(x=20, y=20, width=260, height=40)

boton = Button(frame, text="Obtener", font=("Arial", 14, "bold"), command=obtener_clima)
boton.place(x=100, y=70, width=100, height=40)

label = Label(frame, font=("Arial", 40, "bold"), bg="#CAEDFF")
label.place(x=50, y=160, width=200, height=60)

label2 = Label(frame, font=("Arial", 14, "bold"), bg="#CAEDFF")
label2.place(x=50, y=240, width=200, height=40)

ventana.mainloop()
