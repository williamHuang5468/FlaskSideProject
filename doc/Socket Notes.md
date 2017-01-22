# Socket Notes

## 這是什麼?

為了練習寫一個 Chat room 作的筆記

## 收集資料

Google `pythton socket chat server`

找到別人已經寫好的教學

- [Python socket – chat server and client with code example](http://www.binarytides.com/code-chat-application-server-client-sockets-python/)
    - [Basic Knowledge](http://www.binarytides.com/python-socket-programming-tutorial/)
## Content

兩部分 Server and Client

### Server

作兩件事:從 Client 收多個 Connect，收訊息且廣播給其他 Client

開 5000 port 去接收 connections

Server 怎麼處理多個 Client?

> 用 select ，他可以觀察所有 client sockets 和 master socket 的 activity
> 
> client 會寄送訊息，作為 activity

### Read Code

從 broadcast_data 開始看，已經知道 Server 會收到訊息之後，傳給其他 Client

```Python
def broadcast_data (sock, message):
    #Do not send the message to master socket and the client who has send us the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                CONNECTION_LIST.remove(socket)
```

傳了 `sock`和 `message` 進來，sock 估計是 client socket ， message 則是要傳的訊息。

> 資訊: master socket 指的應該是 server socket ，另一個是傳出訊息的 client 要避免掉。
> 
> eg. 如果我發了一則訊息，Server 收到，要避免 broadcast 給我自己，否則會有回音的效果XD。

- 從 `CONNECTION_LIST` 拿到所有的 Connection
- 發送訊息，但跳過 Server Socket 和 發出訊息的 Client 
    - 有問題 eg. `ctrl+c`關程式，先把 socket 關了，和從 pool 中移除

-----------
到 Main 裡頭看，發現 RECV_BUFFER ，猜測是重新嘗試的次數

socket 的宣告方式，查[官方文件](https://docs.python.org/3.5/library/socket.html#socket.AF_INET6)，用法也是差不多
```Python
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)
```

- 什麼是 `AF_INET` `SOCK_STEAM`?
- 幹什麼用的?

