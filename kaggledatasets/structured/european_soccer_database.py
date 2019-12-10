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

"""European Soccer Database Dataset"""

from kaggledatasets.core.dataset import Dataset


class EuropeanSoccerDatabase(Dataset):
    r"""
    European Soccer Database Dataset
    25k+ matches, players & teams attributes for European Professional Football
    """

    author = "hugomathien"
    slug = "soccer"
    title = "European Soccer Database"
    files = ["database.sqlite"]

    def __init__(self, root=None, download=False):
        r"""
        Initializer for the European Soccer Database Dataset
        """

        super(EuropeanSoccerDatabase, self).__init__(author=self.author, slug=self.slug, \
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
        import sqlite3 # pylint: disable=import-error

        location = self.get_files()

        connection = sqlite3.connect(location[0])

        return pd.read_sql_query("SELECT * FROM Country", connection)

    def load(self, batch_size=1):
        r"""
        This will return tf dataset for Tensorflow 2.0
        """

        # working on converting sqlite data to tf dataset

    def data_loader(self):
        r"""
        This will return data loader for PyTorch
        """

        # import torch # pylint: disable=import-error
