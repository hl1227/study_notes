from selenium import webdriver
import time
#因为每次都会弹出网页，所以可以设置无头浏览器：
chrome_option = webdriver.ChromeOptions()
#chrome_option.headless=True

# 识别---------------------------------------------
chrome_option.add_argument('--disable-blink-features=AutomationControlled')
# UA头---------------------------------------------
ua_list=['Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30']
chrome_option.add_argument('user-agent={}'.format(ua_list))
# 是否加载图片--------------------------------------
chrome_option.add_experimental_option('prefs', {'profile.managed_default_content_settings.images': 2})
chrome_option.add_argument('blink-settings=imagesEnabled=false')
# 无头浏览器----------------------------------------
chrome_option.add_argument('--headless')
chrome_option.add_argument('--no-sandbox')
chrome_option.add_argument('--disable-dev-shm-usage')
chrome_option.add_argument('--disable-gpu')
#关闭证书验证错误
chrome_option.add_argument('--ignore-certificate-errors')
#关闭受到控制
chrome_option.add_experimental_option('useAutomationExtension', False)
chrome_option.add_experimental_option("excludeSwitches", ['enable-automation'])

chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 开发者模式
chrome_option.add_argument("--disable-blink-features=AutomationControlled")  # 禁用启用Blink运行时的功能 88 以后设置为false


#1  创建浏览器对象
driver = webdriver.Chrome(options=chrome_option)
# 清除浏览器cookies
driver.delete_all_cookies()

# 运行Javascript
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

#2 添加网址
driver.get('https://weibo.com/?category=0')
#3 保存截图  获取数据
driver.save_screenshot('28-weibo.png')
#4打印HTML
data = driver.page_source
print(data)
# 5将浏览器最大化显示
driver.maximize_window()
#6设置浏览器宽、高
driver.set_window_size(480, 800)  # 设置浏览器宽480、高800显示
driver.back()  # 浏览器后退
driver.forward()  # 浏览器前进
#4.5:因为点击信息后弹出新的页面，如果要在新的页面操作，需要切换浏览器：
page = driver.window_handles
#print(page)
driver.switch_to.window(page[1])
# 8刷新页面
driver.refresh()
#9获取当前页cookie
driver.get_cookies()
#10拖动滑块
dragger = driver.find_element_by_id('nc_1_n1z')  # .滑块定位
action = ActionChains(driver)
for index in range(500):
    try:
        action.drag_and_drop_by_offset(dragger, 500, 0).perform()  # 平行移动鼠标，此处直接设一个超出范围的值，这样拉到头后会报错从而结束这个动作
    except UnexpectedAlertPresentException:
        break

#11 点击验证码
action.move_to_element_with_offset('element',x,y).click().perform()
#如果遇到iframe 嵌套框架标签（一个网页包含了一整个网页，比如QQ邮箱登陆）
#需要切换到内嵌的框架里面去：再操作
#drive.switch_to.frame('属性值')
#跳出来：
#drive.switch_to.window(drive.window_handles[0])

#----等待页面加载
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="qqq"]')),message="无法定位'下一页'").send_keys('selenium')
except Exception as e:
    print('err',e)