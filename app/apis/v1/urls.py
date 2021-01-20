#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/1/16 0016 16:03
@Author    :Alex Zhang
@File      :urls.py
@Desc      :api路由关系
"""

from flask_restful import Api

from . import api
from app.apis.v1.resource.user import UserResource
from app.apis.v1.resource.post import PostResource
from app.apis.v1.resource.category import CategoryResource

api_v1 = Api(api)

api_v1.add_resource(UserResource, '/user/<int:id>', endpoint='user')
api_v1.add_resource(UserResource, '/user', endpoint='users')
api_v1.add_resource(PostResource, '/post/<int:id>', endpoint='post')
api_v1.add_resource(PostResource, '/post', endpoint='posts')
api_v1.add_resource(CategoryResource, '/category/<int:id>', endpoint='category')
api_v1.add_resource(CategoryResource, '/category', endpoint='categories')
