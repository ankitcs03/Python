from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

file = open("wath_price.csv", "w+")
header = "product, old_price, discount, new_price \n"
file.write(header)

url = 'https://paytmmall.com/watches-llpid-29482?src=1&q=watch'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

page_soup =  soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class","pCOS"})

for container  in containers:

	product = container.div.text
	new_price = container.findAll("span", {"class":"_1kMS"})[0].span.text
	try:
		old_price = container.findAll("span", {"class":"dQm2"})[0].text
	except:
		old_price = 0 

	if old_price == 0:
		discount = 0
	else:
		discount  = container.findAll("span", {"class":"c-ax"})[0].text

	file.write( str(product).replace(",","|") + "," + str(old_price) + "," + str(discount) + "," + str(new_price) + "\n")

file.close()
