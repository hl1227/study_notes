from ftplib import FTP
from io import BytesIO
class ftp():
    def __init__(self):
        self.connect1()
    def connect1(self):
        self.ftp1 = FTP()
        self.ftp1.connect('154.86.175.226', 21)
        self.ftp1.login(user='s1888', passwd='iSFZetGfHBEEHJzF')
        self.ftp1.set_pasv(False)
        self.ftp1.encoding = 'utf-8'
    def send1_data(self,ftp_path,data):
        try:
            self.ftp1.storbinary(cmd="STOR %s" % ftp_path, fp=data)
            print('S1上传成功')
        except Exception as e:
            self.ftp1.close()
            err_data = 's1 error:{} {}'.format(ftp_path, e)
            print(err_data)
            f_error.write(err_data + '\n')
            self.connect1()
    def run(self):
        f_name = 'yindi_1_result'
        f = open(r'D:\result\liwei\biying2_keyword\{}.txt'.format(f_name), 'r', encoding='utf-8').readlines()
        for count in range(0, len(f), 6000):
            ftp_path = '{}_{}:{}.txt'.format(f_name, count, count + 6000)
            print('开始上传:', ftp_path)
            data = BytesIO(''.join(f[count:count + 6000]).encode())
            self.send1_data(ftp_path=ftp_path, data=data)
        self.ftp1.close()
if __name__ == '__main__':
    f_error = open(r'ftp_error.txt', 'w+', encoding='utf-8')
    ftp().run()