"""
@Function:Using Kaspersky's scan results  to classify samples
@File storage format: .\Samples\FileType\ScanResult\File
@use : python Classfy file/folder
@Attention:
  - Before the program runs, you need to name the file in MD5.See the project "MD5Sig"
  - Configure related information in "GlobalConfig.py" first
  - If something wrong happens that causes the program to be interrupted,use "python Classify report.txt" to process the sample that has been scanned,then use 
    "python Classify.py" to processing other samples.

Thanks for the online resource "FtpFileUpload.py" and the author of the program!

@Author:Vi
@email:
  - 3320163319@qq.com
  - viwilla@outlook.com
@Time:2015/12/24
"""

import sys
import re
import os
import os.path 
import shutil
import magic
import MySQLdb
import GlobalConfig as GC
import traceback
reload(sys)
sys.setdefaultencoding('utf-8')

count = 0
global TYPE
global DIR
global MD5

def ConnectDB(h, u ,pa,d,p):
    try:
        global cur
        global conn        
        ISOTIMEFORMAT = '%Y-%m-%d %X'
        conn = MySQLdb.connect(
            host = h, 
            user = u,
            passwd = pa,
            db = d,
            port = p)
        cur = conn.cursor()
        print("DB use success")
    except Exception,e:  
        traceback.print_exc()

def FileType(file):
    global MD5
    MD5 = file.split("\\")[-1][-32:]
    f = magic.Magic(magic_file="C:\Program Files\GnuWin32\share\misc\magic")
    type = f.from_file(file)
    global TYPE
    TYPE = type.replace("\\","\\\\")
    type = type.replace("\\","_").replace("/","_").replace(":","_").replace("*","_").replace("\"","_").replace("<","_").replace(">","_").replace("|","_")
    type = type.split(",")[0]
    if len(type) > 100:
        type = type[0:100]   
    return type

def mkdirs(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False
    
def RemoveLocalFile(rootdir):
    filelist=os.listdir(rootdir)  
    for f in filelist:  
        filepath = os.path.join( rootdir, f )  
        if os.path.isfile(filepath):  
            os.remove(filepath)  
            #print filepath+" removed!"  
        elif os.path.isdir(filepath):  
            shutil.rmtree(filepath,True)  
        #print "dir "+filepath+" removed!"
        
def Sort():
    global cur
    global conn
    global MD5
    global TYPE
    global DIR
    f = open ("report.txt","r")
    lines = f.readlines()
    count0 = 0
<<<<<<< HEAD
    #17
=======
>>>>>>> origin/master
    for line in lines[17:]:
        dirname = GC.dirname
        line = line.strip("\n")
        line = line.replace("\t","  ")
        line = line.split("  ")
        a = re.compile(r'\//.*')
        line[1] = a.sub('',line[1])
        line[1] = line[1].strip()
        newname = line[1].replace("\\","_")
        if len(line) > 5:
            if line[5] == " completed":
                break
        elif len(line) < 3:
            continue
        elif line[2] == "skipped":
            continue

        try:
            ftype = FileType(line[1])
        except Exception,e:
            continue
            ftype = "UNKNOW"
            traceback.print_exc()
        dirname = dirname + ftype + "\\"
        
        if line[2] == "detected":
            try:
<<<<<<< HEAD
                n = line[3].rindex('.')
                newpos = dirname + line[3][0:n]
            except:
                newpos = dirname + line[3]
=======
              n = line[3].rindex('.')
              newpos = dirname + line[3][0:n]
            except:
              newpos = dirname + line[3]
>>>>>>> origin/master
            try:
                mkdirs(newpos)
            except:
                next
            try:
                shutil.move(line[1],newpos)
                print line[1] + "-->" + newpos
                DIR = newpos.replace(".\\","/").replace("\\","/")
<<<<<<< HEAD
                DIR = "/Samples" + DIR.split("Samples")[1]
=======
>>>>>>> origin/master
                str = "INSERT INTO VirusSample(SampleMD5,SampleType,Samplepath)values('%s','%s','%s')"%(MD5,TYPE,DIR)
                try:
                    cur.execute(str)
                    conn.commit()
                    
                except:
                    pass
            except:
                continue

        else:
            newpos = dirname + line[2]
            try:
                mkdirs(newpos)
            except:
                next
            try:
                shutil.move(line[1],newpos)
                print line[1] + "-->" + newpos
                DIR = newpos.replace(".\\","/").replace("\\","/")
<<<<<<< HEAD
                DIR = "/Samples" + DIR.split("Samples")[1]
=======
>>>>>>> origin/master
                str = "INSERT INTO VirusSample(SampleMD5,SampleType,Samplepath)values('%s','%s','%s')"%(MD5,TYPE,DIR)
                try:
                    cur.execute(str)
                    conn.commit()
                except:
                    pass
            except:
                continue
        
        global count
        count = count +1
        count0 = count0 +1
        if count0 > 500:
            try:
                os.system("python FtpFileUpload.py")
<<<<<<< HEAD
=======
                RemoveLocalFile(".\\Samples")
>>>>>>> origin/master
                count0 = 0
            except:
                print "ftp upload error"
                continue
    f.close()
    cur.close()
    conn.close()
    newname = "report" + newname
    os.rename("report.txt",newname)
    if not sys.argv[1] == "report.txt":
        shutil.move(sys.argv[1],".\\Samples\\UNDETECTED")
    os.system("python FtpFileUpload.py")
    
def AVPScan():
    str = "\"C:\\Program Files\\Kaspersky Lab\\Kaspersky Anti-Virus 16.0.0\\avp.com\" SCAN "
    str = str + sys.argv[1]
    str = str + " i1 /R:.\\report.txt"
    os.system(str)
    
def main():
    ConnectDB(GC.host,GC.user,GC.passwd,GC.db,GC.portsql)
    if sys.argv[1] == "report.txt":
        Sort()
    else:
        AVPScan()
        Sort()
        
if __name__ =="__main__":
    print"Waiting......."
    main()
    print"%d items have been detected! others have been sent to dir \"UNDETECTED\" "%count
    print "For more details,Please see the database(address:%s  Table:VirusSample)"%GC.host

exit()
