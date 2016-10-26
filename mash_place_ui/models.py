from mash_place_ui import cache, app
import requests


class Constituency(object):
    """Encapsulating class for Mash Place API access."""
    def __init__(self):
        super(Constituency, self).__init__()
        self.base_url = app.config['PLACE_API_URL'] + "/constituencies"

    @cache.memoize(timeout=86400)
    def get_constituencies(self):
        url = '{0}/'
        response = requests.get(url.format(self.base_url))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
            app.logger.error('GET ' + response.url + ' ' + str(response.status_code))
        else:
            result = response.text
            app.logger.info('GET ' + response.url + ' ' + str(response.status_code))
        return result

    @cache.memoize(timeout=86400)
    def get_constituency(self, code):
        url = '{0}/{1}'
        response = requests.get(url.format(self.base_url, code))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
            app.logger.error('GET ' + response.url + ' ' + str(response.status_code))
        else:
            result = response.text
            app.logger.info('GET ' + response.url + ' ' + str(response.status_code))
        return result


class County(object):
    """Encapsulating class for Mash Place API access."""
    def __init__(self):
        super(County, self).__init__()
        self.base_url = app.config['PLACE_API_URL'] + "/counties"

    @cache.memoize(timeout=86400)
    def get_counties(self):
        url = '{0}/'
        response = requests.get(url.format(self.base_url))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
            app.logger.error('GET ' + response.url + ' ' + str(response.status_code))
        else:
            result = response.text
            app.logger.info('GET ' + response.url + ' ' + str(response.status_code))
        return result

    @cache.memoize(timeout=86400)
    def get_county(self, code):
        url = '{0}/{1}'
        response = requests.get(url.format(self.base_url, code))
        if response.status_code != requests.codes.ok:
            response.raise_for_status()
            app.logger.error('GET ' + response.url + ' ' + str(response.status_code))
        else:
            result = response.text
            app.logger.info('GET ' + response.url + ' ' + str(response.status_code))
        return result
