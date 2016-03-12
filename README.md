# 1.Based on

[wxbot frame][1]

[instapaper ][2]

# 2.Environment

Python 2.7

Modules: os、sys、urllib2、urlparse、simplejson、oauth2、lxml、urllib、HTMLParser、re、sys、traceback

# 3.Install

```
$ git clone git://github.com/chanjh/wechat2instapaper
$ cd wechat2instapaper
```

# 4.Code & conf

You should change 
```
ipaper = instapaper.Instapaper('Your Consumer Key', 'Your Secret')
ipaper.login('Username', 'Password')
```
in wechat2instapaper.py into your own Instapaper data.
You can get consumer key in: [Register New OAuth Application][3]

# 5.Run

``$ python wechat2instapaper.py``

Use WeChat to scan the  QR code named qr.png and confirm to login.

# 6.Share

Use another WeChat account to send a link to the logined account.And it would save your link to Instapaper.

# 7.More

Learn more about me and my project on my blog: [ChanTalk][4]


[1]:	https://github.com/liuwons/wxBot
[2]:	https://github.com/rsgalloway/instapaper
[3]:	https://www.instapaper.com/main/request_oauth_consumer_token
[4]:	http://chanjh.com/