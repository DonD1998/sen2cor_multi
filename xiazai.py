from xml.dom.minidom import parse
from data_downloader import downloader

# 创建.netrc, 可以保存网站的账号密码信息
netrc = downloader.Netrc()
netrc.add('scihub.copernicus.eu', 'dond', 'Qtqk3AsHu%nM_8y')

'''
Created on 2022 10 20 
@author:wanlin qiu
'''

# 输出文件目录
folder_out = r'G:\QiuWanLin\遥感数据\sentinel\2020'

# meta4 文件目录
url_file = r'G:\QiuWanLin\遥感数据\sentinel\2020\products.meta4'

data = parse(url_file).documentElement
urls = [i.childNodes[0].nodeValue for i in data.getElementsByTagName('url')]

downloader.download_datas(urls, folder_out)

print('完成下载！')