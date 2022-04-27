import requests,random

url='https://85tube.com/get_file/1/abc3660e8f7c41e6484d78be0a876dd5e4071de039/2000/2581/2581.mp4/?br=428&rnd=1561577726087'
headers = [{
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"},
           {"User-Agent": "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident / 5.0"},
           {"User-Agent": "Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)"},
           {"User-Agent": "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)"},
           {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"},
           {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
           {
               "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
           {
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"},
           {
               "User-Agent": "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0"},
           {
               "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
           {"User-Agent": "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1"}
           ]
header = random.choice(headers)
res=requests.get(url,headers=header).content
open('韩国2.mp4','wb').write(res)