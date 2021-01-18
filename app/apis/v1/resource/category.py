#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/1/16 0016 16:07
@Author    :Alex Zhang
@File      :category.py
@Desc      :
"""
from flask import abort
from flask_restful import Resource, fields, marshal_with

from app.models import Category


# 格式化输出
category_fields = {
    'id': fields.Integer(),
    'name': fields.String()
}


class CategoryResource(Resource):
    @marshal_with(category_fields)
    def get(self, category_id=None):
        if category_id:
            category = Category.query.get(category_id)
            if not category:
                abort(404)

            return category

        categories = Category.query.all()
        return categories
