#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/1/16 0016 16:07
@Author    :Alex Zhang
@File      :post.py
@Desc      :
"""
from flask import abort
from flask_restful import Resource, fields, marshal_with

from app.models import Post


# 格式化输出
post_fields = {
    'id': fields.Integer(),
    'title': fields.String(),
    'body': fields.String(),
    'pub_date': fields.DateTime(dt_format='iso8601')
}


class PostResource(Resource):
    @marshal_with(post_fields)
    def get(self, post_id=None):
        if post_id:
            post = Post.query.get(post_id)
            if not post:
                abort(404)

            return post

        posts = Post.query.all()
        return posts
