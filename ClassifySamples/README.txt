è„šæœ¬åŠŸèƒ½:
    æ ¹æ®å¡å·´æ–¯åŸºçš„æ‰«æç»“æœå¯¹æ ·æœ¬è¿›è¡Œåˆ†ç±»æ•´ç†ï¼Œå°†æ•´ç†åçš„æ ·æœ¬ç§»åŠ¨åˆ°"Samples"ç›®å½•ä¸‹ï¼ˆä¸Šä¼ ftpååˆ é™¤ï¼‰ã€‚
    å­˜æ”¾æ ¼å¼:.\Samples\FileType\ScanResult\File

<<<<<<< HEAD
ÓÃ·¨:
   - GlobalConfig.py ÀïÅäÖÃÊı¾İ¿âĞÅÏ¢ºÍftpĞÅÏ¢
   - python Classify.py ´ıÉ¨ÃèÎÄ¼ş/ÎÄ¼ş¼Ğ
   - python report.txt
   - Èç¹û³ÌĞò±»ÒâÍâÖĞ¶Ï£¬¿ÉÒÔÊ¹ÓÃ¡°python Classify report.txt¡±´¦ÀíÍêÒÑ¾­É¨ÃèÍêµÄÑù±¾Ö®ºóÔÙ¼ÌĞøÓÃÉÏÃæµÄÃüÁî²Ù×÷¡£
=======
ç”¨æ³•:
   - GlobalConfig.py é‡Œé…ç½®æ•°æ®åº“ä¿¡æ¯å’Œftpä¿¡æ¯
   - python Classify.py å¾…æ‰«ææ–‡ä»¶/æ–‡ä»¶å¤¹
   - å¦‚æœç¨‹åºè¢«æ„å¤–ä¸­æ–­ï¼Œå¯ä»¥ä½¿ç”¨â€œpython Classify report.txtâ€å¤„ç†å®Œå·²ç»æ‰«æå®Œçš„æ ·æœ¬ä¹‹åå†ç»§ç»­ç”¨ä¸Šé¢çš„å‘½ä»¤æ“ä½œã€‚
>>>>>>> origin/master

æ³¨æ„:
   1.ç¨‹åºè¿è¡Œå‰è¯·å°†æ–‡ä»¶MD5å€¼å‘½åï¼Œå‚è€ƒhttps://github.com/Viwilla/GetMD5ã€‚
   2.æ­¤è„šæœ¬é€‚ç”¨äºè£…æœ‰å¡å·´çš„32ä½winxpï¼Œå…¶ä»–ç³»ç»Ÿç¯å¢ƒéœ€è¦åˆ°è„šæœ¬é‡Œä¿®æ”¹ä¸€ä¸‹ç›¸å…³å‚æ•°ã€‚ä¸»è¦æ˜¯avp.comçš„ç»å¯¹è·¯å¾„(å‡½æ•°AVPScan()ä¸­)

å¼€å‘ç¯å¢ƒ:
   python 2.7 + magic + MySQLdb + ftplib
   Winxp 32ä½

<<<<<<< HEAD
-------------------------------------------------------------------------------------
°²×°magic Ä£¿é:
	1¡¢°²×°pycparser-2.14  Á´½Ó: https://pypi.python.org/pypi/pycparser
	2¡¢°²×°VCForPython£¬Á´½Ó: http://aka.ms/vcpython27
	3¡¢°²×°cffiÄ£¿é£¬Á´½Ó: https://pypi.python.org/pypi/cffi/#downloads
	4¡¢°²×°libmagic  Á´½Ó: https://pypi.python.org/pypi/python-libmagic
	5¡¢°²×°file,°²×°Ö®ºóÏò»·¾³±äÁ¿pathÌí¼Ó: ..\GnuWin32\bin
	6¡¢°²×°magicÄ£¿é Á´½Ó: https://github.com/ahupp/python-magic
        ²âÊÔ import magic³É¹¦¼´¿É
-------------------------------------------------------------------------------------
magicÊ¹ÓÃ£º
	>>> import magic
	>>> magic.from_file("testdata/test.pdf")
	'PDF document, version 1.2'
	>>> magic.from_buffer(open("testdata/test.pdf").read(1024))
	'PDF document, version 1.2'
	>>> magic.from_file("testdata/test.pdf", mime=True)
	'application/pdf'
	-----------------------------------------------------------------------------
	>>> f = magic.Magic(uncompress=True)
	>>> f.from_file('testdata/test.gz')
	'ASCII text (gzip compressed data, was "test", last modified: Sat Jun 28
	21:32:52 2008, from Unix)'
	More details see https://github.com/ahupp/python-magic
	-----------------------------------------------------------------------------
	>>> f = magic.Magic(mime=True, uncompress=True)
	>>> f.from_file('testdata/test.gz')
	'text/plain'
	-----------------------------------------------------------------------------
	Èç¹û³öÏÖ'MagicException: could not find any magic files!'´íÎó£¬Ê¹ÓÃÒÔÏÂ·½·¨£º
        >>>f = magic.Magic(magic_file="C:\Program Files\GnuWin32\share\misc\magic")
    	>>>f.from_file(file)

-------------------------------------------------------------------------------------
MySQL½¨±íÓï¾ä£º
=======

å®‰è£…magic æ¨¡å—:
1ã€å®‰è£…pycparser-2.14  é“¾æ¥: https://pypi.python.org/pypi/pycparser
2ã€å®‰è£…VCForPythonï¼Œé“¾æ¥: http://aka.ms/vcpython27
3ã€å®‰è£…cffiæ¨¡å—ï¼Œé“¾æ¥: https://pypi.python.org/pypi/cffi/#downloads
4ã€å®‰è£…libmagic  é“¾æ¥: https://pypi.python.org/pypi/python-libmagic
5ã€å®‰è£…file,å®‰è£…ä¹‹åå‘ç¯å¢ƒå˜é‡pathæ·»åŠ : ..\GnuWin32\bin
6ã€å®‰è£…magicæ¨¡å— é“¾æ¥: https://github.com/ahupp/python-magic
æµ‹è¯• import magicæˆåŠŸ
More details see https://github.com/ahupp/python-magic


MySQLå»ºè¡¨è¯­å¥ï¼š
>>>>>>> origin/master
CREATE TABLE `VirusSample` (
  `SampleMD5` varchar(255) NOT NULL,
  `SampleType` varchar(1024) DEFAULT NULL,
  `Samplepath` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`SampleMD5`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
	
-------------------------------------------------------------------------------------
@Function:Using Kaspersky's scan results  to classify samples
@File storage format: .\Samples\FileType\ScanResult\File
@use : python Classfy file/folder
@Attention:
  - Before the program runs, you need to name the file in MD5.See the project https://github.com/Viwilla/GetMD5
  - Configure related information in "GlobalConfig.py" first
  - If something wrong happens that causes the program to be interrupted,use "python Classify report.txt" to process the sample that has been scanned,then use 
    "python Classify.py" to processing other samples.

Thanks for online resource "FtpFileUpload.py" and the author of the program!


@Author:Vi
@email:
  - 3320163319@qq.com
  - viwilla@outlook.com
@Time:2015/12/24
