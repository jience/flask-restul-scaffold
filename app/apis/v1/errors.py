#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/1/21 0021 10:24
@Author    :Alex Zhang
@File      :errors.py
@Desc      :
"""

from app.common.errors import api_abort, generate_response, ResponseCode
from . import api_v1


@api_v1.errorhandler(400)
def bad_request(e):
    return generate_response(message=ResponseCode.msg[ResponseCode.CODE_BAD_REQUEST],
                             status=ResponseCode.CODE_BAD_REQUEST)


@api_v1.app_errorhandler(404)
def not_found(e):
    return generate_response(message=ResponseCode.msg[ResponseCode.CODE_NOT_FOUND],
                             status=ResponseCode.CODE_NOT_FOUND)


@api_v1.app_errorhandler(500)
def internal_server_error(e):
    return generate_response(message=ResponseCode.msg[ResponseCode.CODE_SERVER_ERROR],
                             status=ResponseCode.CODE_SERVER_ERROR)
