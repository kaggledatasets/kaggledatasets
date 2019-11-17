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

"""File Operations"""

import os
import json

def read_json_file(file_location):
    """
    Reads the JSON file at given file location and returns the json data

    Returns:
        dict: JSON data converted into python dictionary
    """

    with open(file_location, 'r') as file_obj:
        data = file_obj.read()

    return json.loads(data)

def check_if_exists(file_location):
    """
    For given file location, checks if that file or folder exists

    Returns:
        bool: Status is true if file/folder exists, else false
    """

    return os.path.exists(file_location)
