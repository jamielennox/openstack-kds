# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import datetime

from oslo.config import cfg

from kds.common import crypto
from kds.db import api as dbapi

CONF = cfg.CONF
KEY_SIZE = 16


class StorageManager(object):

    @classmethod
    def get_instance(cls):
        _instance = getattr(cls, '_instance', None)

        if not _instance:
            _instance = cls._instance = cls()

        return _instance

    def __init__(self):
        self.dbapi = dbapi.get_instance()
        self.crypto = crypto.CryptoManager()

        self.ttl = datetime.timedelta(seconds=int(CONF.kds.ticket_lifetime))

    def retrieve_key(self, key_id):
        """Retrieves a key from the driver and decrypts it for use.

        :param string key_id: Key Identifier

        :return string: raw key data or None if not found
        """
        keys = self.dbapi.get_shared_keys(key_id)

        if not keys:
            return None

        return self.crypto.decrypt_keyblock(key_id, keys[0], keys[1])

    def store_key(self, key_id, keyblock):
        """Encrypt a key and store it to the backend.

        :param string key_id: Key Identifier
        :param string keyblock: raw key data
        """
        sig, enc = self.crypto.encrypt_keyblock(key_id, keyblock)
        self.dbapi.set_shared_keys(key_id, sig, enc)

    def create_group(self, name):
        return self.dbapi.create_group(name)

    def delete_group(self, name):
        return self.dbapi.delete_group(name)
