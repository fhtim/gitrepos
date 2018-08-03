

from selenium import webdriver
import time


from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery

browser = webdriver.Chrome(".\\chromedriver\\chromedriver_win32\\chromedriver.exe")
# browser.get('https://www.baidu.com/')
# search_box = browser.find_element_by_id('kw')
# submit_button = browser.find_element_by_id('su')
# search_box.send_keys('python')
# submit_button.click()
# next_button = browser.find_element_by_css_selector('#page a.n')
# time.sleep(4)
# next_button.click()
# //////
# browser.get('https://www.36kr.com/')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)') #滚动到底

KEYWORD = 'iPhone'
wait = WebDriverWait(browser,10) #等待超时

def crawl_page(page):
	# try:
	url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
	browser.get(url)
	if page>1:
		page_box = wait.until(
			EC.presence_of_element_located(
				(By.CSS_SELECTOR,'#mainsrp-pager .form .input')
				)
			)

		submit_button = wait.until(
			EC.element_to_be_clickable(
				(By.CSS_SELECTOR,'#mainsrp-pager .form .J_Submit')
				)
			)
		page_box.clear() #清空输入
		page_box.send_keys(page) #输入
		submit_button.click() #点击

	wait.until(
		EC.presence_of_element_located(
			(By.CSS_SELECTOR,'.m-itemlist .items .item')
			)
		)

	get_products()
	# except:
	# 	crawl_page(page)

def get_products():
	global file
	html = browser.page_source
	doc = PyQuery(html)

	items = doc('#mainsrp-itemlist .m-itemlist .items .item').items()
	for item in items:
		product = {
			'image':item.find('.pic .img').attr('data-src'),
			'price':item.find('.price').text(),
			'deal':item.find('.deal-cnt').text(),
			'title':item.find('.title').text(),
			'shop':item.find('.shop').text(),
			'location':item.find('.location').text(),

		}
		print(product)
		# s = product['image']+','+product['price']+','+product['deal']+','+product['title']+','+product['shop']+','+product['location']+'\n';
		# file.write(s.encode('gbk'))

with open('results.csv','wb') as file:

	for page in range(1,5):
		crawl_page(page)

	file.close()


