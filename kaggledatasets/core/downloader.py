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

"""Download Manager"""

import os
import csv
import subprocess
import zipfile


COMMAND_DOWNLOAD = "kaggle datasets download"
COMMAND_LIST_FILES = "kaggle datasets files"

def build_command(command, author, slug, file_path, use_force):
    r"""
    Given command and args, this will build kaggle api command to execute

    Returns:
        str: Kaggle API command to execute
    """

    switcher = {
        "download": COMMAND_DOWNLOAD,
        "list": COMMAND_LIST_FILES
    }

    base = switcher.get(command, "") + " " + str(author) + "/" + str(slug)

    if command == "list":
        return base + " --csv"
    if command == "download" and file_path is None:
        if use_force:
            return base + " --force"
        return base
    if use_force:
        return base + " -p " + str(file_path) + " --force"
    return base + " -p " + str(file_path)

def download_dataset(author, slug, file_path=None, use_force=False):
    r"""
    For given owner name and dataset slug, it will download all files
    """

    subprocess.call(build_command("download", author, slug, file_path, use_force).split())
    if file_path is None:
        with zipfile.ZipFile(slug+".zip", 'r') as zip_ref:
            zip_ref.extractall(slug)
        os.remove(slug+".zip")
    else:
        with zipfile.ZipFile(os.path.join(file_path, slug+".zip"), 'r') as zip_ref:
            zip_ref.extractall(os.path.join(file_path, slug))
        os.remove(os.path.join(file_path, slug+".zip"))


def list_files(author, slug):
    r"""
    For given owner name and dataset slug, it will return list of all files

    Returns:
        list: List of all files with name, size and creation date
    """

    encoding = "ascii"
    pro = subprocess.Popen(build_command("list", author, slug, \
    file_path=None, use_force=False).split(), stdout=subprocess.PIPE)
    output = pro.communicate()[0].decode(encoding)
    edits = csv.reader(output.splitlines(), delimiter=",")
    files = []
    for row in edits:
        files.append({"name": row["name"], "size": row["size"], \
        "creation_date": row["creationDate"]})

    return files
