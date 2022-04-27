
#https://blog.csdn.net/weixin_52040868/article/details/119883498
#https://blog.csdn.net/u010698107/article/details/118468802?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_antiscanv2&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1.pc_relevant_antiscanv2&utm_relevant_index=1

#UI元素定位
# pip install -i https://pypi.douban.com/simple weditor
# python -m weditor

#安装  pip install --upgrade --pre uiautomator2
import uiautomator2 as u2
import time
#连接
devices=u2.connect('127.0.0.1:62001')
#设备信息
print(devices.info)
print(devices.device_info)
'-----------------------------------------------------------------'
#安装app
#devices.app_install('apk网址')
#删除app
#devices.app_uninstall('apk包名')
#屏幕关闭的情况下点亮一次/锁屏
# devices.screen_on()
# devices.screen_off()
'-----------------------------------------------------------------'
#全局每次操作间隔
devices.click_post_delay=3
#从包名运行app  超时时间默认为20S
devices.wait_timeout=18
devices.app_start('com.aiyu.kaipanla',wait=True)
time.sleep(5)
#从包名关闭app
#devices.app_stop('com.aiyu.kaipanla')
#清除app所有数据
#devices.app_clear('com.aiyu.kaipanla')
#关闭所有应用
#devices.app_stop_all()
'-----------------------------------------------------------------'
#当前运行的app包名
print(devices.app_current())
#正在运行的app包名
print(devices.app_list_running())
'-----------------------------------------------------------------'
#点击app
devices(text='开盘啦').click()
devices.xpath('//*[@text="开盘啦"]').click(timeout=30)
#输入文本
devices.xpath('//*').send_keys('888')
#判断元素是否存在
devices.exists(text='忘记密码')
devices(text='忘记密码').exists(timeout=3)

'-----------------------------------------------------------------'
#获取屏幕大小
#print(devices.window_size())
#截图
#devices.screenshot('xxx.png.jpg')
#推送文件
#devices.push(r'D://xxx/xxx','/systeam/xxx')
#拉取文件
#devices.pull('/systeam/xxx',r'D://xxx/xxx')
'-----------------------------------------------------------------'
#手机按键
# devices.press('home')#主页
# devices.press('back')#后退
# devices.press('recent')#最近的程序
# devices.press('power')#电源
'-----------------------------------------------------------------'
#滑动
#指定位置fx, fy, tx, ty
#devices.swipe('起始x','起始y','结束x','结束y',)

#指定方向 "left", "right", "up", "down" 移动百分比
#devices.swipe_ext('left',scale=0.9)

#指定元素滑动
#e=devices(text='xxx')
#e.swipe('down',steps=100)