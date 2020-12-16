# https://github.com/psf/requests
import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://kr.indeed.com/jobs?q=Python&l=%EC%84%9C%EC%9A%B8&radius=0&limit=50")


# print(indeed_resul) # response is 200 mean Okay
# print(indeed_result.text)

# 페이지이동 하기 위해 beautifulsoup 이용
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

# print(indeed_soup)
pagination = indeed_soup.find("div", {"class":"pagination"})

# pages is list
pages = pagination.find_all('a')
spans = []

for page in pages:
    # print(page.find_all("span"))
    spans.append(page.find_all("span"))

# print(spans[-1]) # -1 은 마지막에서부터 시작해서 첫 item을 나타냄
# print(spans[:-1]) # spans 을 모두 가져오되 마지막 값은 제외 하여 가져온다
# print(spans[0:-1]) # 위와 같음
# print(spans[0:5]) # 0부터 시작해서 5까지를 가져옴

spans = spans[:-1]