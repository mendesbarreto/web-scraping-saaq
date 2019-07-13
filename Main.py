import requests
from bs4 import BeautifulSoup

my_headers = {
        'Host': 'testdeconnaissances.saaq.gouv.qc.ca',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://testdeconnaissances.saaq.gouv.qc.ca/questionnaire/question/categorie/signalisation-routiere/code/2001/',
        'Connection': 'keep-alive',
        'Cookie': '234155675.1571991622.1561519613.1561836635.1562001711.4; __utmz=234155675.1561519613.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=122660873.1328791845.1561519613.1561838637.1562001711.4; __utmz=122660873.1561519613.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=unngrhpvbcg7cqg8h3t8b449g7; __utmc=234155675; __utmc=122660873; __utmb=234155675.2.10.1562001711; __utmt=1; __utmb=122660873.1.10.1562001711; __utmt_ix=1',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache',
        'Content-Length': '0',
        'Cache-Control': 'no-cache',
        'TE': 'Trailers'}

page = requests.post("https://testdeconnaissances.saaq.gouv.qc.ca/index.php?eID=testdeconnaissances_getquestionhtmlquestionnaire",
                    headers=my_headers)
print(page.content)

if( page.status_code == 200 ) :
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())
