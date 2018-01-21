# AndroidAppTest

* **Appium自动化测试框架**,Appium 是基于UIAutomator的测试框架,官方网站:http://appium.io/
1. 安装[appium-desktop](https://github.com/appium/appium-desktop/releases/tag/v1.2.7),目前最新版本为1.2.7 
2. 安装[appium-python-client](https://pypi.python.org/pypi/Appium-Python-Client),目前版本为0.2.6，解压后cmd跳转解压目录输入：python setup.py install进行安装
3. 安装[android studio&sdk](https://developer.android.com/studio/index.html),可以安装android studio，也可以sdk tools，并且设置系统环境变量
4. 安装[java sdk](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html),设置好java环境变量
5. 安装appium-uiautomator的驱动: npm install appium-uiautomator2-driver，而安装npm需要安装nodejs

* **MonkeyRunner** ,Android sdk tools 自动的工具,同样支持黑盒测试

* **Input 工具**,Input工具是android系统内自带的一个jar文件，位于/system/framwork/input.jar
  在cmd当中输入adb shell input 可以模拟点击，滑动，按键各种事件,Input工具本身是用java编写的,位于Android
  [framework层](https://android.googlesource.com/platform/frameworks/base.git/+/master/cmds/input/src/com/android/commands/input/Input.java)
  input工具的缺点就是默认不能模拟出按压的Prs值和Size值，因为默认都是1.0，需要重新编译打包input.jar文件，修改其默认参数
  修改injectMotionEvent方法中的形参pressure和局部变量DEFAULT_SIZE，这两个参数分别对应Prs和Size值
```
Usage: input [<source>] <command> [<arg>...]

The sources are:
      keyboard
      mouse
      joystick
      touchnavigation
      touchpad
      trackball
      dpad
      stylus
      gamepad
      touchscreen

The commands and default sources are:
      text <string> (Default: touchscreen)
      keyevent [--longpress] <key code number or name> ... (Default: keyboard)
      tap <x> <y> (Default: touchscreen)
      swipe <x1> <y1> <x2> <y2> [duration(ms)] (Default: touchscreen)
      press (Default: trackball)
      roll <dx> <dy> (Default: trackball)
```     

* 用法如下:
 1. adb shell input text "nihao" 目前只支持ASCII
 2. adb shell input swipe 300 200 500 900 200  # 头2两个参数表示第一个点，即起点的坐标,三，四参数表示第二个点的坐标，即终点，最后一个参数表示按压时间为200ms
 3. adb shell input tap 300 400 表示点击 坐标为(300,400)的点
 4. adb shell input keyevent 3 表示回退到主屏幕 3这个值对应的按键就是HOME键，[KeyEvent映射表](https://developer.android.com/reference/android/view/KeyEvent.html)

    
