from tkinter import *
from BaiduTranslate import BaiduFanyi
import time

root = Tk()
root.geometry('800x450+100+100')
v = StringVar()
flag = True
while True:
    try:
        cb = root.clipboard_get()
        print(cb)
        B = BaiduFanyi(cb)
        B.run()
        means = B.trans_res
        print(means)
    except:
        print('剪切板为空 or 不是正确的单词')
    v.set(means)
    text = Text(root, width=500, height=450)
    text.insert(1.0, means)
    text.pack()
    time.sleep(1)
    if flag:
        root.mainloop()
        flag = False
    
 
#root.destroy()
    



