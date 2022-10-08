connect = os.popen('rasdial 宽带连接 8521296 204771').read()
print(connect)

quit_connect = os.popen('rasdial 宽带连接 /disconnect').read()
print(quit_connect)