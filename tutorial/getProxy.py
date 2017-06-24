import requests
import time


class Proxy:
    def __init__(self):
        self.time = 0
        self.ip_list = []

    def get_proxy(self):
        current_time = int(time.time())
        different = current_time - self.time
        if different > 800000:
            try:
                contents = requests.get('http://api.xicidaili.com/free2016.txt')
                ip_list = contents.content.decode().split('\r\n')
                self.time = current_time
                self.ip_list = ip_list
                return ip_list
            except Exception as e:
                pass
        else:
            return self.ip_list
