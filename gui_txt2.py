import tkinter

def click_btn():
    text.insert(tkinter.END, "モンスターが現れた!")

def check():
    if cval.get():
        print("チェックされています")
    else:
        print("チェックされていません")

root = tkinter.Tk()
root.title("複数行のテキスト入力")
root.geometry("400x200")
button = tkinter.Button(text="メッセージ", command=click_btn)
button.pack()
cval = tkinter.BooleanVar()
cval.set(False)
cbtn = tkinter.Checkbutton(text="チェックボタン", variable=cval, command=check)
cbtn.pack()
text = tkinter.Text()
text.pack()
root.mainloop()