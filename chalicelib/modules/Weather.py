from chalicelib.modules.BasicRequest import BasicRequest

'''
https://www.metaweather.com/api/
'''
class Weather(BasicRequest):
    base_url = 'https://www.metaweather.com/api'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_city_info(self, city_name):
        url = '{}/location/search/?query={}'.format(self.base_url,city_name)
        return self.make_request(url)

    def get_city_weather(self, woeid):
        url = 'https://www.metaweather.com/api/location/{}/'.format(woeid)
        return self.make_request(url)