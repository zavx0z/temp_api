from time import sleep

import requests

from utils.driver import Driver
from selenium import webdriver


def init():
    capabilities = {
        "browserName": "chrome",
        "version": "81.0",
        "enableVNC": True,
        "enableVideo": False
    }

    return webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities)


def yt_query(q):
    wd = init()
    response = requests.get("http://localhost:4444/status")
    pk = response.json().get('browsers').get("chrome").get('81.0').get("unknown").get("sessions")[0].get('id')

    requests.post('http://localhost:5000/api/', json={"id": pk, "msg": 'подключение к браузеру'})

    wdex = Driver(wd)
    wd.get("https://youtube.com")
    wd.fullscreen_window()

    input_text = wd.find_element_by_name('search_query')
    input_text.click()
    input_text.clear()
    input_text.send_keys(q)
    button = wd.find_element_by_id('search-icon-legacy')
    button.click()

    xpath_video = "//ytd-video-renderer[@class='style-scope ytd-item-section-renderer']"
    videos = wdex.wait_finds_by_xpath(xpath_video)

    for video in videos:
        wdex.scroll_to_center(video)
        title = video.text
        requests.post('http://localhost:5000/api/', json={"id": pk, "msg": title})
