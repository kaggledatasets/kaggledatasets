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

"""Wine Reviews Dataset"""

from kaggledatasets.core.dataset import Dataset


class WineReviews(Dataset):
    r"""
    Wine Reviews Dataset
    130k wine reviews with variety, location, winery, price, and description
    """

    author = "zynicide"
    slug = "wine-reviews"
    title = "Wine Reviews"
    files = ["winemag-data-130k-v2.json"]

    def __init__(self, root=None, download=False):
        r"""
        Initializer for the Wine Reviews Dataset
        """

        super(WineReviews, self).__init__(author=self.author, slug=self.slug, \
        title=self.title, root=root, download=download)

    def __getitem__(self, idx):
        r"""
        This will return one sample of data
        """
        raise NotImplementedError

    def __len__(self):
        r"""
        This denotes the total number of samples
        """
        raise NotImplementedError

    def data_frame(self):
        r"""
        This will return pandas data frame for using in Scikit Learn or raw processing
        """

        import pandas as pd # pylint: disable=import-error

        location = self.get_files()

        return pd.read_json(location[0])

    def load(self, batch_size=1):
        r"""
        This will return tf dataset for Tensorflow 2.0
        """

        # working on converting json to tf dataset

    def data_loader(self):
        r"""
        This will return data loader for PyTorch
        """

        # import torch # pylint: disable=import-error
