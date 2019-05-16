# -*- coding: utf-8; -*-
#
# This file is part of Triangle Superdesk.
#
# Copyright 2019 The Triangle and contributors.
#
# This file is forked from AAP Superdesk
# https://github.com/superdesk/superdesk-aap/blob/master/server/aap/subscriber_transmit_references/resource.py

import logging
from superdesk.resource import Resource


logger = logging.getLogger(__name__)


class SubscriberTransmitReferenceResource(Resource):
    schema = {
        # superdesk id of the item
        'item_id': {
            'type': 'string'
        },
        'subscriber_id': Resource.rel('subscribers'),
        # reference_id points to the unique id in the subscriber system
        'reference_id': {
            'type': 'string'
        },
        'extra': {'type': 'dict'}
    }
    internal_resource = True
    mongo_indexes = {
        'item_id_1': [('item_id', 1)],
        'subscriber_id_1': [('subscriber_id', 1)],
        'reference_id_1': [('reference_id', 1)]
    }
    item_methods = []
    resource_methods = []