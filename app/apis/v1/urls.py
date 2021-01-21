#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/1/16 0016 16:03
@Author    :Alex Zhang
@File      :urls.py
@Desc      :api路由关系
"""

from flask_restful import Api

from . import api_v1
from app.apis.v1.resource.user import UserResource
from app.apis.v1.resource.post import PostResource
from app.apis.v1.resource.category import CategoryResource

api = Api(api_v1, catch_all_404s=False)

api.add_resource(UserResource, '/user/<int:id>', endpoint='user')
api.add_resource(UserResource, '/user', endpoint='users')
api.add_resource(PostResource, '/post/<int:id>', endpoint='post')
api.add_resource(PostResource, '/post', endpoint='posts')
api.add_resource(CategoryResource, '/category/<int:id>', endpoint='category')
api.add_resource(CategoryResource, '/category', endpoint='categories')
