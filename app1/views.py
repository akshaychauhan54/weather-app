from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def get_html_content(city):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    city=city.replace(" ","+")
    html_content=session.get(f'https://www.google.com/search?q=weather+{city}').text
    return html_content

def weather(request):
    result=None
    if 'city' in request.GET:
        
        city=request.GET.get('city')
        html_content=get_html_content(city)
        soup=BeautifulSoup(html_content,'html.parser')
        result=dict()
        result['region']=soup.find("div",attrs={'id':'wob_loc'}).text
        result['daytime']=soup.find("div",attrs={'id':'wob_dts'}).text
        result['condition']=soup.find("span",attrs={'id':'wob_dc'}).text
        result['temp']=soup.find('span',attrs={'id':'wob_tm'}).text

        pass

    return render(request,'weather.html',{'result':result})


