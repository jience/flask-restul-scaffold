#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/1/16 0016 16:06
@Author    :Alex Zhang
@File      :errors.py
@Desc      :
"""
from flask import jsonify
from flask_restful import abort


# 自定义返回格式中的code
class ResponseCode:
    CODE_SUCCESS = 200
    CODE_CREATED = 201
    CODE_ACCEPTED = 202
    CODE_NO_CONTENT = 204
    CODE_BAD_REQUEST = 400
    CODE_UNAUTHORIZED = 401
    CODE_FORBIDDEN = 403
    CODE_NOT_FOUND = 404
    CODE_SERVER_ERROR = 500

    msg = {
        CODE_SUCCESS: "请求成功",
        CODE_CREATED: "创建成功",
        CODE_ACCEPTED: "",
        CODE_NO_CONTENT: "删除成功",
        CODE_BAD_REQUEST: "请求参数有误",
        CODE_UNAUTHORIZED: "没有权限",
        CODE_FORBIDDEN: "禁止访问",
        CODE_NOT_FOUND: "请求资源未找到",
        CODE_SERVER_ERROR: "内部服务器错误"
    }


# 自定义返回格式中的status
class ResponseStatus:
    STATUS_SUCCESS = "SUCCESS"
    STATUS_FAIL = "FAIL"


# 自定义响应函数
def generate_response(data=None, message=ResponseCode.msg[ResponseCode.CODE_SUCCESS], status=ResponseCode.CODE_SUCCESS):
    return {
        "status": status,
        "message": message,
        "data": data
    }


# 自定义API视图abort()
def api_abort(http_status_code, **kwargs):
    if http_status_code == 400:
        abort(400, **generate_response(data=kwargs.get("data"), message=ResponseCode.msg[ResponseCode.CODE_BAD_REQUEST],
                                       status=ResponseCode.CODE_BAD_REQUEST))
    elif http_status_code == 404:
        abort(404, **generate_response(data=kwargs.get("data"), message=ResponseCode.msg[ResponseCode.CODE_NOT_FOUND],
                                       status=ResponseCode.CODE_NOT_FOUND))
    elif http_status_code == 500:
        abort(500, **generate_response(data=kwargs.get("data"), message=ResponseCode.msg[ResponseCode.CODE_SERVER_ERROR],
                                       status=ResponseCode.CODE_SERVER_ERROR))
    abort(http_status_code)
