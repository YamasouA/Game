import tkinter

def click_btn():
    button["text"] = "クリックしました"

root = tkinter.Tk()
root.title("初ボタン")
root.geometry("800x600")#windowサイズ
label = tkinter.Label(root, text="ラベルの文字列", font=("System", 24))
button = tkinter.Button(root, text="ボタンの文字列", font=("Times New Roman", 24), command=click_btn)
button.place(x=200, y=300)
label.place(x=200, y=100)

root.mainloop()