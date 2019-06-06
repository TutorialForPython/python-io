# 使用python搭建后端服务

python在很早就已经是一个可以用于开发后端服务的语言,像豆瓣知乎在开始的时候都是使用python写的,历史上也出现过许多广受欢迎的web框架.
而现在微服务架构盛行,python自然不会在这个传统领域落后于人.

## python在后端开发中的角色

在前后端分离成为趋势之前python在服务中的角色定位和php,C#的.net差不多,使用经典的[MVC]架构设计,需要依赖一套html模板系统作为前端,比如[jinja2](http://jinja.pocoo.org/),搭配服务器中间件进行部署,比如[guncorn](https://gunicorn.org/),[uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/),或者通过猴子补丁用[gevent](http://www.gevent.org/)这类协程库替换掉线程库然后执行其独立wsgi容器.

这种类型的任务常见的框架有[django](https://www.djangoproject.com/)和[flask](http://docs.jinkan.org/docs/flask/).本文不对这种类型的技术做过多介绍,感兴趣的可以买本[Flask Web开发：基于Python的Web应用开发实战](http://www.ituring.com.cn/book/1449)看看,这本书全书围绕一个例子对于这种类型的技术做了相当好的介绍,看完这类任务基本就可以自己去做了.

而在在前后端分离成为主流,微服务盛行的今天,结合python自身特点,python在服务端的角色更多的是:

+ 快速原型实现服务接口
+ 结合python的数据处理能力提供RPC服务

本文将介绍

+ 快速实现RESTful接口服务
+ 快速实现Websocket服务
+ GRpc提供的接口服务

而后端相关的技术有:

+ 关系数据库技术,常见的有[PostgreSQL](http://www.postgres.cn/docs/10/),业务上一般使用orm来操作数据库.我们使用基于[peewee](https://github.com/coleifer/peewee)的异步版本[peewee-async](https://github.com/05bit/peewee-async),配合[aiopg](https://github.com/aio-libs/aiopg)来使用虽然我个人也封装过一个类似的aioorm,但由于peewee做了大版本更新而我也懒得跟进,所以就不多介绍了.
+ 共享内存技术,常见的是Redis,我们使用[aioredis](https://github.com/aio-libs/aioredis)
+ 消息队列技术,常见的有rabbitMQ,我们使用[aio-pika](https://github.com/mosquito/aio-pika)
+ 消息的发布订阅工具,常见的有Redis,rabbitMQ,postgreSQL
+ [aiortc](https://github.com/aiortc/aiortc)一个webrtc的python实现
+ [zmq](http://zeromq.org/)一种跨语言的基于通信模式的消息队列框架