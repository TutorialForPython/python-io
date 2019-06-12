# 快速实现RESTful接口服务

python有很多优秀的web框架,但个人最喜欢的还是[sanic](https://github.com/huge-success/sanic)这时一个基于python3.5+新特性协程的异步框架,其接口设计参照了同样受欢迎的[flask](http://flask.pocoo.org/)但它比flask更加轻量,由于协程的作用,其并发性能更强.而且并不需要借助其他http组件就可以单独运行,甚至于它还可以多进程启动.当然相对的它的生态比flask差的多,但作为一个Restful接口服务它已经很够用了.

如果更加偏爱同步接口,那flask依然是最稳妥的选择,它足够轻量,也有足够的插件支持,非常适合快速实现.配合gevent也可以轻松异步.

## 利用flask构造同步的接口服务



首先是一个[helloworld]()项目,我们来看看如何用sanic构造Restful接口

## 利用sanic构造异步的接口服务

