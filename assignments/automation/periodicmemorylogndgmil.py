import os
import time
import psutil
from urllib import request
import urllib.request
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        urllib.request.urlopen('http://216.58.192.142',timeout=1):
        return True
    except Exception as err:
        return False

def MailSender(filename,time):
    try:
        fromaddr="omgawali777@gmail.com"
        toaddr="omgawali777@gmail.com"

        msg=MIMEMultipart()

        msg['From']=fromaddr

        msg['To']=toaddr

        body="""
        HELLO            
        This MAIL is Auto Generated

        """%(toaddr,time)

        Subject="""
        Process Log generated %s
        """%(time)

        msg['Subject']=Subject

        msg.attach(MIMEText(body,'plain'))

        attachment=open(filename,"rb")

        p=MIMEBase('application','octet-stream')

        p.set_payload((attachment).read())
        encoders.encode_base64(p)

        p.add_header('Content-Disposition',"attachment; filename=%s"% filename)

        msg.attach(p)

        s=smtplib.SMTP('\smtp.gmail.com',587)

        s.starttls()

        s.login(fromaddr,"Rajug@77")

        text=msg.as_string()

        s.sendmail(fromaddr,toaddr,text)

        s.quit()

        print("Log File sent ")

    except Exception as E:
        print("Unable to send",E)



def ProcessLog(log_dir="Marvellous"):
    listprocess=[]
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    seperator="-"*80
    log_path=os.path.join(log_dir,"MarvellousLog%s.log"%(time.time()))
    f = open(log_path,'w')
    f.write(seperator+"\n")
    f.write("Marvellous Infosystem Process Logger:"+time.ctime()+"\n")
    f.write(seperator+"\n")            

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms=proc.memory_info().vms/(1024*1024)
            pinfo['vms']=vms
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)

    print("Logfile is succe\s\sgfully generated at%s"%(log_path))


    connected=is_connected()

    if connected:
        startTime=time.time()
        MailSender(log_path,time.ctime())
        endTime=time.time()

        print("Took %s seconds "%(endTime-startTime))
    else:
        print("There is no internet")

def main():

    
    schedule.every(int(argv[1])).minutes.do(ProcessLog)
    while True:
        schedule.run_pending()
        time.sleep(1)
        


if __name__=="__main__":
    main()

    
