#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/1/16 0016 16:07
@Author    :Alex Zhang
@File      :post.py
@Desc      :
"""
from flask_restful import Resource, fields, marshal

from app.models import Post
from app.common.errors import generate_response, api_abort


# 格式化输出
post_fields = {
    'id': fields.Integer(),
    'title': fields.String(),
    'body': fields.String(),
    'pub_date': fields.DateTime(dt_format='iso8601'),
    'user_url': fields.Url(attribute='user_id', endpoint='.user', absolute=True),
    'category_url': fields.Url(attribute='category_id', endpoint='.category', absolute=True),
    'self': fields.Url(attribute='id', endpoint='.post', absolute=True)
}


class PostResource(Resource):
    def get(self, id=None):
        if id:
            post = Post.query.get(id)
            if not post:
                api_abort(404)

            return generate_response(marshal(post, post_fields))

        posts = Post.query.all()
        return generate_response(marshal(posts, post_fields))
