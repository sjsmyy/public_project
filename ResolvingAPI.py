#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
url = 'http://0.0.0.0:8802/get_userData'
req = requests.get(url, timeout=30)
req_json = req.json()