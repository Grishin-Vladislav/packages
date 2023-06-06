from bs4 import BeautifulSoup
import requests


class RandomHuman:
    url = 'https://www.behindthename.com/random/random.php?' \
          'gender=both&number=1&sets=1&surname=&randomsurname=yes' \
          '&showextra=yes&all=yes'

    def __init__(self):
        self._soup = self._get_soup()
        self.data = self._get_data()

    def _get_data(self):
        name, surname = self._find_full_name()
        return {
            'name': name,
            'surname': surname,
            'gender': 'male' if self._search('Gender:') == 'Masculine'
            else 'female',
            'age': self._search('Age:'),
            'b_date': self._search('Birth date:'),
            'height': self._search('Height:').split('/')[0].rstrip(),
            'weight': self._search('Weight:').split('/')[0].rstrip(),
            'blood_type': self._search('Blood type:')
        }

    def _search(self, search):
        tag = self._soup.find(string=search)
        return tag.next_element.text

    def _find_full_name(self) -> list:
        return [tag.string for tag in self._soup.find_all('a', 'plain')]

    @classmethod
    def _get_soup(cls):
        try:
            response = requests.get(cls.url)
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            print('Request error in application/stuff/parser.py\n'
                  f'{e}')