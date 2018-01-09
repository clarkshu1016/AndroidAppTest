import csv
import os

import time


class App():
    def __init__(self):
        self.content = ""
        self.start_time = 0

    # 启动APP
    def launcher_app(self):
        cmd = 'adb shell am start -W -n com.google.android.youtube/com.google.android.apps.youtube.app' \
              '.WatchWhileActivity '
        self.content = os.popen(cmd)

    # 彻底停止APP
    def stop_app(self):
        cmd = 'adb shell am force-stop com.google.android.youtube'
        os.popen(cmd)

    # 输入home键
    def stop_app_but_running_background(self):
        cmd = "adb shell input keyevent 3"
        os.popen(cmd)

    # 获取启动时间
    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                print("line:" + line)
                self.start_time = line.split(":")[1].strip()
                break
        return self.start_time


class Controller(object):
    def __init__(self, count):
        self.app = App()
        self.counter = count
        self.alldata = [("timestamp", "elapsedtime")] # 时间戳，消耗时间

    # 单次测试过程
    def testprocess(self):
        self.app.launcher_app()
        time.sleep(3)
        elapsedtime = self.app.GetLaunchedTime()
        self.app.stop_app_but_running_background()
        time.sleep(3)
        currenttime = self.get_current_time()
        self.alldata.append((currenttime, elapsedtime))

    def run(self):
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
    controller = Controller(3)
    controller.run()
    controller.save_data_to_csv()
