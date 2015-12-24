# ClassifySamples
  Using Kaspersky's scan results  to classify samples
	脚本功能:
	根据卡巴斯基的扫描结果对样本进行分类整理，将整理后的样本移动到"Samples"目录下（上传ftp后删除）。
	存放格式:.\Samples\FileType\ScanResult\File

	 用法:
	- GlobalConfig.py 里配置数据库信息和ftp信息
	- python Classify.py 待扫描文件/文件夹
	- 如果程序被意外中断，可以使用“python Classify report.txt”处理完已经扫描完的样本之后再继续用上面的命令操作。
 
  注意:
	1.程序运行前请将文件MD5值命名，参考MD5Sig。
	2.此脚本适用于装有卡巴的32位winxp，其他系统环境需要到脚本里修改一下相关参数。主要是avp.com的绝对路径(函数AVPScan()中)

  开发环境:
	python 2.7 + magic + MySQLdb + ftplib
	Winxp 32位

  安装magic 模块:
	1、安装pycparser-2.14  链接: https://pypi.python.org/pypi/pycparser
	2、安装VCForPython，链接: http://aka.ms/vcpython27
	3、安装cffi模块，链接: https://pypi.python.org/pypi/cffi/#downloads
	4、安装libmagic  链接: https://pypi.python.org/pypi/python-libmagic
	5、安装file,安装之后向环境变量path添加: ..\GnuWin32\bin
	6、安装magic模块 链接: https://github.com/ahupp/python-magic
	测试 import magic成功即可
	More details see https://github.com/ahupp/python-magic


MySQL建表语句：
	CREATE TABLE `VirusSample` (
	  `SampleMD5` varchar(255) NOT NULL,
	  `SampleType` varchar(1024) DEFAULT NULL,
	  `Samplepath` varchar(255) DEFAULT NULL,
	  PRIMARY KEY (`SampleMD5`)
	) ENGINE=MyISAM DEFAULT CHARSET=latin1;
	

@Function:Using Kaspersky's scan results  to classify samples
@File storage format: .\Samples\FileType\ScanResult\File
@use : python Classfy file/folder
@Attention:
  - Before the program runs, you need to name the file in MD5.See the project "MD5Sig"
  - Configure related information in "GlobalConfig.py" first
  - If something wrong happens that causes the program to be interrupted,use "python Classify report.txt" to process the sample that has been scanned,then use 
    "python Classify.py" to processing other samples.

Thanks for online resource "FtpFileUpload.py" and the author of the program!


@Author:Vi
@email:
  - 3320163319@qq.com
  - viwilla@outlook.com
@Time:2015/12/24
