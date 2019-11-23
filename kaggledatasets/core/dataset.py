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
from abc import abstractmethod

from kaggledatasets.core.fileops import check_if_exists
from kaggledatasets.core.downloader import download_dataset


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

        if not download:
            if not self.is_downloaded:
                raise Exception("dataset is not downloaded, set flag download=True in constructor") # pylint: disable=C0325
            print("dataset is already downloaded") # pylint: disable=C0325
        else:
            self.download_files(use_force=True)

    def _check_if_exists(self):
        r"""
        Checks if the dataset already exists at the given root location

        Returns:
            bool: Returns true if all files exist, else false
        """

        files = self.get_files()
        for file_path in files:
            if not check_if_exists(file_path):
                return False

        return True

    def get_files(self):
        r"""
        Returns a list of files downloaded for this dataset

        Returns:
            list: List of python dict containing file name, size, creation date
        """

        basepath = self.slug
        if self.root:
            basepath = os.path.join(self.root, self.slug)

        files = []
        for filename in self.files:
            files.append(os.path.join(basepath, filename))

        return files

    def download_files(self, use_force=False):
        r"""
        Downloads all the files available for this dataset
        """

        download_dataset(self.author, self.slug, file_path=self.root, use_force=use_force)

    def __getitem__(self, index):
        r"""
        This will return one sample of data
        """
        raise NotImplementedError

    def __len__(self):
        r"""
        This denotes the total number of samples
        """
        raise NotImplementedError

    @abstractmethod
    def data_frame(self):
        r"""
        This will return pandas data frame for using in Scikit Learn or raw processing
        """
        raise NotImplementedError

    @abstractmethod
    def load(self, batch_size=1):
        r"""
        This will return tf dataset for Tensorflow 2.0
        """
        raise NotImplementedError

    @abstractmethod
    def data_loader(self):
        r"""
        This will return data loader for PyTorch
        """
        raise NotImplementedError
