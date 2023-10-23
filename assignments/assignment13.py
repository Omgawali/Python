import os
import hashlib
import time
import schedule
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from sys import argv

def hashfile(path, blocksize=1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)
    fd.close()
    return hasher.hexdigest()

def findDuplicate(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)
    exist = os.path.isdir(path)
    dups = {}
    if exist:
        for dirName, subdirs, filelist in os.walk(path):
            for filen in filelist:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid path")

def PrintDuplicate(dict1):
    log_dir = "marvellous"
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(log_dir, "MarvellousLog%s.log" % (time.time()))
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystem Process Logger:" + time.ctime() + "\n")
    f.write(separator + "\n")

    results = list(filter(lambda x: len(x) > 1, dict1.values()))

    if len(results) > 0:
        f.write("Duplicates found\n")
        f.write("The following files are identical\n")
        icnt = 0
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    f.write("%s\n" % subresult)
                    os.remove(subresult)
    f.close()
    return log_path

def send_email(log_path):
    from_email = 'your_email@gmail.com'
    to_email = 'recipient_email@gmail.com'
    password = 'your_email_password'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Duplicate File Log'

    body = 'Please find attached the log file containing duplicate files.'
    msg.attach(MIMEText(body, 'plain'))

    filename = os.path.basename(log_path)
    attachment = open(log_path, 'rb')
    part = MIMEApplication(attachment.read(), Name=filename)
    part['Content-Disposition'] = 'attachment; filename="%s"' % filename
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def main():
    start_time = time.time()  # Record the start time
    print("-------Automation script---------")
    print("Automation script name", argv[0])
    if(len(argv) != 2):
        print("Invalid number of arguments")
        exit()
    else:
        pass
    if(len(argv) == 2):
        if(argv[1] == "-h" or argv[1] == "-H"):
            print("This automation script is used to perform file automation")
            exit()
        if(argv[1] == "-u" or argv[1] == "-U"):
            print("Usage: Name_of_script first_argument ")
            exit()
    try:
        arr = {}
        arr = findDuplicate(argv[1])
        log_path = PrintDuplicate(arr)
        send_email(log_path)
    except ValueError:
        print("Invalid error")

    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time  # Calculate execution time
    print(f"Script execution time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    main()

# Schedule the script to run daily at a specific time (e.g., 2:00 AM)
schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
