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

"""Kaggle Datasets Core"""

from kaggledatasets.core.config import Config
from kaggledatasets.core.downloader import download_dataset, build_command
from kaggledatasets.core.utils import get_os, get_home_location
from kaggledatasets.core.fileops import read_json_file
from kaggledatasets.core.dataset import Dataset
