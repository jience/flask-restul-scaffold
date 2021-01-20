#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/1/16 0016 16:07
@Author    :Alex Zhang
@File      :category.py
@Desc      :
"""
from flask_restful import Resource, fields, marshal

from app.models import Category
from app.common.errors import generate_response, api_abort


# 格式化输出
category_fields = {
    'id': fields.Integer(),
    'name': fields.String(),
    'self': fields.Url(attribute='id', endpoint='.category', absolute=True),
}


class CategoryResource(Resource):
    def get(self, id=None):
        if id:
            category = Category.query.get(id)
            if not category:
                api_abort(404)

            return generate_response(marshal(category, category_fields))

        categories = Category.query.all()
        return generate_response(marshal(categories, category_fields))
