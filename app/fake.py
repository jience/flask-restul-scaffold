#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@Time      :2021/1/20 0020 17:11
@Author    :Alex Zhang
@File      :fake.py
@Desc      :使用Faker生成测试使用DB数据
"""
from random import randint

from faker import Faker
from sqlalchemy.exc import IntegrityError

from app import db
from app.models import User, Post, Category


def users(count=100):
    fake = Faker()
    i = 0
    while i < count:
        u = User(username=fake.user_name(), email=fake.email())
        db.session.add(u)
        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            db.session.rollback()


def posts(count=100):
    fake = Faker()
    user_count = User.query.count()
    category_count = Category.query.count()
    for i in range(count):
        u = User.query.offset(randint(0, user_count - 1)).first()
        c = Category.query.offset(randint(0, category_count - 1)).first()
        post = Post(title=fake.company(), body=fake.text(),
                    pub_date=fake.past_date(),
                    user=u,
                    category=c)
        db.session.add(post)
    db.session.commit()
