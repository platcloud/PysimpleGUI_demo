import PySimpleGUI as sg
import json
#定义登录界面
#返回窗口，用户集，用户信息
def get_login():
    #打开用户信息
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    sg.theme('DarkBlack')#主题，只要出现一次所有窗口的主题都会改变
    users = []
    user_default_value = ''
    remember_default = False
    password_default_text = ''
    if data:
        for i in range(len(data)):
            users.append(data[i]['user'])
        user_default_value = data[0]['user']
        if data[0]['记住密码']:
            remember_default = True
            password_default_text = data[0]['load']
    layout = [[sg.T('用户名', size=(5, 1)),
               sg.Combo(values=users, default_value=user_default_value, key='user', size=(21, 1), enable_events=True)],
              [sg.T('密码', size=(5, 1)),
               sg.In(key='password', default_text=password_default_text, size=(23, 1), password_char='#')],
              [sg.CBox('记住密码', default=remember_default, size=(12, 1), key='remember', enable_events=True),
               sg.CBox('自动登录', size=(12, 1), key='auto')],
              [sg.Button('登录', size=(12, 2), key='in'), sg.Button('退出', size=(12, 2), key='out')]]
    window = sg.Window('登录', layout=layout, auto_size_text=True,alpha_channel=.8,font=['微软雅黑','10','bold'],
                       text_justification='c', return_keyboard_events=True, grab_anywhere=False)
    return window,users,data
