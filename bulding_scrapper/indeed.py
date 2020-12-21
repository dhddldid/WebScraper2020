import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/jobs?q=Python&l=%EC%84%9C%EC%9A%B8&radius=0&limit={LIMIT}"
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    'referer': 'https://www.google.com/'}


def get_last_page():
    print(URL)
    result = requests.get(URL, headers=header)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))
    max_page = pages[-1]
    return max_page


# 아래의 과정을 위에 함수로 만들었음.

# indeed_result = requests.get("https://kr.indeed.com/jobs?q=Python&l=%EC%84%9C%EC%9A%B8&radius=0&limit=50")
#
# # print(indeed_resul) # response is 200 mean Okay
# # print(indeed_result.text)
#
# # 페이지이동 하기 위해 beautifulsoup 이용
# # https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#
# indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
#
# # print(indeed_soup)
# pagination = indeed_soup.find("div", {"class": "pagination"})
#
# # pages is list
# links = pagination.find_all('a')
# pages = []
#
# # for link in links:
# #     # print(page.find_all("span"))
# #     # pages.append(link.find_all("span"))
# #     # pages.append(link.find("span").string)
# #     pages.append(link.string) # 바로 위에 있는것과 결과가 같음
#
# # print(pages[-1]) # -1 은 마지막에서부터 시작해서 첫 item을 나타냄
# # print(pages[:-1]) # pages 을 모두 가져오되 마지막 값은 제외 하여 가져온다
# # print(pages[0:-1]) # 위와 같음
# # print(pages[0:5]) # 0부터 시작해서 5까지를 가져옴
#
# # pages = pages[:-1]
#
# # intger로 변환
# for link in links[:-1]:
#     pages.append(int(link.string))
# # print(pages[-1]) #마지막 페이지
# max_page = pages[-1]
#
# ############# 2.5 Requesting Each Page 많은 수의 request를 만들 예정 #############
# # print(range(max_page)) # 결과값 range(0, 7)
#
# for n in range(max_page):
#     # print(n) # 0 1 2 3 4 5 6
#     print(f"start={n*50}")

def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class": "company"})
    company_anchor = company.find("a")
    if company:
        if company_anchor is not None:
            company = (str(company.find("a").string))
        else:
            company = (str(company.string))
    else:
        company = None
    company = company.strip()
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]
    job_id = html["data-jk"]
    return {'title': title, 'company': company, 'location': location,
            'link': f"https://kr.indeed.com/viewjob?jk={job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        # print(f"&start={page*LIMIT}")
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page * LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})

        for result in results:
            job = extract_job(result)  # type(job) = <class 'dict'>
            jobs.append(job)

    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(1)
    return jobs
