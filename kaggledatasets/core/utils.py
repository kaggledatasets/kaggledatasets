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

"""Core Utils"""

import os
import platform


def get_os():
    r"""
    Detects the OS and returns the platform name

    Returns:
        str: name of the os (linux, windows, darwin for macOS)
    """

    return platform.system().lower()

def get_home_location():
    r"""
    Returns the home folder location i.e.
    Windows: C:\Users\<windows username>
    Linux/Mac: /home/<username>

    Returns:
        str: home folder location
    """

    return os.path.expanduser("~")
