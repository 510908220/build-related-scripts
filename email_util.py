# -*- coding: UTF-8 -*-
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

class EmailManage(object):
	"""
	邮件发送
	"""
	def __init__(self):
		"""
		设置发送邮件账户及服务器基本信息
		"""
		self.mail_host="smtp.163.com"  #设置服务器
		self.mail_user="dailybuild"    #用户名
		self.mail_pass="hzz@2009119135"   #口令
		self.mail_postfix="163.com"  #发件箱的后缀

	def send(self,sub,content,to_list = None,char_set ="utf-8"):
		me="YYE Extension Check"+"<"+self.mail_user+"@"+self.mail_postfix+">"
		msgRoot = MIMEMultipart('related')
		msgRoot['Subject'] = sub
		msgRoot['From'] = me
		if to_list == None:
			to_list = ["huzhongzhong@yy.com"]
		msgRoot['To'] = ";".join(to_list)
		msgAlternative = MIMEMultipart('alternative')
		msgRoot.attach(msgAlternative)
		msg = MIMEText(content,_subtype='html',_charset=char_set)
		msgAlternative.attach(msg)
		try:
			server = smtplib.SMTP()
			server.connect(self.mail_host)
			server.login(self.mail_user,self.mail_pass)
			server.sendmail(me, to_list, msgRoot.as_string())
			server.quit()
			return True
		except Exception, e:
			print str(e)
			return False

if __name__ == '__main__':
	mailto_list=["huzhongzhong@yy.com"]
	em = EmailManage()
	flag = em.send( "test", "haha", mailto_list)
	if flag:
		print "send sucess"