# !/usr/bin/python
# -*- coding: utf-8 -*-
import os

DEBUG = True
SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'sqlite:///db_zlwd.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
