import pymysql
import hashlib
def get_book(search_key='',search_calss='书名',type='全部'):
    book=[]
    if search_key!='' and type!= '全部':
        if search_calss=='书名':
            sql='select title,writer,type from book where title="{}" and type="{}";'.format(search_key,type)
        else:
            sql = 'select title,writer,type from book where writer="{}" and type="{}";'.format(search_key, type)
    elif search_key!='':
        if search_calss=='书名':
            sql='select title,writer,type from book where title="{}";'.format(search_key)
        else:
            sql = 'select title,writer,type from book where writer="{}";'.format(search_key)
    elif type!= '全部':
        sql= 'select title,writer,type from book where type="{}";'.format(type)
    else:
        sql='select title,writer,type from book;'
    db = pymysql.connect(host='localhost',
                         port=3306, db='NOVEL',
                         user='root',
                         password='123456',
                         charset='utf8')
    cur = db.cursor()
    try:
        cur.execute(sql)
        book = cur.fetchall()
    except:
        pass
    cur.close()
    book= list(map(list, book))
    return book

def get_type():
    type=[]
    sql='select distinct(type) from book;'
    db = pymysql.connect(host='localhost',
                         port=3306, db='NOVEL',
                         user='root',
                         password='123456',
                         charset='utf8')
    cur = db.cursor()
    try:
        cur.execute(sql)
        type = list(cur.fetchall())
    except:
        pass
    cur.close()
    type = list(map(lambda x: x[0], type))
    type.insert(0,'全部')
    return type
def get_chapter_list(title):
    chapter=[]
    sql='select chaptertitle from book natural join chapter where title="{}";'.format(title)
    db = pymysql.connect(host='localhost',
                         port=3306, db='NOVEL',
                         user='root',
                         password='123456',
                         charset='utf8')
    cur = db.cursor()
    try:
        cur.execute(sql)
        chapter = cur.fetchall()
    except:
        pass
    cur.close()

    return chapter
def get_txt(title,chaptertitle):
    txt = []
    sql = 'select txt from book natural join chapter where title="{}" and chaptertitle="{}";'.format(title,chaptertitle)
    db = pymysql.connect(host='localhost',
                         port=3306, db='NOVEL',
                         user='root',
                         password='123456',
                         charset='utf8')
    cur = db.cursor()
    try:
        cur.execute(sql)
        txt = cur.fetchall()
    except:
        pass
    cur.close()

    return txt

def get_hash_password(password):
    sha = hashlib.sha1()
    sha.update(password.encode('utf-8'))
    password_hash = sha.hexdigest()
    return password_hash
