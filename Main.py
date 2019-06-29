import requests
from bs4 import BeautifulSoup

my_headers = {'Host': 'testdeconnaissances.saaq.gouv.qc.ca',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:68.0) Gecko/20100101 Firefox/68.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': '__utma=234155675.1571991622.1561519613.1561836632.1561836635.3; __utmz=234155675.1561519613.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=122660873.1328791845.1561519613.1561519613.1561836632.2; __utmz=122660873.1561519613.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=unngrhpvbcg7cqg8h3t8b449g7; __utmc=234155675; __utmc=122660873; __utmb=234155675.5.6.1561838574583; __utmt=1',
            'Upgrade-Insecure-Requests': '1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'Trailers'}
page = requests.get("https://testdeconnaissances.saaq.gouv.qc.ca/index.php?eID=testdeconnaissances_getquestionhtmlquestionnaire",
                    headers=my_headers)
print(page.content)

if( page.status_code == 200 ) :
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())
