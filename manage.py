#!/usr/bin/env python
import os
import sys

#burası belli başlı komutları terminal ekranın çalıştırmamızı saglayan dosya,
#calışmış fonk ise, ilk olarak ayarlamarı django ya bildirir,
#artindan terminalden verdiğimiz komutları çalıştırıcak fonksiyonu cagırır hata almassak komutlar calısır

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ybblog.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
