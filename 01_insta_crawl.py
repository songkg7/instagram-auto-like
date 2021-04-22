# selenium으로 instagram열기

from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup


# instagram data
insta_id = "songkg8"
insta_pw = "black7kg"
keyword = "반려동물"


driver = webdriver.Chrome(
    executable_path=""
)

url = "https://www.instagram.com/accounts/login/?source=auth_switcher"
driver.get(url)


time.sleep(3)
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(insta_id)
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(insta_pw)
driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()

# time.sleep(3)
# popup
# driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()

# search
time.sleep(4)
url = f"https://www.instagram.com/explore/tags/{keyword}/"
driver.get(url)


def parse(pageString):
    bsobj = BeautifulSoup(pageString, "html.parser")
    photo_all = bsobj.find("div", {"class": "EZdmt"})
    resent_list = photo_all.findAll("div", {"class": "v1NH3"})

    links = []
    for resent in resent_list:
        insta_link = "https://www.instagram.com"
        # <a href="123" alt="456">hi my name is ~~</a>
        link_addr = resent.find("a")['href']
        links.append(insta_link + link_addr)

    return links


time.sleep(4)
pageString = driver.page_source
links = parse(pageString)

# 좋아요 누르고 댓글 달기
for url in links:
    try:
        print(url)
        driver.get(url)

        rndSec = random.randint(5, 15)
        time.sleep(rndSec)
        messages = ["잘 보고 갑니다.", "좋은 사진이네요", "좋아요 누르고 갑니다~", "very good!"]
        message = random.choice(messages)

        # 좋아요
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[1]/span[1]/button').click()

        # 댓글
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[3]/div/form/textarea').click()
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[3]/div/form/textarea').send_keys(message)
        driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[3]/div/form/button').click()
    except Exception as e:
        pass


# driver.close()
# link뽑기
