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

from kds.common import config
from kds.openstack.common import log


def prepare_service(argv=[]):
    cfg.set_defaults(log.log_opts,
                     default_log_levels=['sqlalchemy=WARN',
                                         'eventlet.wsgi.server=WARN'
                                         ])
    config.parse_args(argv)
    log.setup('kds')
