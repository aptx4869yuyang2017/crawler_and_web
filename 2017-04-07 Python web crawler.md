



# 构建 维度与逆运算的思考
初级爬虫 与 初级网页制作
框架爬虫scrapy 与web应用框架 Django
写作 与  网络协议
网上教程那么多，有的是学习笔记，有的真心是操作指南，我想写点不一样的

# HTML CSS 知识

# HTTP协议


![](./_image/基本流程图-2.png)

了解了HTTP协议和HTML文档，我们其实就明白了一个Web应用的本质就是：

* 浏览器发送一个HTTP请求；
* 服务器收到请求，生成一个HTML文档；
* 服务器把HTML文档作为HTTP响应的Body发送给浏览器；
* 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

# 利用python 运行你的第一个网站然后爬取它
### 第一个页面读取

```python
#!/usr/bin/env python 
#coding:utf-8 

import web

urls = (
'/', 'index'
)

class index:
    def GET(self):
        return "Hello, world!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
```

```python
#!/usr/bin/env python 
#coding:utf-8 
import urllib2  
response = urllib2.urlopen('http://0.0.0.0:8080/')  
html = response.read()  
print html 
```


![](./_image/web.png)
![](./_image/read.png)
