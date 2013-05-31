django-yacaptcha
================

Python wrapper for API Yandex Captcha. 

Yandex Captcha installs easy and simple usage.

Install
-----
* Install via pip::
        
        pip install -e https://github.com/myarik/django-yacaptcha.git#egg=yacaptcha

* You need `Obtain API key`_

.. _Obtain API key: http://api.yandex.ru/cleanweb/form.xml

Usage
-----
* Add to INSTALLED_APPS::

        yacaptcha

* Add Yandex API Key to settings.py::
        
        YANDEX_KEY = 'your_api_key'

* Add to your model::
        
        from yacaptcha.fields import YandexCaptchField
        class TestForm(forms.Form):
            captcha = YandexCaptchField()
