from chalicelib.modules.BasicRequest import BasicRequest

'''
https://rickandmortyapi.com
'''
class RickAndMorty(BasicRequest):
    base_url = 'https://rickandmortyapi.com/api'

    def get_a_character(self, character_id):
        if character_id < 1 or character_id > 493:
            character_id = 1
        url = '{}/character/{}'.format(self.base_url, character_id)
        return self.make_request(url)