import os
import psutil
import time
import schedule

def ProcessDisplay(log_dir="Marvellous"):
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

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            vms = proc.memory_info().vms / (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)
    print("Done")

def main():
    print("Process Monitor")
    print("Automation script name", __file__)

    schedule.every(1).minutes.do(ProcessDisplay)  # Run 'ProcessDisplay' function every minute

    while True:
        schedule.run_pending()  # Check and run pending tasks
        time.sleep(1)

if __name__ == "__main__":
    main()
