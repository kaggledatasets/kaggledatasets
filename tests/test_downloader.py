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

"""Tests for Core Downloader"""

from kaggledatasets.core.downloader import build_command, COMMAND_DOWNLOAD, COMMAND_LIST_FILES


def test_build_command():
    """
    Test Build Command for Kaggle API execution
    """

    example_owner = "ownerUser"
    example_dataset = "datasetSlug"
    example_file_path = "/home/username"

    assert build_command(command="download", author=example_owner, slug=example_dataset, \
    file_path=example_file_path, use_force=False) == COMMAND_DOWNLOAD + " " + \
    example_owner + "/" + example_dataset + " -p " + example_file_path
    assert build_command(command="download", author=example_owner, slug=example_dataset, \
    file_path=example_file_path, use_force=True) == COMMAND_DOWNLOAD + " " + \
    example_owner + "/" + example_dataset + " -p " + example_file_path + " --force"
    assert build_command(command="download", author=example_owner, slug=example_dataset, \
    file_path=None, use_force=False) == COMMAND_DOWNLOAD + \
    " " + example_owner + "/" + example_dataset
    assert build_command(command="download", author=example_owner, slug=example_dataset, \
    file_path=None, use_force=True) == COMMAND_DOWNLOAD + " " \
    + example_owner + "/" + example_dataset + " --force"
    assert build_command(command="list", author=example_owner, slug=example_dataset, \
    file_path=None, use_force=False) == COMMAND_LIST_FILES + " " \
    + example_owner + "/" + example_dataset + " --csv"
