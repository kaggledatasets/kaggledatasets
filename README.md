# kaggledatasets

Collection of Kaggle Datasets ready to use for Everyone

![License](https://img.shields.io/github/license/kaggledatasets/kaggledatasets) 
![Release](https://img.shields.io/github/v/release/kaggledatasets/kaggledatasets)
![Platform Support](https://img.shields.io/pypi/pyversions/kaggledatasets)

- [More about Kaggle Datasets](#more-about-kaggle-datasets)
- [Installation](#installation)
  - [Binaries](#binaries)
  - [From Source](#from-source)
- [Getting Started](#getting-started)
- [Communication](#communication)
- [Releases and Contributing](#releases-and-contributing)
- [License](#license)

|  System |                                Python 3.5                               |                                Python 3.6                               |                                Python 3.7                               |
|:-------:|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
|  Linux  | ![Build Status](https://travis-matrix-badges.herokuapp.com/repos/kaggledatasets/kaggledatasets/branches/master/1) | ![Build Status](https://travis-matrix-badges.herokuapp.com/repos/kaggledatasets/kaggledatasets/branches/master/2) | ![Build Status](https://travis-matrix-badges.herokuapp.com/repos/kaggledatasets/kaggledatasets/branches/master/3) |
|  macOS  |                                                                         | ![Build Status](https://travis-matrix-badges.herokuapp.com/repos/kaggledatasets/kaggledatasets/branches/master/4) | ![Build Status](https://travis-matrix-badges.herokuapp.com/repos/kaggledatasets/kaggledatasets/branches/master/5) |
| Windows | ![Build Status](https://travis-matrix-badges.herokuapp.com/repos/kaggledatasets/kaggledatasets/branches/master/6) | ![Build Status](https://travis-matrix-badges.herokuapp.com/repos/kaggledatasets/kaggledatasets/branches/master/7) | ![Build Status](https://travis-matrix-badges.herokuapp.com/repos/kaggledatasets/kaggledatasets/branches/master/8) |

## More About Kaggle Datasets

```python
import kaggledatasets as kd

heart_disease = kd.structured.HeartDiseaseUCI(download=True)

# Returns the pandas data frame to be used in Scikit Learn or any other framework
df = heart_disease.data_frame()

# Returns the tensorflow dataset type compatible with TF 2.0
dataset = heart_disease.load()
for batch, label in dataset.take(1):
    for key, value in batch.items():
        ...

# Returns the data loader for PyTorch
# Work in progress for PyTorch support
```

## Installation

### Binaries

Commands to install from binaries via Conda or pip wheels are on our website: [https://kaggledatasets.github.io](https://kaggledatasets.github.io)

### From Source

#### Get the kaggledatasets Source

```
git clone --recursive https://github.com/kaggledatasets/kaggledatasets
cd kaggledatasets
```

#### Install Dependencies

```
pip install -r requirements.txt
```

#### Install kaggledatasets

```
python setup.py install
```

## Getting Started

* [Tutorials: Get started with kaggledatasets](https://kaggledatasets.github.io/get-started)
* [Examples: Easy to understand kaggledatasets code](https://github.com/kaggledatasets/kaggledatasets/tree/master/examples)
* [API Reference](https://kaggledatasets.readthedocs.io)

## Communication

* **GitHub Issues**: bug reports, feature requests, dataset requests, install issues, help wanted, thoughts, etc.
* **Slack**: The [Kaggle Datasets Slack](https://kaggledatasets.slack.com/) hosts a primary audience of moderate to experienced Kaggle Datasets users and developers for general chat, online discussions, collaboration etc. If you need a slack invite, please visit: [http://bit.ly/kdslack](http://bit.ly/kdslack)

## Releases and Contributing

kaggledatasets is expecting to have a 30 day release cycle (major releases). Please let us know if you encounter a bug by [filing an issue](https://github.com/kaggledatasets/kaggledatasets/issues).  

We appreciate all contributions and make sure you go through our [Contributing Guide](CONTRIBUTING.md). If you are planning to contribute back bug-fixes, please do so without any further discussion.  

If you plan to contribute new features, new datasets, utility functions or extensions to the core, please first open an issue and discuss the feature with us.
Sending a PR without discussion might end up resulting in a rejected PR, because we might be taking kaggledatasets in a different direction than you might be aware of.

## License

kaggledatasets is Apache-2.0 licensed, as found in the [LICENSE](LICENSE) file.
