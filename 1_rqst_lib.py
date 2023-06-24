import requests

url1 = "https://courses.wscubetech.com/s/store/courses"
r1 = requests.get(url1)       #200 means rqst successful & we can use html of the page
print(r1)



url2 = "https://www.hindustantimes.com/latest-news"
r2 = requests.get(url2)       #401 or 400 means rqst unsuccesfull & we cant use html of the page like this
print(r2)


#use this method when rqst blocked

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
r2 = requests.get(url2,headers=headers)
print(r2)



#in order to get the html of thepage
print(r1.text)


print(r2.text)