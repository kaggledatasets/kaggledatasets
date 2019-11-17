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

"""Kaggle Dataset"""

import os

from kaggledatasets.core.fileops import check_if_exists
from kaggledatasets.core.downloader import download_dataset, list_files


class Dataset(object):  # pylint: disable=E0012,R0205
    r"""
    This class contains kaggle dataset related methods.
    All the other datasets will inherit this class for making custom datasets.

    Attributes:
        root (str): Custom location where dataset should be downloaded
        download (bool): Flag to download the dataset
        author (str): Username of the author who uploaded this kaggle dataset
        slug (str): Slug of the Kaggle dataset
        title (str): Title of the kaggle dataset
        is_downloaded (bool): Status of dataset if already downloaded
        files (list): List of files with their name, size and creation date
    """
    download = False
    is_downloaded = False
    files = [None]
    author = None
    slug = None
    title = None

    # pylint: disable=too-many-arguments
    def __init__(self, author, slug, title, root=None, download=False):
        r"""
        Reads the root and download argument provided for the dataset
        """

        self.author = author
        self.slug = slug
        self.title = title
        self.root = root
        self.download = download
        self.is_downloaded = self._check_if_exists()

        if not self.is_downloaded:
            if not download:
                print("dataset is not downloaded, set flag download=True in constructor") # pylint: disable=C0325
            else:
                self.download_files(use_force=False)
        else:
            if not download:
                print("dataset is already downloaded") # pylint: disable=C0325
            else:
                self.download_files(use_force=True)

        self.files = self.get_files()

    def _check_if_exists(self):
        r"""
        Checks if the dataset already exists at the given root location

        Returns:
            bool: Returns true if all files exist, else false
        """

        # TODO: recursively travel to check if all files are present # pylint: disable=W0511
        return check_if_exists(self.get_files())

    def list_files(self):
        r"""
        Returns a list of files available for this dataset

        Returns:
            list: List of python dict containing file name, size, creation date
        """

        list_files(self.author, self.slug)

    def get_files(self):
        r"""
        Returns a list of files downloaded for this dataset

        Returns:
            list: List of python dict containing file name, size, creation date
        """

        # TODO: return list of all files with their location # pylint: disable=W0511
        if self.root is None:
            return self.slug
        return os.path.join(self.root, self.slug)

    def download_files(self, use_force=False):
        r"""
        Downloads all the files available for this dataset
        """

        download_dataset(self.author, self.slug, file_path=self.root, use_force=use_force)

    def __getitem__(self, idx):
        r"""
        Returns the dataset file existing in list of files by given index

        Returns:
            dict: File information like name, size and creation date
        """

        return self.files[idx]
