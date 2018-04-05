from tkinter import *
from BaiduTranslate import BaiduFanyi
import time

root = Tk()

while True:
    try:
        cb = root.clipboard_get()
        print(cb)
        B = BaiduFanyi(cb)
        B.run()
    except:
        print('剪切板为空 or 不是正确的单词')
    time.sleep(1)
 
root.destroy()
    
root.mainloop()


