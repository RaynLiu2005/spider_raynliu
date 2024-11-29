# jason爬虫例子
import json
import time
import requests

headers = {

    "Cookie": "uuid=FA0AEE318AB663EB0D75D20F92F251EFCE4F37E1D6D84365B1988E94B691362A; "
              "iuuid=FA0AEE318AB663EB0D75D20F92F251EFCE4F37E1D6D84365B1988E94B691362A; "
              "zgwww=46870c40-6c6f-11ef-8b7d-43b4f059c32b; "
              "_lxsdk_cuid=191c8390493c8-08e4e7ebdc9069-26001151-f6bdb-191c8390493c8; "
              "_lxsdk=FA0AEE318AB663EB0D75D20F92F251EFCE4F37E1D6D84365B1988E94B691362A; "
              "WEBDFPID=91yyv5z7636y5y7310w17uwvw85uu28w808x160902z97958103u8u54-2041001066690"
              "-1725641066060WMWKUGSfd79fef3d01d5e9aadc18ccd4d0c95074006; _gid=GA1.2.1516262161.1725641068; "
              "_gat_gtag_UA_113236691_1=1; zg.userid.untrusted=630520689; "
              "token2=AgGFISEJfcvwXbc00JcCVZjNSOLkmaPiKTC-t9UUb8dFzS6PJS"
              "-d5p_QNTZnwceHInvwWokOdSzS7wAAAADNIgAAORuGL5o01TV8ZWjnZZehCq3VQHmXmFJGaIFwlok-3Z9ypC-ASbSvDVI_DcJSMcjN"
              "; userid=2638581819; _ga=GA1.1.288445549.1725641068; "
              "_hc.v=3f08d2f6-383d-1eb0-3f3b-7ee91f27136b.1725641105; _lxsdk_s=191c8390494-19e-53c-f14%7C%7C20; "
              "_ga_14F924BYNN=GS1.1.1725641067.1.1.1725641104.23.0.0; XSRF-TOKEN=nU3acuoi-CCH1wiiKGBzNg42tszyw0n6Rof8",

    "Referer": "https://minsu.dianping.com/guangzhou/pn2/",

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 "
                  "Safari/537.36"

}

url = ("https://minsu.dianping.com/api/phx/cprod/products?cityPinyin=guangzhou&pageNow=2&isInternal=false&_token"
       "=eJx9lQuOpEgMRK8E%2FsJxIBPuf4R9NlRtj6Y1alUL58dhh8POsPCQ0Fj4HbHHL7bmv%2Fdfe8Wa%2F9j"
       "%2F2IvsMb42O7lgb8n9nOq68qessa6XcgB7qqjx%2F9bkxKKWB%2FbJSuqZG9"
       "%2B1vunBaeGrvKTuusudm0QqK5PzmwwV4a6Y3nLpnausoGDLLleef92%2FZI1MImoP%2BY3PJTl7saLY4xOfmyXp3nJIxkU%2BKjd7i0"
       "%2F2LyXvXCEkObnJIpNcFnXZdfjlqZdcvoGR7Xm6kJH6zr4T40KG4Zds3DddsSd7awy4Mxvk4zJlwOpISc9bPQKWPU74jeSsFPNtwbn0aqZlPPkHlc6FFddBBpp33HiYXZuEyZUq418OkrcQbPKJ013syYePNBEvfj1lFncSsnvVeM8NhVyx1r5FWE434ltTPGy1Q25ZjJNZcSTca9yUw6y0tYXngT%2FjfNoi7gexnURAjk%2F8IAt%2BFwh2%2FB55mnFfwFbODzuJ8ZZgRSkTeiNzjchSY9FQ%2Fia5OHkTLe6q%2Fm5bCYbaPDb0PPqhfhREJxk9erqqTnjhjla1hhZjOA9UQkRX7WJR89ZZlL8SFVqaIE9zYj1D2IZi%2BKNeVKKyWWRwOWFkCtwY9csTjtEvNnrDmqhPOTeowsmfFoc2u%2BLFoXp5QytkT4dBU9s%2BYXXkLcW7gtl82Yl%2BwUBrDvchQ9KQO%2FhETlmmblULTWoHx3nFOA70TdZ%2B4Mhk5I7yw8%2FO1XMkOVTmUvqCVx1U6MngUeAV4d4ddLKGovKiY1EQDFtPhA2lhS4Uur5qMixSTD8dMfjVzJjdMWRPVY7qWqnZMOjplXX66MFj7yyB0GHRd2G2OrL2u4L5KAaMoycIhez71bn5xRvdx%2FninXxr45V%2F4ft%2FvJ29o%2FGYMl88JCBF7Sh%2FjaeNx4SqacP9tebgi%2BfvLJQXr2bQaLybGwynP%2FDI48Wr%2B%2BeLtzQeFfyBt9Z84XzHW1X%2F4nlPOH3x6v6Dd3CD5Yrvi6dgPHxG36%2F4ovms%2FOIHXgm%2FzlW8dUY6vic%2Fqan64q1Y0fEd5MdM%2FAMv3vrxStREbLzi8Te84ufk7oM3fuCVfj56QVH9Sqydtz78%2F1W%2Fu%2Bt%2FvXi%2F8VlVGtXprz47v36r8MWN1jf7j79C3d96fvSwt6Yq%2F4pH6QreEV4U9AVyxVDd9LPeGxmt%2FUJoxzf7JcvmpzpCWbN%2BYUoXH36zJkjrZ%2BN1oh95jc7uRzNmis%2Fqv7yYznD8vkD1EsKH74%2FNVFzrBfrYzPTXlnoxeS0em2xvqxfPPhy%2B%2FrqyOnDMGNfDmWY5%2FwN2xf2g&yodaReady=h5&csecplatform=4&csecversion=3.0.0")

for number in range(1, 101):
    time.sleep(3)
    res = requests.get(url.format(number), headers=headers)
    data = json.loads(res.text)
    items = data['data']['list']
    for item in items:
        productId = item.get('productId')
        cityName = item.get('cityName')
        title = item.get('title').replace("\r", "").replace("\n", "").replace("\t", "").replace(" ", "")
        districtName = item.get('districtName')
        locationArea = item.get('locationArea')
        starRating = item.get('starRating')
        starRatingDesc = item.get('starRatingDesc')
        commentNumber = item.get('commentNumber')
        distanceDesc = item.get('distanceDesc', '未知')
        coverImage = item.get('coverImage')
        favCount = item.get('favCount')
        favCountDesc = item.get('favCountDesc')
        productUserCount = item.get('productUserCount')
        consumeDesc = item.get('consumeDesc')
        discountPrice = item.get('discountPrice')
        layoutDesc = item.get('layoutDesc')
        guestNumberDesc = item.get('guestNumberDesc')
        ugcDesc = item.get('ugcDesc')
        tags = "_".join(list(tag['tagName'] for tag in item['productTagModelList']))
        line = (str(productId) + "-" + str(cityName) + "-" + str(title) + "-" + str(districtName) + "-" + str(
            locationArea) + "-" + str(starRating) + "-" + str(starRatingDesc) + "-" + str(commentNumber) + "-" + str(
            distanceDesc) + "-" + str(coverImage) + "-" + str(favCount) + "-" + str(favCountDesc) + "-" + str(
            productUserCount) + "-" + str(consumeDesc) + "-" + str(discountPrice) + "-" + str(layoutDesc) + "-" + str(
            guestNumberDesc) + "-" + str(ugcDesc) + "-" + str(tags))

        print(line)
        
        with open('./.txt', 'a+', encoding='utf-8') as f:
            f.write(line + "\n")
