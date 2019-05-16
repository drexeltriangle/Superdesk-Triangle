# -*- coding: utf-8; -*-
#
# This file is part of Triangle Superdesk.
#
# Copyright 2019 The Triangle and contributors.
#
# This file is forked from AAP Superdesk
# https://github.com/superdesk/superdesk-aap/blob/master/server/aap/subscriber_transmit_references/service.py

from superdesk.services import BaseService
from eve.utils import config


class SubscriberTransmitReferenceService(BaseService):
    def get_subscriber_reference(self, item_id, subscriber_id):
        return self.find_one(req=None, item_id=item_id, subscriber_id=subscriber_id)

    def insert_update_reference(self, item_id, subscriber_id, extra, reference_id):
        reference = self.find_one(req=None, reference_id=reference_id)
        if not self.find_one(req=None, reference_id=reference_id):
            self.post(
                [
                    {
                        'item_id': item_id,
                        'reference_id': reference_id,
                        'subscriber_id': subscriber_id,
                        'extra': extra
                    }
                ]
            )
        else:
            self.patch(reference.get(config.ID_FIELD), {'extra': extra})