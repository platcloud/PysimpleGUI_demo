from login import get_login
from search import get_search
from backhome import get_book,get_hash_password,get_txt
from read import get_read_window
import PySimpleGUI as sg
login_window,users,data=get_login()
login_num=0
while True:
    event, value = login_window.read()
    if event == None or event == 'out':
        break
    elif event == 'user':
        login_window['password'].update(data[users.index(value['user'])]['load'])
    elif event == 'in':
        if value['user'] not in users:
            sg.PopupOK('用户未注册')
        else:
            password_hash = get_hash_password(value['password'])
            if password_hash == data[users.index(value['user'])]['password']:
                sg.PopupOK('登录成功！')
                login_num=1
                break
            else:
                sg.PopupOK('登陆失败！')
login_window.close()
del login_window
if login_num==1:
    search_window, book_data = get_search()
    while True:
        event, value = search_window.read()
        if event == None:
            break
        if event == 'do':
            book_data = get_book(value['input'], value['class'], value['type'])
            search_window['table'].update(book_data)
        if event == 'read':
            search_window.Hide()
            try:
                title = book_data[value['table'][0]][0]
                read_window = get_read_window(title)
                while True:
                    event_1, value_1 = read_window.read()
                    if event_1 == None:
                        break
                    elif event_1 == 'list':
                        txt = get_txt(title, value_1['list'][0])
                        read_window['txt'].update(txt)
                read_window.close()
                del read_window
            except:
                sg.PopupOK('请您先选择书籍！')
            search_window.UnHide()
    search_window.close()
    del search_window
