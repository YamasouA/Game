import tkinter
root = tkinter.Tk()
root.title("初キャンバス")
canvas = tkinter.Canvas(root, width=600, height=600)
canvas.pack()
#jpgは読み込めなかった
gazou = tkinter.PhotoImage(file="lena.png")
canvas.create_image(200, 300, image=gazou)
root.mainloop()