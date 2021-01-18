#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/1/16 0016 16:02
@Author    :Alex Zhang
@File      :__init__.py.py
@Desc      :api蓝本构造
"""
from flask import Blueprint

api = Blueprint('api', __name__)

from . import urls
