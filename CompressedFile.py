import os
import zlib
import zipfile

''' 思路： 创建文件对象 - 读取文件 - 关闭文件 - 压缩 - 获得压缩结果 - 生成新文件 - 写入新文件'''

#创建file对象并打开
fileObject = open("shakespeare.txt", "r")
print ("文件名: ", fileObject.name)

ret = fileObject.read()
fileObject.close()
ret = ret.encode()
print("压缩前大小:", len(ret))
# print("压缩前文本内容:", ret)

res = zlib.compress(ret)
print("压缩后大小:", len(res))
res_content = zlib.decompress(res)
res_content = res_content.decode()
# print("压缩后:", res_content)

logName = "log.txt"
logging = open(logName, "a+")
logging.write(res_content)
logging.close()
