import os
import time
import psutil
import smtplib
import schedule
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def is_connected():
    try:
        with urllib.request.urlopen('http://216.58.192.142', timeout=1):
            return True
    except Exception as err:
        return False

def send_email(filename, timestamp):
    try:
        fromaddr = "omgawali777@gmail.com"  # Replace with your email
        toaddr = "omgawali777@gmail.com"  # Replace with recipient's email
        password = "Rajug@77"  # Replace with your email password

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = f"""
        HELLO
        This MAIL is Auto Generated
        {toaddr} {timestamp}
        """
        msg.attach(MIMEText(body, 'plain'))

        attachment = open(filename, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename={filename}")
        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print("Log File sent")
    except Exception as e:
        print("Unable to send email:", e)

def process_log(log_dir="Marvellous"):
    listprocess = []
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except Exception as e:
            print("Error creating directory:", e)
            return

    separator = "-" * 80
    log_path = os.path.join(log_dir, f"MarvellousLog_{time.time()}.log")

    try:
        with open(log_path, 'w') as f:
            f.write(separator + "\n")
            f.write("Marvellous Infosystem Process Logger: " + time.ctime() + "\n")
            f.write(separator + "\n")

            for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
                try:
                    vms = proc.info['memory_info'].vms / (1024 * 1024)
                    proc_info = f"PID: {proc.info['pid']}, Name: {proc.info['name']}, Username: {proc.info['username']}, VMS: {vms:.2f} MB"
                    listprocess.append(proc_info)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

            f.write("\n".join(listprocess))

        print(f"Log file successfully generated at {log_path}")

        connected = is_connected()

        if connected:
            start_time = time.time()
            send_email(log_path, time.ctime())
            end_time = time.time()

            print(f"Took {end_time - start_time:.2f} seconds to send the email")
        else:
            print("There is no internet connection")
    except Exception as e:
        print("Error creating log file:", e)

def main():



    schedule.every(1).minutes.do(process_log)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
