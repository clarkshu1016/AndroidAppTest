import csv
import os

import time


class App():
    def __init__(self):
        self.content = ""
        self.cpu_percent = 0

    # 启动APP
    def launcher_app(self):
        cmd = 'com.tencent.tim/com.tencent.mobileqq.activity.SplashActivity'
        self.content = os.popen(cmd)

    # 打印CPU 运行情况
    def print_cpu_info(self):
        cmd = 'adb shell dumpsys cpuinfo | findstr com.tencent.tim'
        self.content = os.popen(cmd)

    # 彻底停止APP
    def stop_app(self):
        cmd = 'adb shell am force-stop com.tencent.tim'
        os.popen(cmd)

    # 获取CPU显示信息
    def get_cpu_info(self):
        self.cpu_percent = self.content.readlines()[0].split("%")[0].strip()
        return self.cpu_percent


class Controller(object):
    def __init__(self, count):
        self.app = App()
        self.counter = count
        self.alldata = [("timestamp", "elapsedtime")] # 时间戳，消耗时间

    # 单次测试过程
    def testprocess(self):
        self.app.print_cpu_info()
        time.sleep(3)
        self.app.cpu_percent = self.app.get_cpu_info()
        currenttime = self.get_current_time()
        print("current_time: "+currenttime +"   cpu: "+self.app.cpu_percent)
        self.alldata.append((currenttime, self.app.cpu_percent))

    def run(self):
        self.app.launcher_app()
        while self.counter > 0:
            self.testprocess()
            self.counter = self.counter - 1

    def get_current_time(self):
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        return current_time

    def save_data_to_csv(self):
        csvfile = open("start_time.csv", 'w', newline="")
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()


if __name__ == "__main__":
    controller = Controller(50)
    controller.run()
    controller.save_data_to_csv()