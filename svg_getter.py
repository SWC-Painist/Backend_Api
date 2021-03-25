from selenium import webdriver


option = webdriver.ChromeOptions()
option.add_argument('--headless')
chrome_driver = webdriver.Chrome(executable_path=r"D:\Productors\chromedriver_win32\chromedriver.exe",options=option)

def getSVGStr(file_path:str):
    global chrome_driver
    chrome_driver.get(r"file://"+file_path)
    svg_text = chrome_driver.find_element_by_tag_name("SVG").get_attribute("outerHTML")
    return svg_text

if __name__ == '__main__':
    s = getSVGStr(r'D:\VS_Progs\__CODE__PY\Painist\backend\data\trans_1.txt.html')