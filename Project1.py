import requests
import pandas as pd
from bs4 import BeautifulSoup
from lxml import etree
def get_from_xpath(dom,xpath):
    result = dom.xpath(xpath[0])
    if type(result) is list:
        return result[xpath[1]].strip()
    else:
        return ""
main_url = "https://research.seed.law.nyu.edu/Search/Results"
response = requests.get(main_url).content
dom = etree.HTML(str(BeautifulSoup(response, 'html.parser')))
result_urls = ["https://research.seed.law.nyu.edu" + url for url in dom.xpath("//a[contains(@href,'Search/ActionDetail')]/@href")]
print("Url Result Count :",len(result_urls))
dom_xpaths = {
    "Defendant Name" : ("//div[contains(@class,'newRow') and contains(.,'Defendant Name:')]//h2/text()",-1)
}
for url in result_urls[:5]:
	response = requests.get(url).content
	dom = etree.HTML(str(BeautifulSoup(response, 'html.parser')))
	url_data = {'URL': url}
	for field,xpath in dom_xpaths.items():
		url_data[field] = get_from_xpath(dom,xpath)
	print(url_data)