import requests

from bs4 import BeautifulSoup

def scrape_website(Your_url):
    # 指定されたURLからHTMLを取得する
    response = requests.get(Your_url, timeout=5.0)


    # エラーチェック
    if response.status_code != 200:
        print("エラー：ウェブページを取得できませんでした")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('title').text

    return title

Your_url = 'https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q11237021016'
result = scrape_website(Your_url)

print(result)
