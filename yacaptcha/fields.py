# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import EMPTY_VALUES
from utils import YandexCaptcha
from widget import YandexCaptchaWidget
from django.conf import settings

class YandexCaptchField(forms.CharField):
    description = "Yandex Captcha Field"

    def __init__(self, *args, **kwargs):
        self.widget = YandexCaptchaWidget(key=settings.YANDEX_KEY)
        super(YandexCaptchField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if value in EMPTY_VALUES:
            return None
        return value

    def validate(self, values):
        yacaptcha = YandexCaptcha(self.widget.key)
        if not yacaptcha.check_captcha(captcha=values['yacaptcha'], value=values['user_input']):
            raise forms.ValidationError(_("You entered incorrect captcha code"))
