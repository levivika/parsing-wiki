import requests
import json
from bs4 import BeautifulSoup

URL='https://en.wikipedia.org/wiki/Moscow#External_links'

def get_html(url):
    headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0'}
    response = requests.get(url, headers=headers)
    return response.text


def get_links(html):
    soup=BeautifulSoup(html, 'html.parser')
    a_el = soup.find_all('a')
    links={}
    for i,a in enumerate(a_el):
        href = a.get('href')
        if href:
            links[i+1]=href
    return links

def write_links_to_json(links, filename='links'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(links, file, indent=2, ensure_ascii=False)


html ="""
    <ul>
    <li><span class="official-website"><span class="url"><a class="external text" href="https://www.mos.ru/en/" rel="nofollow">Official website</a></span></span></li>
    <li><a class="external text" href="https://strelkamag.com/ru/article/moscow-housing-map" rel="nofollow">Interactive map of housing in Moscow from 1785–2018</a>. <a class="external text" href="https://web.archive.org/web/20200623093543/https://strelkamag.com/ru/article/moscow-housing-map" rel="nofollow">Archived</a></li>
    <li><a class="external text" href="https://web.archive.org/web/20170722083414/http://en.travel2moscow.com/" rel="nofollow">Travel2moscow.com – Official Moscow Guide</a></li>
    <li><a class="external text" href="https://web.archive.org/web/20120505061015/http://mos.ru/en/index.php" rel="nofollow">Official Moscow Administration Site</a></li>
    <li><a class="external text" href="http://xn--80adxhks.xn--h1akdx.xn--80aswg/" rel="nofollow">Informational website of Moscow</a> <a class="external text" href="https://web.archive.org/web/20200527141051/http://www.xn--80adxhks.xn--h1akdx.xn--80aswg/" rel="nofollow">Archived</a></li>
    <li><a class="external text" href="http://historic-cities.huji.ac.il/russia/moscow/moscow.html" rel="nofollow">Old maps of Moscow</a>. <a class="external text" href="https://web.archive.org/web/20210116220851/http://historic-cities.huji.ac.il/russia/moscow/moscow.html" rel="nofollow">Archived</a>.</li>
    </ul>
    """

links = get_links(html)
write_links_to_json(links)
