import requests
import unittest


url_get = 'https://rivcor.pythonanywhere.com/api/urls/'
url_post = 'https://rivcor.pythonanywhere.com/api/'


def post_request(url, data):
    # POST request with add data
    response = requests.post(url, data=data)
    return response.json()


def post_clear_request(url, data):
    # Delete all data & POST request with new data
    requests.delete(url)
    response = requests.post(url, data=data)
    return response.json()


def get_request(url):
    # Get all data
    response = requests.get(url)
    return response.json()



class APIrequestTest(unittest.TestCase):
    def test_1(self):
        # Check create new instance with full data
        data = {
            'host_url': 'https://www.figma.com/file/example40',
            'short_url': 'https://www.figma.com/12345',
            'length': 15,
            'list_of_symbols': 'qwerty1234567890',
        }
        url = url_post
        result = {'post': {'host_url': 'https://www.figma.com/file/example40',
                           'short_url': 'https://www.figma.com/12345'}}
        self.assertEqual(post_clear_request(url, data), result)

    def test_2(self):
        # Check if 'host_url' exists in db
        data = {
            'host_url': 'https://www.figma.com/file/example40',
            'short_url': 'https://www.figma.com/12345',
            'length': 15,
            'list_of_symbols': 'qwerty1234567890',
        }
        url = url_post
        result = [{'host_url': 'https://www.figma.com/file/example40',
                   'short_url': 'https://www.figma.com/12345'}]
        self.assertEqual(post_request(url, data), result)

    def test_3(self):
        # Check if 'short_url' exists in db
        data = {
            'host_url': 'https://www.figma.com/file/example41',
            'short_url': 'https://www.figma.com/12345',
            'length': 15,
            'list_of_symbols': 'qwerty1234567890',
        }
        url = url_post
        result = {'error': 'The short_url exists. Edit, please, and try again.'}
        self.assertEqual(post_request(url, data), result)

    def test_4(self):
        # Check create new instance without 'short_url'
        data = {
            'host_url': 'https://www.figma.com/file/example42',
            'length': 15,
            'list_of_symbols': 'qwerty1234567890',
        }
        url = url_post
        result = {'post': {'host_url': 'https://www.figma.com/file/example42', 'short_url': 'https://www.figma.com/3y5t8t6q1qwr6ee'}}
        self.assertEqual(post_clear_request(url, data)['post']['host_url'], result['post']['host_url'])
        self.assertEqual(post_clear_request(url, data)['post']['short_url'][:20], result['post']['short_url'][:20])
        self.assertEqual(len(post_clear_request(url, data)['post']['short_url']), 37)

    def test_5(self):
        # Check create new instance without 'short_url' and 'length'
        data = {
            'host_url': 'https://www.figma.com/file/example43',
            'list_of_symbols': 'qwerty1234567890',
        }
        url = url_post
        result = {'post': {'host_url': 'https://www.figma.com/file/example43',
                           'short_url': 'https://www.figma.com/241r8098'}}
        self.assertEqual(post_clear_request(url, data)['post']['host_url'], result['post']['host_url'])
        self.assertEqual(post_clear_request(url, data)['post']['short_url'][:20], result['post']['short_url'][:20])
        self.assertEqual(len(post_clear_request(url, data)['post']['short_url']), 30)

    def test_6(self):
        # Check create new instance without 'short_url', 'length' and 'list_of_symbols'
        data = {
            'host_url': 'https://www.figma.com/file/example44',
        }
        url = url_post
        result = {'post': {'host_url': 'https://www.figma.com/file/example44',
                           'short_url': 'https://www.figma.com/Cq4tEJDt'}}
        self.assertEqual(post_clear_request(url, data)['post']['host_url'], result['post']['host_url'])
        self.assertEqual(post_clear_request(url, data)['post']['short_url'][:20], result['post']['short_url'][:20])
        self.assertEqual(len(post_clear_request(url, data)['post']['short_url']), 30)

    def test_7(self):
        # Check trying to create new instance with another error'
        data = {
            'host_url': 'https://www.figma.com/file/example44',
            'length': 'abcde890'
        }
        url = url_post
        result = {'error': 'User data is not correct. Edit, please, and try again.'}
        self.assertEqual(post_clear_request(url, data), result)

    def test_8(self):
        # Check get request for all data'
        url = url_post
        data = {
                'host_url': 'https://www.figma.com/file/example51',
                'short_url': 'https://www.figma.com/abcd51'
            }
        post_clear_request(url, data)
        data = {
                'host_url': 'https://www.figma.com/file/example52',
                'short_url': 'https://www.figma.com/abcd52'
            }
        post_request(url, data)
        data = {
                'host_url': 'https://www.figma.com/file/example53',
                'short_url': 'https://www.figma.com/abcd53'
            }
        post_request(url, data)
        result = [
            {'host_url': 'https://www.figma.com/file/example51',
             'short_url': 'https://www.figma.com/abcd51'},
            {'host_url': 'https://www.figma.com/file/example52',
             'short_url': 'https://www.figma.com/abcd52'},
            {'host_url': 'https://www.figma.com/file/example53',
             'short_url': 'https://www.figma.com/abcd53'}
        ]
        url = url_get
        self.assertEqual(get_request(url), result)


