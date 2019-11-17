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

|  System |                                  Python 3.5                                  |                                  Python 3.6                                  |                                  Python 3.7                                  |
|:-------:|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
|  Linux  | ![Build Status](https://img.shields.io/travis/kaggledatasets/kaggledatasets) | ![Build Status](https://img.shields.io/travis/kaggledatasets/kaggledatasets) | ![Build Status](https://img.shields.io/travis/kaggledatasets/kaggledatasets) |
|  macOS  | ![Build Status](https://img.shields.io/travis/kaggledatasets/kaggledatasets) | ![Build Status](https://img.shields.io/travis/kaggledatasets/kaggledatasets) | ![Build Status](https://img.shields.io/travis/kaggledatasets/kaggledatasets) |
| Windows | ![Build Status](https://img.shields.io/travis/kaggledatasets/kaggledatasets) | ![Build Status](https://img.shields.io/travis/kaggledatasets/kaggledatasets) | ![Build Status](https://img.shields.io/travis/kaggledatasets/kaggledatasets) |

## More About Kaggle Datasets

```python
import kaggledatasets as kd

dataset = kd.structured.CreditCardFraudDetection(download=True)
# Returns the split for train and test in Scikit and Tensorflow
train, test = dataset.load()
# Returns the train and test data loader for PyTorch
train_dataloader, test_dataloader = dataset.dataloader()
```

## Installation

### Binaries

Commands to install from binaries via Conda or pip wheels are on our website: [https://kaggledatasets.github.io](https://kaggledatasets.github.io)

### From Source

#### Install Dependencies

```
pip install -r requirements.txt
```

#### Get the kaggledatasets Source

```
git clone --recursive https://github.com/kaggledatasets/kaggledatasets
cd kaggledatasets
```

#### Install kaggledatasets

```
python setup.py install
```

## Getting Started

* [Tutorials: Get started with understanding kaggledatasets](https://kaggledatasets.github.io/tutorials)

* [Examples: Easy to understand kaggledatasets code](https://kaggledatasets.github.io/docs/examples)

* [API Reference](https://kaggledatasets.github.io/docs)

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