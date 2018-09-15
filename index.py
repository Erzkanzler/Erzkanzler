import urllib.request
from bs4 import BeatifulSoup
import csv

Base_url = 'htpp://weblacner.net/projects/'


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def get_page_count(html):
    soup = BeatifulSoup(html)
    pagenation = soup.find('div', class_="pages_list text_box")
    return int(pagenation.find_all('a')[-2.].text)


def parse(html):
    Soup = BeatifulSoup(html)
    table = Soup.find('table', class_='items_list')

    projects.append({
        'title': cols[0].a.text,
        'categories': [category.text for category in cols[0].div.find_all('noindex')],
        'price': cols[1].text.strip(),
        'application': cols[2].text.strip().split()[0]
    })

    return projects


def save(projects, path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(("Project", "categories", "Cena", "Zayavki"))

        for projects in projects:
            writer.writerow((projects['tittle'], ', '.join(projects['categories'], projects['price'], projects['application']))


def main():
    page_count=get_page_count(get_html(Base_url))

    print('Всего найдено страниц %d' % page_count)

    projects[]

    for page in range(1, page_count):
        print('Парсинг %в%%'(page / page_count * 100))
        projects.extend(parese(get_html(Base_url + "page=%d" % page)))

    save(projects, 'projects.csv')

    for projects in projects:
        print(projects)


if __name__ == '__main__':
    main()
