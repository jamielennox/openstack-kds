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

import abc

from oslo.config import cfg
import six

from kds.openstack.common.db import api as db_api
from kds.openstack.common import log

CONF = cfg.CONF

_BACKEND_MAPPING = {'sqlalchemy': 'kds.db.sqlalchemy.api'}

IMPL = db_api.DBAPI(backend_mapping=_BACKEND_MAPPING)
LOG = log.getLogger(__name__)


def get_instance():
    """Return a DB API instance."""
    return IMPL


@six.add_metaclass(abc.ABCMeta)
class Connection(object):

    @abc.abstractmethod
    def set_shared_keys(self, kds_id, sig, enc):
        """Set key related to kds_id."""

    @abc.abstractmethod
    def get_shared_keys(self, kds_id):
        """Get key related to kds_id.

        :param string: Key Identifier
        :returns tuple(string, string): signature key, encryption key
        :raises: keystone.exception.ServiceNotFound
        """

    @abc.abstractmethod
    def set_group_key(self, group_name, key, expiration):
        pass

    @abc.abstractmethod
    def get_group_key(self, group_name):
        pass

    @abc.abstractmethod
    def create_group(self, group_name):
        pass

    @abc.abstractmethod
    def delete_group(self, group_name):
        pass
