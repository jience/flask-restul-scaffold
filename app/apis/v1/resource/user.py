#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/1/16 0016 16:07
@Author    :Alex Zhang
@File      :user.py
@Desc      :
"""
from flask import abort
from flask_restful import Resource, fields, marshal_with

from app.models import User


# 格式化输出
user_fields = {
    'id': fields.Integer(),
    'username': fields.String(),
    'email': fields.String()
}


class UserResource(Resource):
    @marshal_with(user_fields)
    def get(self, user_id=None):
        if user_id:
            user = User.query.get(user_id)
            if not user:
                abort(404)

            return user

        users = User.query.all()
        return users
