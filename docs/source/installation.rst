Installation
============

*kaggledatasets requires Python 3.5+*

kaggledatasets is available in the Python Package Index via

.. code-block:: console

  $ pip install kaggledatasets

The easiest way to get started on most systems is to create a `virtualenv`

.. code-block:: console

  $ python3 -m venv kd_venv
  $ source kd_venv/bin/activate
  (kd_venv) $ pip install kaggledatasets

This will install a version of all TF and PyTorch dependencies depending on your system. See `kaggledatasets <https://kaggledatasets.github.io>`_ for more information.

If you need a different version of kaggledatasets, follow the instructions on the `kaggledatasets website <https://kaggledatasets.github.io>`_ to install the appropriate version of kaggledatasets.github.io

Install From Source
--------------------

.. code-block:: console

  $ git clone git@github.com:kaggledatasets/kaggledatasets.git
  $ cd kaggledatasets
  $ source kd_venv
  (kd_venv) $ python3 setup.py install

Once that is installed, you can run the unit tests. We recommend using X as a runner.

To resume development in an already checked-out repo:

.. code-block:: console

  $ cd kaggledatasets
  $ source kd_venv

To exit the virtual environment:

.. code-block:: console

   (kd_venv) $ deactivate


**Coming Soon**

Cloud VM Setup
---------------

This guide will cover all the setup work you have to do in order to be able to easily install kaggledatasets on a cloud VM
.
*Note that while these instructions worked when they were written, they may become incorrect or out of date. If they do, please send us a Pull Request!*

After following these instructions, you should be good to either follow the `Installation`_ instructions or the `Install From Source`_ instructions

Amazon Web Services
^^^^^^^^^^^^^^^^^^^^
**Coming Soon**

Google Cloud Engine
^^^^^^^^^^^^^^^^^^^^
**Coming Soon**

Microsoft Azure
^^^^^^^^^^^^^^^^^
**Coming Soon**