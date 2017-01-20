# Install Env

Python 3.6 有的接口改掉了，所以寫點筆記紀錄一下

使用上，Add the `Python -m` to be prefix

`Python -m pip`

## venv

- [3.6 venv](https://docs.python.org/3/library/venv.html)

使用方法

3.6

`python3 -m venv /path/to/new/virtual/environment`

3.5

`virtualenv venv`

呼叫方法

`<venv>\Scripts\activate.bat`

## Run Flask Fail

錯誤訊息

	ImportError: No module named 'SocketServer'

	During handling of the above exception, another exception occurred:

	Traceback (most recent call last):
	  File "C:/Users/jowu/Desktop/PyWeb/PyWeb.py", line 12, in <module>
	    app.run()
	  File "C:\Users\jowu\AppData\Local\Programs\Python\Python36\lib\site-packages\flask\app.py", line 828, in run
	    from werkzeug.serving import run_simple
	  File "C:\Users\jowu\AppData\Local\Programs\Python\Python36\lib\site-packages\werkzeug\serving.py", line 68, in <module>
	    from socketserver import ThreadingMixIn, ForkingMixIn
	ImportError: cannot import name 'ForkingMixIn'

[原因](https://segmentfault.com/q/1010000006148765) Socketserver 的接口被改掉了

不知道後面還有多少雷，直接跳回 3.5

## Resource

- [舊版的介紹](http://www.cnblogs.com/Ray-liang/p/4173923.html?utm_source=tuicool&utm_medium=referral)

