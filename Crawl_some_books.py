from lxml import html
import requests
import pymysql
db=pymysql.connect(host='localhost',
                   port=3306,db='NOVEL',
                   user='root',
                   password='123456',
                   charset='utf8')
cur=db.cursor()
for i in range(1,2):#大页
    request = requests.get('http://www.ybdu.co/book/allvisit-{}.html'.format(i))
    sel=html.fromstring(request.content)
    title=sel.xpath('//li[@class="articlename"]/a/text()')#标题
    bookwriter=sel.xpath('//li[@class="author"]/a/text()')#作者
    url=sel.xpath('//li[@class="articlename"]/a/@href')#本体url
    for j in range(len(title)):#每页的每本书
        sel_1=html.fromstring(requests.get(url[j]).content)
        src = 'http://www.ybdu.co' + sel_1.xpath('//div[@class="info1"]/img/@src')[0]  # 图片
        type = sel_1.xpath('//div[@class="info2"]/h3[2]/text()')[0][3:7]#类型
        chapters_urls = sel_1.xpath('//ul[@class="list-group list-charts"]/li/a/@href')
        chapters_titles = sel_1.xpath('//ul[@class="list-group list-charts"]/li/a/text()')
        sql = 'insert into book values("{}","{}","{}","{}","{}");'.format(url[j],title[j],bookwriter[j],type,src)
        try:
            cur.execute(sql)
            print(i, j, '成功导入')
            db.commit()
        except:
            print(i, j, '导入错误')
            db.rollback()
        for k in range(10):#前十章
            chapters_urls[k]='http://www.ybdu.co'+chapters_urls[k]
            sel_2 = html.fromstring(requests.get(chapters_urls[k]).content)
            text = sel_2.xpath('//div[@class="panel-body content-body content-ext"]/text()')
            sql = 'insert into chapter values("{}","{}","{}","{}");'.format(url[j],chapters_urls[k],chapters_titles[k],text)
            try:
                # 执行sql
                cur.execute(sql)
                print(i,j,k,'章节成功导入')
                db.commit()
            except:
                # 发生错误时回滚
                print(i,j,k,'章节导入错误')
                db.rollback()
cur.close()
