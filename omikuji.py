import tkinter
import random

def click_btn():
    label["text"] = random.choice(["Phil_back", "Ronnie_back", "Jay_back", "Phil_front", "Ronnie_front", "Jay_front"])
    label.update()
    gazou2["file"] = "./Image/" + label["text"] + ".png"

root = tkinter.Tk()
root.title("おみくじソフト")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="./Image/oriba.png")
gazou2 = tkinter.PhotoImage(file="")
canvas.create_image(200, 300, image=gazou)
canvas.create_image(600, 300, image=gazou2)
label = tkinter.Label(root, text ="? ?", font=("Times New Roman", 30), bg="white")
label.place(x=500, y=60)
button = tkinter.Button(root, text="おみくじを引く", font=("Times New Roman", 36), command=click_btn, fg="skyblue")
button.place(x=400, y=500)
root.mainloop()