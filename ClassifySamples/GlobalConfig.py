#coding=utf-8
#author: Vi

from __future__ import with_statement
import ConfigParser

config = ConfigParser.ConfigParser()


"""
@ftp
"""
hostaddr = '' # ftp地址
username = '' # 用户名
password = '' # 密码
port  =  21   # 端口号 
rootdir_local  = 'C:\ClassifySamples\Samples' # 本地目录
rootdir_remote = "/Samples"

"""
@MySQL
"""
host = ""
user = ""
passwd = ""
db = ""
portsql =  
