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

from oslo.config import cfg
from pecan import hooks

from kds.api.controllers.v1 import crypto
from kds.db import manager as storage_manager


class ConfigHook(hooks.PecanHook):
    """Attach the configuration object to the request
    so controllers can get to it.
    """

    def before(self, state):
        state.request.cfg = cfg.CONF


class StorageHook(hooks.PecanHook):

    def before(self, state):
        state.request.storage_manager = \
            storage_manager.StorageManager.get_instance()


class CryptoHook(hooks.PecanHook):

    def before(self, state):
        state.request.crypto_manager = crypto.get_crypto_manager()
