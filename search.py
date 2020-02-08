import PySimpleGUI as sg
from backhome import get_book,get_type
def get_search():
    type_choose=get_type()
    search_in = sg.InputText('',key='input',size=(30,1))
    search_do = sg.Button('搜索',key='do',size=(20,1))
    search_read=sg.Button('阅读',key='read',size=(20,1))
    search_calss = sg.OptionMenu(('书名', '作者'),key='class', default_value='书名',size=(4,1))
    search_type = sg.OptionMenu(type_choose, key='type', default_value='全部', size=(8, 1))
    data = get_book()
    table = sg.Table(data, justification='center', headings=['书名', '作者', '类型'], display_row_numbers=True,
                     def_col_width=10, auto_size_columns=False,key='table')

    layout = [[search_in, search_calss,search_type],
              [search_do,search_read],
              [table]]
    window = sg.Window('搜索', layout,font=['微软雅黑','10','bold'])  # , default_element_size=(30, 2))
    return window,data
