# @Author  :  lijishi
# @Contact :  lijishi@emails.bjut.edu.cn
# @Software:  Pycharm & Python 3.7
# @EditTime:  Jan 6, 2020
# @Version :  1.0
# @describe:  Realize IP Adress Query
# @LICENSE :  GNU GENERAL PUBLIC LICENSE Version 3

# Thanks
# https://ip.cn/
# http://freeapi.ipip.net/

# References
# https://blog.csdn.net/qq_27378621/article/details/88828581
# https://blog.csdn.net/lion_cui/article/details/51329497

import requests
import base64
import re
import os
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
from tkinter import *
from picture import Icon
from picture import Gif

def GetLocalIP():

    html_text = requests.get("https://ip.cn/").content.decode("utf-8")
    for index_start in range(0, len(html_text)):
        if  html_text[index_start: index_start+7] == "Your IP":
            break;
    index_end = index_start+16

    for index_end in range(index_start+16, len(html_text)):
        if  html_text[index_end] == "<":
            break;

    local_ip.set(html_text[index_start+16: index_end])
    find_ip.set(html_text[index_start+16: index_end])
    GetIP()

def GetIP():
    url='http://freeapi.ipip.net/'
    ip=find_ip.get()
    response = requests.post(url+ip)
    responsetext = response.content.decode("utf-8")
    address = ''
    company = ''
    index = 0
    num = 0
    index_start = 0
    index_end = 0
    while True:
        if responsetext == '\"not found\"':
            Error()
            break
        if responsetext[index] == '\"':
            if num == 4:
                for temp in range(index+1, len(responsetext)):
                    if responsetext[temp] != '\"':
                        company += responsetext[temp]
                    else:
                        break
                break
            index += 1
            index_start = index
            for temp in range(index_start, len(responsetext)):
                if responsetext[temp] == '\"':
                    index_end = temp
                    index = temp+1
                    address += responsetext[index_start: index_end]
                    address += ' '
                    num += 1
                    index_start = 0
                    index_end = 0
                    break
        index += 1

    ip_address.set(address)
    ip_company.set(company)

def About():
    # window centered
    about_window = Toplevel()
    screen_width = about_window.winfo_screenwidth()
    screen_heigh = about_window.winfo_screenheight()
    about_window_width = 420
    about_window_heigh = 340
    x = (screen_width - about_window_width) / 2
    y = (screen_heigh - about_window_heigh) / 2
    about_window.geometry("%dx%d+%d+%d" % (about_window_width, about_window_heigh, x, y))

    # window layout
    global cha_gif
    about_window.title('About')
    with open('tmp.ico', 'wb') as tmp:
        tmp.write(base64.b64decode(Icon().img))
    about_window.iconbitmap('tmp.ico')
    os.remove('tmp.ico')
#    about_window.iconbitmap(".\\cha.ico")
    with open('tmp.gif', 'wb') as tmp:
        tmp.write(base64.b64decode(Gif().img))
#    about_window.iconbitmap('temp.gif')
    cha_gif = tk.PhotoImage(file="tmp.gif")

#    os.remove('temp.gif')
#    cha_gif = tk.PhotoImage(file=".\\cha.gif")
    software_frame = ttk.LabelFrame(about_window, text='Software Info')
    software_frame.grid(row=0, column=0, rowspan=5, columnspan=4, padx=50, pady=5)
    ttk.Label(software_frame, image=cha_gif, compound='left').grid(row=0, rowspan=3, column=0)
    os.remove('tmp.gif')
    ttk.Label(software_frame, text="IP Query Version 1.0").grid(row=0, column=1, sticky = W)
    ttk.Label(software_frame, text="@Author    :   lijishi").grid(row=1, column=1, sticky = W)
    ttk.Label(software_frame, text="@EditTime  :   Jan 5,2020").grid(row=2, column=1, sticky = W)

    copyright_frame = ttk.LabelFrame(about_window, text='LICENSE Info')
    copyright_frame.grid(row=5, column=0, rowspan=3, columnspan=4, padx=50, pady=5)
    ttk.Label(copyright_frame, text = "Github @ IP_Query").grid(row=5, column=0)
    ttk.Label(copyright_frame, text="GNU GENERAL PUBLIC LICENSE Version 3").grid(row=6, column=0)

    thanks_frame = ttk.LabelFrame(about_window, text='Thanks Info')
    thanks_frame.grid(row=8, column=0, rowspan=3, columnspan=4, padx=50, pady=5)
    ttk.Label(thanks_frame, text="IP Get Powered By ip.cn").grid(row=8, column=0)
    ttk.Label(thanks_frame, text="IP Query Powered By ipip.net").grid(row=9, column=0)

def Tips():
    tk.messagebox.showinfo("Tips", "IP查询支持IPV4/6 \n单日查询最高1000次 \n不确保数据准确性")

def Error():
    tk.messagebox.showerror("Error", "IP地址有误，请重试")

# window centered
main_window=tk.Tk()
screen_width = main_window.winfo_screenwidth()
screen_heigh = main_window.winfo_screenheight()
main_window_width = 365
main_window_heigh = 110
x = (screen_width-main_window_width) / 2
y = (screen_heigh-main_window_heigh) / 2
main_window.geometry("%dx%d+%d+%d" %(main_window_width,main_window_heigh,x,y))

# window layout
main_window.title("IP Query V1.0")
with open('tmp.ico', 'wb') as tmp:
    tmp.write(base64.b64decode(Icon().img))
main_window.iconbitmap('tmp.ico')
os.remove('tmp.ico')
#main_window.iconbitmap(".\\cha.ico")
local_ip = tk.StringVar()
find_ip = tk.StringVar()
ip_address = tk.StringVar()
ip_company = tk.StringVar()
ttk.Label(main_window, text = "本机IP：").grid(row = 0, column = 0, padx=10)
ttk.Entry(main_window, width = 25, textvariable = local_ip).grid(row = 0, column = 1, padx=5)
ttk.Button(main_window, width = 10, text = "获取", command = GetLocalIP).grid(row = 0, column = 2, padx=10)
ttk.Label(main_window, text = "查询IP：").grid(row = 1, column = 0, padx=10)
ttk.Entry(main_window, width = 25, textvariable = find_ip).grid(row = 1, column = 1, padx=5)
ttk.Button(main_window, width = 10, text = "查询", command = GetIP).grid(row = 1, column = 2, padx=10)
ttk.Label(main_window, text = "地区：").grid(row = 2, column = 0, padx=10)
ttk.Label(main_window, width = 25, textvariable = ip_address).grid(row = 2, column = 1, padx=10)
ttk.Label(main_window, text = "运营商：").grid(row = 3, column = 0, padx=10)
ttk.Label(main_window, width = 25, textvariable = ip_company).grid(row = 3, column = 1, padx=10)
ttk.Button(main_window, width = 10, text = "提示", command = Tips).grid(row = 2, column = 2, padx=10)
ttk.Button(main_window, width = 10, text = "关于", command = About).grid(row = 3, column = 2, padx=10)

main_window.mainloop()