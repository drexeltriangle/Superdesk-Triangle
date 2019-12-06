# -*- coding: utf-8; -*-
#
# This file is part of Triangle Superdesk.
#
# Copyright 2019 The Triangle and contributors.
#
# This file is forked from AAP Superdesk
# https://github.com/superdesk/superdesk-aap/blob/master/server/aap/publish/formatters/aap_apple_news_formatter.py

from superdesk.publish.formatters import Formatter

class TriangleAppleNewsFormatter(Formatter):
    def __init__(self):
        self.format_type = 'Triangle Apple News'