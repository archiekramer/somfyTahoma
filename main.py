import os, requests, sys, logging
from config import login, mdp

url = "https://www.somfy-connect.com"
url = "https://www.tahomalink.com"
url2 = "https://www.tahomalink.com/enduser-mobile-web/steer-html5-client/tahoma/"
header_mozilla = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/100.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate, br",
"DNT": "1",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",   
"Sec-Fetch-Site": "none",
"Sec-Fetch-User": "?1"}

r = requests.get(url, headers=header_mozilla)
cookie = r.cookies
contenu = r.content

r = requests.get(url2, headers=header_mozilla)
logging.DEBUG("pause")


#login 
data = {
    
    username : login,
    password : mdp,
    grand_type : "password"
}
requests.post("https://accounts.somfy.com/oauth/oauth/v2/token")