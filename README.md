# Wechat2instapaper

## Version 0.2
## Update:
* 1.Change the frame into [WeixinBot][1].
* 2.Add a new command “#insta” to push all your links to your instapaper.
* 3.Add a new command “#list” whose function is able to show all your items.
* 4.Add a new command “#del”+number whose function is able to delect the item of your list.
* 5.Add a new command “#num” whose function is able to show the number of your list.


## 1.Based on

[WeixinBot][2]

[instapaper ][3]

## 2.Environment

Python 2.7



## 3.Install

```
$ git clone git://github.com/chanjh/wechat2instapaper
$ cd wechat2instapaper
```

## 4.Code & conf

You should change 
```
ipaper = instapaper.Instapaper('Your Consumer Key', 'Your Secret')
ipaper.login('Username', 'Password')
```
in wechat2instapaper.py into your own Instapaper data.
You can get consumer key in: [Register New OAuth Application][4]

## 5.Run

`$ python wechat2instapaper.py`

Use WeChat to scan the  QR code and confirm to login.

## 6.Share

Use another WeChat account to send a link to the logined account.And then when you send "#insta" to it,it would save all your links to Instapaper.

## 7.More

Learn more about me and my project on my blog: [ChanTalk][5]


[1]:	https://github.com/Urinx/WeixinBot
[2]:	https://github.com/Urinx/WeixinBot
[3]:	https://github.com/rsgalloway/instapaper
[4]:	https://www.instapaper.com/main/request_oauth_consumer_token
[5]:	http://chanjh.com/