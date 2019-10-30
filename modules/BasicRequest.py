import requests

class BasicRequest(object):
    '''
    basic generic url requester
    '''
    def make_request(self, url):
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        print('no response')
        return {}