# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET

"""
Script uses elements from  https://github.com/coagulant/cleanweb.
"""


class YandexApiError(Exception):
    pass


class YandexCaptcha(object):
    def __init__(self, key=None):
        if not key:
            raise YandexApiError('Scrip needs API key to use. Get it here: http://api.yandex.ru/cleanweb/form.xml')
        self.session = requests.Session()
        self.session.params['key'] = key

    def request(self, *args, **kwargs):
        """
            http://api.yandex.ru/cleanweb/doc/dg/concepts/error-codes.xml
        """
        r = self.session.request(*args, **kwargs)
        if r.status_code != requests.codes.ok:
            error = ET.fromstring(r.content)
            message = error.findtext('message')
            code = error.attrib['key']
            raise YandexApiError('%s (%s)' % (message, code))
        return r

    def get_captcha(self, id=None):
        payload = {'id': id}
        r = self.request('get', 'http://cleanweb-api.yandex.ru/1.0/get-captcha', params=payload)
        return dict((item.tag, item.text) for item in ET.fromstring(r.content))

    def check_captcha(self, captcha, value, id=None):
        payload = {'captcha': captcha,
                   'value': value,
                   'id': id}
        r = self.request('get', 'http://cleanweb-api.yandex.ru/1.0/check-captcha', params=payload)
        root = ET.fromstring(r.content)
        if root.findall('ok'):
            return True
        return False
