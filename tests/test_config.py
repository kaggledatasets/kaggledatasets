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

"""Tests for Core Config"""

from kaggledatasets.core.config import * # pylint: disable=wildcard-import,unused-wildcard-import


def test_constants():
    """
    Test constants
    """

    assert KAGGLE_DIR_NAME == ".kaggle"
    assert KAGGLE_CONFIG_FILE_NAME == "kaggle.json"
    assert JSON_KEY_USERNAME == "username"
    assert JSON_KEY_TOKEN == "key"
