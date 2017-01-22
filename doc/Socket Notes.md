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
