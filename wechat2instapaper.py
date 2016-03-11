#!/usr/bin/env python
# coding: utf-8

from wxbot import *
import instapaper

__author__= "Chanjh <jiahao0408@gmail.com>"

__dic__="""
This is a python wrapper for adding new url to the Instapaper.

http://github.com/chanjh
"""

class MyWXBot(WXBot):
    # 文本自动回复
    def handle_msg_all(self, msg):
        if msg['msg_type_id'] == 4 and msg['content']['type'] == 0:
            self.send_msg_by_uid(u"暂不支持保存文本", msg['user']['id'])
    def send_result(self, word, msg):
        self.send_msg_by_uid(word, msg['user']['id'])
    def instapaper(self, url, message):
        msg = message
        ipaper = instapaper.Instapaper('Your Consumer Key', 'Your Secret')
        ipaper.login('Username', 'Password')
        result,marks = ipaper.add(url)
        if result == 0:
            self.send_result(u"保存失败", msg)
            print u"保存失败"
        elif result == 1:
            self.send_result(u"保存成功", msg)
            print u"保存成功"


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'png'
    bot.run()


if __name__ == '__main__':
    main()
