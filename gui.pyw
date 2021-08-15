import tkinter as tk
import main
window = tk.Tk()
window.configure(background="black")
window.geometry("450x300")
window.title("ata11ata")

label = tk.Label(
    text="VALORANT INSTA-LOCKER",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
)
label.pack()

def helloCallBack():
    main.search(variable.get())
    print(variable.get())

button = tk.Button(window, text ="Start Searching", command = helloCallBack)
button.pack()

variable = tk.StringVar(window)
variable.set("jett")

w = tk.OptionMenu(window,variable,"astra","breach","brim","cypher","jett","kayu","killjoy","omen","phoneix","raze","reyna","sage","skye","sova","viper","yoru")
w.pack()

window.mainloop()