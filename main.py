from bs4 import BeautifulSoup
import requests
import json

param = "Python+junior"
url = f"https://career.habr.com/resumes"
data = "data.json"


def parse(url):
    request = requests.get(url)
    soup = BeautifulSoup(request.text, "html.parser")
    result = soup.find_all("article", class_="resume-card")
    for i in result:
        employee_text = i.text
        employee_href = i.find("a")["href"]
        print(employee_text)
        print(employee_href)


if __name__ == '__main__':
    parse(url)
