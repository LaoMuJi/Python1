import requests
import json
import time
import re

def a():
    loginurl = 'https://sx.byebyetext.com/api/app/users/third/login'
    headers1 = {
        "User-Agent": "okhttp/3.11.0",
        'accept-encoding': 'gzip',
        'content-length': '370',
        'Host': 'sx.byebyetext.com',
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = 'openId=oR6sd1dTvATHpczuv2mpBicdnIOU&unionId=oGEegwG5z30-BQJQBXcSM-coEcNA&nickName=wxid_qfpud60bmqj421&avatarUrl=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTLn2wBLGGSDR4Efhpb48XeTFUKCqicUddGGbUKBRdBZBOt7r8dcrXgSaNfdgxTuB1Le2J28XjZZZFQ%2F132&userGender=2&authType=1&countryCode=CN&appVersion=3.5.0&deviceInfo=unknown%2Funknown%2F8.1.0&platformId=1&deviceId='
    while True:
        try:
            rsp2 = requests.post(loginurl, headers=headers1, data=data)
        except Exception:
            print('一级重试')
        else:
            json1 = json.loads(rsp2.content)
            data_token = json1['data']
            token = data_token['token']
            b(token)
            break


def b(token):
    url = "https://sx.byebyetext.com/api/app/users/6301/voices?"
    kw = {
        "lastId": "null",
        'moduleId': '2'
    }
    headers2 = {
        "User-Agent": "okhttp/3.11.0",
        'accept-encoding': 'gzip',
        'authorization': 'Bearer ' + token,
        'Host': 'sx.byebyetext.com',
        'content-type': 'application/x-www-form-urlencoded'
    }
    while True:
        try:
            rsp = requests.get(url, params=kw, headers=headers2)
        except:
            print('二级重试')
        else:
            a = rsp.content.decode("UTF-8-sig")
            # print(a)
            b = json.loads(a)
            c = b['data']
            # 循环json
            for d in c:
                e = time.localtime(int(d['created_at']))
                t = time.strftime("%Y-%m-%d %H:%M:%S", e)

                m, topic_name, album_name, htmlstr = '', '', '', ''

                if 'img_list' in d:
                    s = ''.join(d['img_list'])
                    m = re.search(r'http.*jpeg', s).group()
                    m = '= '+m

                voice_url = d['voice_url']
                voice_len = d['voice_len']

                if 'topic_name' in d:
                    topic_name = d['topic_name']
                if 'resource' in d:
                    g = d['resource']
                    print(g)
                    # album_name = g['album_name'] + '(音乐)'

                out = voice_url + ' ' + t + ' ' + voice_len + '秒' + ' ' + '——' + topic_name + album_name + '——' + ' ' + m
                print(out)
                out = out + '\n'
                # 读取文件
                with open(r'C:\Users\lcc92\Desktop\音频.txt', 'r+', encoding='UTF-8-sig') as f:
                    old = f.read()
                    if out in old:
                        pass
                    else:
                        f.seek(3)
                        f.write(out)
                        f.write(old)
            aa()
            break


def aa():
    htmlstr = ''
    html = '''    <br>
    %s
    <br>
    <img src="%s" alt="" />
    <br>
    <audio src="%s" controls="controls"></audio>
    <br>
    %s
    <br>
    <br>
    <br>
    '''
    htmlend = '''</body>
</html>'''

    with open(r'C:\Users\lcc92\Desktop\音频.txt', 'r', encoding='UTF-8-sig') as f:
        l = list(f)
    for i in l:
        m1 = re.match(r'^.*aac', i).group()
        m2 = re.search(r' .*秒 ', i).group()
        m3 = re.search(r'——.*——', i).group()
        p = re.compile(r'——')
        m3 = p.sub(r'', m3)
        try:
            m4 = re.search(r'http://im.*jpeg', i).group()
        except:
            m4 = ''
        htmll = html % (m3, m4, m1, m2)
        htmlstr += htmll
        # print(htmlstr)
    htmlstr += htmlend


    with open(r'C:\Users\lcc92\Desktop\1.html', 'r+', encoding='utf-8') as f:
        f.seek(286, 0)
        f.write(htmlstr)


if __name__ == '__main__':
    while True:
        a()
        t = time.localtime()
        ft = time.strftime("%Y{y}%m{m}%d{d} %H:%M", t).format(y='-', m='-', d='')
        print(ft)
        time.sleep(180)

