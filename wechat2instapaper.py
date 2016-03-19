#!/usr/bin/env python
# coding: utf-8

# from wxbot import *
from weixin import *
import instapaper
import types

__author__= "Chanjh <chanjh.com>"

__dic__="""
This is a python wrapper for adding new url to the Instapaper.

http://github.com/chanjh
"""

class MyWXBot(WebWeixin):

	def messageHandle(self, msgBox, content, name):
		if content == "#insta":
			self.sendAll2insta(msgBox, name)
			self.sendMsg(name, "Success!")
		elif content == "#list":
			self.showAllTheContent(msgBox, name)
		elif content[0:4] == "#del":
			try:
				word = msgBox[ int(content[4:]) ]
				del msgBox[ int(content[4:]) ]
				self.sendMsg(name, content[4:] + ".已删除")
			except:
				self.sendMsg(name, "You cannot delect songthing out of range!")
		elif content == "#num":
			self.sendMsg(name, "一共保存【" + str(len(msgBox)-1) + "】条目")
		else:
			self.storeTheTextInBox(content, msgBox)
			return msgBox

	def showAllTheContent(self, msgBox, name):
		for i in range(1,len(msgBox)):
			if type(msgBox[i]) is types.StringType or types.DictType:
				if type(msgBox[i]) is types.StringType:
					word = str(i) + "." + msgBox[i]
				else:
					word = str(i) + "." + "【标题】：\n" + msgBox[i]['fileName'] + "\n【链接】：\n" + msgBox[i]['url']
				self.sendMsg(name, word)
			else:
				pass
					


	def storeTheTextInBox(self, content, msgBox):
		msgBox.append(content)
		return msgBox

	def storeTheSharingInBox(self, fileName, url, msgBox):
		urlDetail = {'fileName':fileName, 'url':url}
		msgBox.append(urlDetail)
		return msgBox


	def sendAll2insta(self, msgBox, name):
		
		dics = []
		i = 0

		while True:
			if i > len(msgBox)-1:
				break
			elif type(msgBox[i]) is types.DictType:
				dics.append(msgBox[i])
				del msgBox[i]
			else:
				i+=1
		
		for i in range(0, len(dics)):
	        ipaper = instapaper.Instapaper('Your Consumer Key', 'Your Secret')
			try:
				ipaper.login('Username', 'Password')
				result = ipaper.add(dics[i]['url'])
				if result == 0:
					word = "《" + dics[i]['fileName'] + "》\n【保存失败】"
				elif result == 1:
					word = "《" + dics[i]['fileName'] + "》\n【保存成功】"
			except:
				word = u"保存失败，账号密码错误或 API 出错，请检查"

			self.sendMsg(name, word)
			print word,msgBox

def main():
	webwx = MyWXBot()

	logger = logging.getLogger(__name__)
	import coloredlogs
	coloredlogs.install(level='DEBUG')
	

	webwx.start()


if sys.stdout.encoding == 'cp936':
	sys.stdout = UnicodeStreamFilter(sys.stdout)


if __name__ == '__main__':
	main()
