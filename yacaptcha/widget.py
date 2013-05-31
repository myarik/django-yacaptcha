# -*- coding: utf-8 -*-
from django.forms import widgets
from utils import YandexCaptcha
from django.template.loader import render_to_string


class YandexCaptchaWidget(widgets.Widget):
    """YandexCaptchaWidget"""
    def __init__(self, key=None):
        self.key = key
        super(YandexCaptchaWidget, self).__init__()

    def render(self, name, value, attrs=None):
        TEMPLATE_WIDGET = 'yandex_captcha.html'

        yacaptcha = YandexCaptcha(self.key)
        context_dic = yacaptcha.get_captcha()

        return render_to_string(TEMPLATE_WIDGET, {'yacaptcha_response': context_dic['captcha'],
                                'yandex_captcha_img': context_dic['url']})

    def value_from_datadict(self, data, files, name):
        return {'user_input': data.get('yandex_captcha_userinput', None), 'yacaptcha': data.get('yandex_response', None)}
