一.登陆
    1.https://wx.qq.com/
        没什么返回
    2.https://res.wx.qq.com/a/wx_fed/webwx/res/static/js/index_ca360ff.js
        返回app_id
    3.https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_=1516980369142
        返回 YdzC6r4psQ==  参数
    4.https://login.weixin.qq.com/qrcode/YdzC6r4psQ==
        发送请求获取二维码图片
    5.https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=YdzC6r4psQ==&tip=0&r=-856939101&_=1516980369144
        请求服务器 二维码登陆是佛通过  返回408  201 200（为正确状态码） 状态为200时 返回转跳连接
    6.https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=Aw9YbrGBNY8APJXlRk5NHqAq@qrticket_0&uuid=YdzC6r4psQ==&lang=zh_CN&scan=1516980521
        返回信息  会转跳下一个页面  禁止转跳
二.初始化信息
    1.https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-857016728
        获取微信人物列表
    2.https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxstatusnotify
        获取msgid 7153298037437709806
    3.https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxbatchgetcontact?type=ex&r=1516980473160
        获取信息
    4.https://webpush.wx2.qq.com/cgi-bin/mmwebwx-bin/synccheck?r=1516980473119&skey=%40crypt_44167482_1c8f17cf3935ad412139dd612ed73398&sid=0aSPqHRIAjN3vCKC&uin=1894228408&deviceid=e457107474762512&synckey=1_668600012%7C2_668600879%7C3_668600886%7C1000_1516961762&_=1516980472135

    5.https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxbatchgetcontact?type=ex&r=1516980474353 重复了

    6.https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?r=1516980473115&seq=0&skey=@crypt_44167482_1c8f17cf3935ad412139dd612ed73398
        获取人物信息

    7.https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxstatreport?fun=new  不知效果 发送了json数据


三.发信息
    1.https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg 发送信息
    2.https://wx2.qq.com/cgi-bin/mmwebwx-bin/webwxsync?sid=0aSPqHRIAjN3vCKC&skey=@crypt_44167482_1c8f17cf3935ad412139dd612ed73398
三.维持心跳