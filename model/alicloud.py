# Copyright (c) 2019-2020 SAP SE or an SAP affiliate company. All rights reserved. This file is
# licensed under the Apache Software License, v. 2 except as noted otherwise in the LICENSE file
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from model.base import (
    NamedModelElement,
)


class AlicloudConfig(NamedModelElement):
    def region(self):
        return self.raw.get('region')

    def access_key_id(self):
        return self.raw.get('access_key_id')

    def access_key_secret(self):
        return self.raw.get('access_key_secret')

    def _required_attributes(self):
        return ['region', 'access_key_id', 'access_key_secret']
