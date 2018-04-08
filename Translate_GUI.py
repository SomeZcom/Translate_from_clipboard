from tkinter import *
from BaiduTranslate import BaiduFanyi
import time

class LanguageFrom:
    
    def zh():
        print('翻译源为汉语！')
        lg_from.set('zh')
    def en():
        print('English')
        lg_from.set('en')
    def jp():
        lg_from.set('jp')
    def ru():
        lg_from.set('ru')
        
class LanguageTo:
    
    def zh():
        print('翻译源为Chinese！')
        lg_to.set('zh')
    def en():
        print('英文')
        lg_to.set('en')
    def jp():
        lg_to.set('jp')
    def ru():
        lg_to.set('ru')
        
        
lgf = LanguageFrom
lgt = LanguageTo


def start_translate(event):
    try:
        cb = root.clipboard_get()
        print(cb)
        B = BaiduFanyi(cb, lg_from.get(), lg_to.get())
        B.run()
        means = B.trans_res
        str_view = cb + '\n' + means
        text.delete(1.0, END)
        text.insert(1.0, str_view)
    except:
        text.delete(1.0, END)
        text.insert(1.0, '剪切板为空或不是正确的单词！！！')

languages_from = {
    '中文':lgf.zh,
    '英语':lgf.en,
    '日语':lgf.jp,
    '俄语':lgf.ru,
    }

languages_to = {
    '中文':lgt.zh,
    '英语':lgt.en,
    '日语':lgt.jp,
    '俄语':lgt.ru,
    }

def add_menu():
    menubar = Menu(root)
    lgf_menu = Menu(menubar, tearoff=0)
    lgf_menu.add_separator()
    for lg in languages_from:
        lgf_menu.add_command(label=lg, command=languages_from[lg])
    menubar.add_cascade(label='TranslateFrom', menu=lgf_menu)
    lgt_menu = Menu(menubar, tearoff=0)
    lgt_menu.add_separator()
    for lg in languages_to:
        lgt_menu.add_command(label=lg, command=languages_to[lg])
    menubar.add_cascade(label='TranslateTo', menu=lgt_menu)
    root['menu'] = menubar

def get_text_trans(event):
    try:
        trans_word = trans_text.get(1.0, END).split('\n')[0]
        print(trans_word)
        B = BaiduFanyi(trans_word, lg_from.get(), lg_to.get())
        B.run()
        means = B.trans_res
        str_view = trans_word + '\n' + means
        text.delete(1.0, END)
        text.insert(1.0, str_view)
    except:
        text.delete(1.0, END)
        text.insert(1.0, 'Error!!!')

root = Tk()
root.geometry('900x550+100+100')
root.title('专注翻译 为你而生')

lg_from = StringVar()
lg_to = StringVar()
lg_from.set('en')
lg_to.set('zh')

add_menu()
    
trans_text = Text(root, width='65', height='12')
trans_text.insert(1.0, 'input...')
trans_text.place(x=0, y=0, anchor=NW)


img1 = PhotoImage(file='fy.gif')
img2 = PhotoImage(file='tj.gif')

button_entry = Button(root, text='提交', width='120', height='169', image=img2)
button_entry.bind('<Button-1>', get_text_trans)
button_entry.place(x=480, y=0, anchor=NW)

button = Button(root, text='Translate', width='250', height='169', image=img1)
button.bind('<Button-1>', start_translate)
button.place(x=620, y=0, anchor=NW)
text = Text(root, width=800, height=400)
text.place(x=0, y=210, anchor=NW)



root.mainloop()
    



