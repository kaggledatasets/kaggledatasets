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

"""Heart Disease UCI Dataset"""

from kaggledatasets.core.dataset import Dataset


class HeartDiseaseUCI(Dataset):
    r"""
    Heart Disease UCI Dataset
    https://archive.ics.uci.edu/ml/datasets/Heart+Disease
    """

    author = "ronitf"
    slug = "heart-disease-uci"
    title = "Heart Disease UCI"
    files = ["heart.csv"]

    def __init__(self, root=None, download=False):
        r"""
        Initializer for the Heart Disease UCI Dataset
        """

        super(HeartDiseaseUCI, self).__init__(author=self.author, slug=self.slug, \
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

        return pd.read_csv(location[0])

    def load(self, batch_size=1):
        r"""
        This will return tf dataset for Tensorflow 2.0
        """

        import tensorflow as tf # pylint: disable=import-error

        location = self.get_files()

        return tf.data.experimental.make_csv_dataset(
            location[0],
            batch_size=batch_size,
            label_name='target',
            num_epochs=1,
            ignore_errors=True)

    def data_loader(self):
        r"""
        This will return data loader for PyTorch
        """

        # import torch # pylint: disable=import-error
