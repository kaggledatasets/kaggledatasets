# Copyright 2019 Omkar Prabhu
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Kaggle Configuration"""

import os

from kaggledatasets.core.fileops import read_json_file
from kaggledatasets.core.utils import get_home_location


KAGGLE_DIR_NAME = ".kaggle"
KAGGLE_CONFIG_FILE_NAME = "kaggle.json"
JSON_KEY_USERNAME = "username"
JSON_KEY_TOKEN = "key"

class Config(object): # pylint: disable=E0012,R0205
    r"""
    This class contains kaggle configuration related methods

    Attributes:
        username (str): Kaggle username
        token (str): Kaggle API token
    """
    username = None
    token = None

    def __init__(self):
        r"""
        Reads the config and initializes username and token
        """

        data = self._read_config_file()
        self.username = data[JSON_KEY_USERNAME]
        self.token = data[JSON_KEY_TOKEN]

    @classmethod
    def _read_config_file(cls):
        r"""
        This will read the config file present at recommended location by Kaggle i.e.
        Windows: C:\Users\<Windows-username>\.kaggle\kaggle.json
        Linux/Mac: ~/.kaggle/kaggle.json
        """

        location = os.path.join(get_home_location(), KAGGLE_DIR_NAME, KAGGLE_CONFIG_FILE_NAME)
        return read_json_file(location)

    def get_credentials(self):
        r"""
        Returns kaggle credentials present in config file

        Returns:
            dict: kaggle config containing username and api token
        """

        return dict({
            'username': self.username,
            'token': self.token,
        })

    def get_username(self):
        r"""
        Returns kaggle username present in config file

        Returns:
            str: kaggle username
        """

        return self.username

    def get_token(self):
        r"""
        Returns kaggle api token present in config file

        Returns:
            str: kaggle api token
        """

        return self.token
