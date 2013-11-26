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


CONF = cfg.CONF

API_SERVICE_OPTS = [
    cfg.StrOpt('bind_ip',
               default='0.0.0.0',
               help='IP for the server to bind to'),
    cfg.IntOpt('port',
               default=6385,
               help='The port for the server'),
    ]
CONF.register_opts(API_SERVICE_OPTS)

KDS_OPTS = [
    # cfg.StrOpt('driver', default='keystone.contrib.kds.backends.sql.KDS'),
    cfg.StrOpt('master_key_file',
               default='/etc/keystone/kds.mkey',
               help='The location of the master key file'),
    cfg.StrOpt('enctype',
               default='AES',
               help='Encryption type to use for keys'),
    cfg.StrOpt('hashtype',
               default='SHA256',
               help='Hash type to use for keys'),
    cfg.IntOpt('ticket_lifetime',
               default='3600',
               help='Validity period of a ticket (in seconds)')
]
CONF.register_group(cfg.OptGroup(name='kds',
                                 title='Key Distribution Server Options'))
CONF.register_opts(KDS_OPTS, group='kds')


def parse_args(args, default_config_files=None):
    CONF(args=args[1:],
         project='kds',
         default_config_files=default_config_files)
