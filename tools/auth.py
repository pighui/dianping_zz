# !/usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ = pighui
# __time__ = 2021-1-15 下午8:24
import random
import requests

username = "17765810231"
password = "PDoW6qfTw982nxtKeHWozGLXzBONaAOjfVxWX1FZJhinF484fcTDD9y5utCg9VYGE2Gh4grGxipxH0/fXG56o2q6biFdMXzwLjsMQtfcSOfjYYoQMkJmtPO7Iz3xiUPFwE3affszVclmGzFJiugkktkkQO6nxGJ5cmf+nUrBl8A="
cookies = [
    "fspop=test; cy=130; cye=zhangzhou; s_ViewType=10; _hc.v=743f819f-b4b8-0764-c43b-557321a8ae3a.1610709101; ctu=8165d77d09a3dbfa6c134a71ecb893de284837e15c8f2eaefa07a0636bd621e8; _dp.ac.v=62353c21-c02d-4bfe-8aaa-afc2f14a9737; lgtoken=01e7b4fcd-2276-4dee-9992-78b49b1d61e0; dplet=f141531e21926b29dd971b7444472809; dper=85dfe084b53e3ccd4bc4d195b49f17efe01de0969814954aa9305e9800a7833baee721cc4c18c376160801dde886fa48b07829b04c8c2e69110aeadfae8fdf275dbc5412461b398da3436e1979be76a4ebb71a9a3e7f49745850cb425c223261; ll=7fd06e815b796be3df069dec7836c3df; ua=test; uamo=17765810231"]
tokens = [
    "eJyVk2tvolAQhv8LSfsFoufC1cRssIDVVrSIoHabBrlYRC5ykdbN/vc9uFvazaabNjkfnpl3mHfO5PCDykce1aMgAICVKIY6+nkTdkCHJ1FZUD3IQyBAnsUs5AWGct/nOMwLHENtckuhevdIAgwWuIcmYZD4HkoIMBCI4IF5ZQ49MIglp6kakSLqqSyzotftOq6bVknZ8UInycJk23HT+DXZDYPcif3bdBsm31xnv984btRXneLlnHo8q4+vArisQ8/vB86+8C+zPC1TN933f/tc5r4X5ufgAssXSCOnruu/XMnF/zvU/jzGWyNS908Lcr3YbK6HeMAggEnPd8RJnyTxkyR8mfhPEvcBoQ+J/TLhM5GVReeVBcxIny1MIvkteS25LW1aclq6bmnZ0vcKAAj+hMTFObtASNaMJWawMM2pTsowasZov2r05sW3sQQZCN90BASGQ4zcSCJPJPxWSvaHMcvMZ7LeGJaNYWM8If8W0YtwmxDyx7VWexDdnWRZng6WyI81JFmBOx2GySJLlKFfJhJcjweHzBjFymyGaIFV1LqywUjSQlwvHC7eOQYXQVF4uTkE9ulubG4Nm8+550yMYJe1t6nGgoMH6G68nzkRmmQ3CqZ3A9p+4qxUxatbGdFQCxLDX7jTW9mQbF0c6rvyCGmVPTiy/nScyIHiVdEiPronEFVXQTaeW93lKJJW+mRbeCZvVZ4maAd2WbxokbW1eGV/pakW4J9DY+ff5ewgnGwUf65jPjiBE+aGhc7uVOu6mosjsF6tTaFeFzeioOQDr2uHK7pSg+eDN0d1v0/9/AWO9z9w"]


def auth():
    login_url = "https://account.dianping.com/account/ajax/passwordLogin"
    data = {"countrycode": "86",
            "username": "17765810231",
            "keepLogin": "off",
            "encryptPassword": password, "_token": random.choice(tokens)}
    res = requests.post(url=login_url, data=data)
    if res.status_code == 200:
        cookie = res.json()["cookie"]
        return cookie
    else:
        cookies_txt = random.choice(cookies)
        return cookies_txt
