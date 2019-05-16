# -*- coding: utf-8; -*-
#
# This file is part of Triangle Superdesk.
#
# Copyright 2019 The Triangle and contributors.
#
# This file is forked from AAP Superdesk
# https://github.com/superdesk/superdesk-aap/blob/master/server/aap/subscriber_transmit_references/__init__.py

import superdesk
from .resource import SubscriberTransmitReferenceResource
from .service import SubscriberTransmitReferenceService


def init_app(app):
    endpoint_name = 'subscriber_transmit_references'
    refs_service = SubscriberTransmitReferenceService(endpoint_name, backend=superdesk.get_backend())
    SubscriberTransmitReferenceResource(endpoint_name, app=app, service=refs_service)