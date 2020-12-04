import requests
from bs4 import BeautifulSoup
import pprint


class HNItem:
    def __init__(self, item):
        self.item = item
        self.item_points = 0
        self.parse_hn_link()
        self.parse_hn_link_title()
        self.parse_hn_points()

    def parse_hn_link(self):
        self.item_href = self.item.select('a.storylink[href]')[0]['href']

    def parse_hn_link_title(self):
        self.item_href_title = self.item.select(
            'a.storylink[href]')[0].getText()

    def parse_hn_points(self):
        points_element = self.item.next_sibling.select('span.score[id]')
        if len(points_element):
            self.item_points = int(
                points_element[0].getText().replace(' points', ''))


class HNews():
    def __init__(self, page=1):
        self.__page = page
        self.hn = []
        self.__pull_hn_items()

    def __pull_hn_items(self):
        items = self.__fetch_hn_items()
        for item in items:
            hn_item = HNItem(item)
            if hn_item.item_points > 99:
                self.hn.append({'title': hn_item.item_href_title,
                                'link': hn_item.item_href, 'votes': hn_item.item_points})

        self.__sort_stories_by_votes()

    def __fetch_hn_items(self):
        res = requests.get(
            'https://news.ycombinator.com/news?p=' + str(self.__page))
        soup = BeautifulSoup(res.text, 'html.parser')
        items = soup.tr.next_sibling.next_sibling.next_sibling.select(
            '.athing[id]')

        return items

    def __sort_stories_by_votes(self):
        self.hn = sorted(self.hn, key=lambda k: k['votes'], reverse=True)

    def pull_page(self, page=1):
        self.__page = page
        self.hn = []
        self.__pull_hn_items()


hn_obj = HNews()
pprint.pprint(hn_obj.hn)
hn_obj.pull_page(2)
pprint.pprint(hn_obj.hn)
