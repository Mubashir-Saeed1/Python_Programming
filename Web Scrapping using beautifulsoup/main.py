from bs4 import BeautifulSoup
import requests

url = requests.get('https://www.mhvillage.com/parks/tx?group-by=counties')
# print(url.text)


soup = BeautifulSoup(url.content, "html.parser")

results = soup.find(id="results-list")
# print(results.prettify())

job_elements = results.find_all("div", class_="container-fluid paginated-result-container ng-star-inserted")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()