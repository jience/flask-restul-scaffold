#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/1/16 0016 16:07
@Author    :Alex Zhang
@File      :user.py
@Desc      :
"""
from flask_restful import Resource, fields, marshal

from app.models import User
from app.common.errors import generate_response, api_abort


# 格式化输出
user_fields = {
    'id': fields.Integer(),
    'username': fields.String(),
    'email': fields.String(),
    'self': fields.Url(attribute='id', endpoint='.user', absolute=True)  # 需要注意的是url里面的参数名必须和主键(例如:id)一致
}


class UserResource(Resource):
    def get(self, id=None):
        if id:
            user = User.query.get(id)
            if not user:
                api_abort(404)

            return generate_response(marshal(user, user_fields))

        users = User.query.all()
        return generate_response(marshal(users, user_fields))
