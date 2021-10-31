import requests
import re

def beianchaxun(url):
    urls = url
    URL = ("https://beian.tianyancha.com/search/{}".format(urls))
    headers = {
            'Connection': 'close',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            }
    try:
        req = requests.get(url=URL,headers=headers)
        html = req.content
        #print(req.content.decode())
        titlere = r'<span class="ranking-ym" rel="nofollow">(.+?)</span>'
        title = re.findall(titlere,html.decode('utf-8'))
        if len(title) == 0:
            print(urls,"该公司天眼查找不到备案域名",'\n')
        else:
            print('\n',urls,"备案域名: ")
            for i in title:
                print(i)
    except:
        print('有异常，无法爬取')

def duqu():
    num = 0
    f = None
    filename=input('请输入所有公司名字所在的路径：')
    try:
        with open(filename, 'r',encoding='utf-8') as f:
            line = f.readlines()
            print("共获取了%d个目标"%(len(line)),'\n')
        for i in line:
            num = num+1
            a = i.strip() 
            beianchaxun(a)
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()
    
if __name__ == '__main__':
    banner='''
    

               __                 
              / _|                
   __ _ _   _| |_ ___ _ __   __ _ 
  / _` | | | |  _/ _ \ '_ \ / _` |
 | (_| | |_| | ||  __/ | | | (_| |    by aufeng 
  \__,_|\__,_|_| \___|_| |_|\__, |    基于天眼查的批量公司名备案查询域名脚本
                             __/ |    Tips ：cmd运行后，输入请输入域名所在的文本路径,txt即可
                            |___/ 


    '''
    print(banner)
    duqu()
    print('\n',"运行完毕")
    #a = '方欣科技有限公司'
    #beianchaxun(a)
    
