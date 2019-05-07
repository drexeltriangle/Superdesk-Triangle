# -*- coding: utf-8; -*-
#
# This file is part of Triangle Superdesk.
#
# Copyright 2019 The Triangle and contributors.
#
# Custom error codes and messages can be defined here.

from superdesk.errors import SuperdeskPublishError

class AppleNewsError(SuperdeskPublishError):
    _codes = {
        50000: 'Article couldn"t be converted to Apple news format',
        50001: 'Failed to publish article to Apple News'
    }

    @classmethod
    def AppleNewsFormatter(cls, exception=None, destination=None):
        return AppleNewsError(50000, exception, destination)

    @classmethod
    def AppleNewsPublishError(cls, exception=None, destination=None):
        return AppleNewsError(50001, exception, destination)