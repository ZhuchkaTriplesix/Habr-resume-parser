from bs4 import BeautifulSoup
import requests
import json

param = "Python+junior"
url = f"https://career.habr.com/resumes"
data = "data.json"
import json


def write_inf(data, file_name):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(file_name, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def read_inf(file_name):
    with open(file_name, 'r', encoding="utf-8") as file:
        return json.load(file)


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
