�ű�����:
    ���ݿ���˹����ɨ�������������з��������������������ƶ���"Samples"Ŀ¼�£��ϴ�ftp��ɾ������
    ��Ÿ�ʽ:.\Samples\FileType\ScanResult\File

�÷�:
   - GlobalConfig.py ���������ݿ���Ϣ��ftp��Ϣ
   - python Classify.py ��ɨ���ļ�/�ļ���
   - ������������жϣ�����ʹ�á�python Classify report.txt���������Ѿ�ɨ���������֮���ټ�������������������

ע��:
   1.��������ǰ�뽫�ļ�MD5ֵ�������ο�MD5Sig��
   2.�˽ű�������װ�п��͵�32λwinxp������ϵͳ������Ҫ���ű����޸�һ����ز�������Ҫ��avp.com�ľ���·��(����AVPScan()��)

��������:
   python 2.7 + magic + MySQLdb + ftplib
   Winxp 32λ


��װmagic ģ��:
1����װpycparser-2.14  ����: https://pypi.python.org/pypi/pycparser
2����װVCForPython������: http://aka.ms/vcpython27
3����װcffiģ�飬����: https://pypi.python.org/pypi/cffi/#downloads
4����װlibmagic  ����: https://pypi.python.org/pypi/python-libmagic
5����װfile,��װ֮���򻷾�����path���: ..\GnuWin32\bin
6����װmagicģ�� ����: https://github.com/ahupp/python-magic
���� import magic�ɹ�
More details see https://github.com/ahupp/python-magic


MySQL������䣺
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