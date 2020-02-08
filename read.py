import PySimpleGUI as sg
from backhome import get_chapter_list,get_txt
def get_read_window(title):
    chapter = get_chapter_list(title)
    chapter = tuple(map(lambda x: x[0], chapter))
    chapter_list = sg.Listbox(values=chapter, enable_events=True, size=(30, 28), key='list')
    txt = get_txt(title, chaptertitle=chapter[0])
    text_out = sg.Multiline(txt, size=(40, 30), key='txt')
    layout = [[chapter_list, text_out]]
    window = sg.Window('阅读', layout,font=['微软雅黑',10])  # , default_element_size=(30, 2))
    return window
