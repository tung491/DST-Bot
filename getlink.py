import requests
from bs4 import BeautifulSoup
import openweathermap_token


def tinhte():
    url_src = []
    r = requests.get('https://tinhte.vn/')

    soup = BeautifulSoup(r.text, 'html.parser')

    a = soup.find_all("div", class_="thread-title width-narrow")
    title_n_link = []

    for i in a[:5:]:
        for n in i.find_all('a', href=True):
            link = 'https://tinhte.vn/' + str(n['href'])
            title = n.get_text()
            title_n_link.append((title, link))

    b = soup.find_all("div", class_="thread-image width-wide")
    for i in b[:5:]:
        url_src.append(i['data-src'])

    return title_n_link, url_src


def fml():
    r = requests.get('http://www.familug.org/')

    soup = BeautifulSoup(r.text, 'html.parser')

    x = soup.find_all('h3', class_="post-title entry-title")

    link = x[0].find_all(href=True)[0]['href']
    title = x[0].get_text()

    return (title, link)


def genk():
    title_n_link = []
    url_src = []

    r = requests.get('http://genk.vn/')

    soup = BeautifulSoup(r.text, 'html.parser')

    a = soup.find_all('a', href=True, title=True,
                      class_="klwfnr-thumb")
    b = soup.find_all('a', href=True, title=True,
                      class_="gfnp-thumb knswa_border")
    c = soup.find_all('a', href=True, title=True,
                      class_="klwfnswn-thumb knswa_border")

    for i in a + b + c:
        link = 'http://genk.vn' + i['href']
        title = i['title']
        title_n_link.append((title, link))
        url_src.append(i.find_all('img', src=True)[0]['src'])

    return title_n_link, url_src


def kenh14():
    title_n_link = []
    url_src = []

    r = requests.get('http://kenh14.vn/')

    soup = BeautifulSoup(r.text, 'html.parser')
    x = soup.find_all('a', class_="klwfnl-thumb", title=True, href=True)
    y = soup.find_all('a', class_="klwfnr-thumb", title=True, href=True)
    z = soup.find_all('a', class_="klwfnswn-thumb", title=True, href=True)

    for i in x + y + z:
        title = i['title']
        link = 'http://kenh14.vn' + i['href']
        title_n_link.append((title, link))
        url_src.append(i.find_all('img', src=True)[0]['src'])


def xkcd():
    r = requests.get('https://xkcd.com/')

    soup = BeautifulSoup(r.text, 'html.parser')

    x = soup.find_all('img', alt=True, src=True, title=True)[0]

    title = x['alt']
    scr_url = 'https:' + x['src']
    content = x['title']

    return (title, scr_url, content)


def PE():
    sovled = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
              19, 20, 21, 22, 24, 25, 28, 29, 30, 31, 34, 35, 36, 48, 52, 56,
              67]
    problem = list(range(1, 612))

    for i in sovled:
        problem.remove(i)

    un_solved = problem
    num = un_solved[0]

    r = requests.get('https://projecteuler.net/problem={}'.format(num))
    soup = BeautifulSoup(r.text, 'html.parser')

    x = soup.find_all("div", class_="problem_content")

    content = ''

    for i in x:
        content += i.get_text()

    return (num, content)


def pornhub():
    r = requests.get('https://pornohub.su/')

    title_n_link = []
    url_src = []

    soup = BeautifulSoup(r.text, 'html.parser')

    x = soup.find_all("div", class_="td-module-thumb")

    for a in x[:5:]:
        for b in a.find_all('a', href=True, title=True):
            link = b['href']
            title = b['title']
            title_n_link.append((title, link))
            url_src.append('https:' + b.find_all('img', src=True)[0]['src'])

    return title_n_link, url_src


def vnexpress():
    title_n_link = []
    url_src = []
    r = requests.get('https://vnexpress.net/')
    soup = BeautifulSoup(r.text, 'html.parser')

    x = soup.find_all('a', class_="thumb thumb_5x3")
    for i in x[:5:]:
        link = i['href']
        title = i['title']
        src = i.find_all('img')[0]['src']
        title_n_link.append((title, link))
        url_src.append(src)

    return title_n_link, url_src


def viettlot():
    r = requests.get('http://vietlott.vn/vi/')
    soup = BeautifulSoup(r.text, 'html.parser')

    x = soup.find_all('ul', class_="result-number")
    lst_num = x[0].get_text().split()

    result_num = ''

    for i in lst_num:
        result_num += i + ' '

    y = soup.find_all('td', class_="red")
    jackpot_value = y[0].get_text()

    z = soup.find_all('div', class_="lotto-result")
    t = soup.find_all('div', class_="lotto-result")

    content = z[0].find('h4').get_text() + '\n' + \
        t[0].find_all('p', class_="time-result")[0].get_text()

    return (content, result_num, jackpot_value)


def openweathermap():
    token = openweathermap_token.token
    id_city = 1581129

    api_url = 'http://api.openweathermap.org' \
        '/data/2.5/weather?id={0}&APPID={1}'.format(id_city, token)

    r = requests.get(api_url)

    info = r.json()

    description = info['weather'][0]['description']
    humidity = info['main']['humidity']
    pressure = info['main']['pressure']
    temp = info['main']['temp'] - 273
    temp_max = info['main']['temp_max'] - 273
    temp_min = info['main']['temp_min'] - 273
    wind_speed, wind_deg = info['wind']['speed'], info['wind']['deg']

    data = {'description': description,
            'pressure': pressure,
            'humidity': humidity,
            'temp': temp,
            'temp_max': temp_max,
            'temp_min': temp_min,
            'wind_speed': wind_speed,
            'wind_deg': wind_deg
            }

    return data


def boba_place(msg):
    link_page = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
                 'location={},{}&radius'
                 '=5000&keyword=teae&key={}')
    
    link_page_token = ('https://maps.googleapis.com/maps/api'
                       '/place/nearbysearch/json?pagetoken={0}&key={1}')
    
    API_key = 'AIzaSyBHFBk7ycGOQ5vEKXCqgAq1BQfFoyS3Ep0'

    g = geocoder.google(msg)
    current_place = g.lat
    current_place = g.lng

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    distance = 6367 * c
