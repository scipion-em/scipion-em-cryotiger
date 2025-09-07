=========================
Scipion plugin for CryoTIGER
=========================

.. image:: https://img.shields.io/pypi/v/scipion-em-cryotiger.svg
        :target: https://pypi.python.org/pypi/scipion-em-cryotiger
        :alt: PyPI release

.. image:: https://img.shields.io/pypi/l/scipion-em-cryotiger.svg
        :target: https://pypi.python.org/pypi/scipion-em-cryotiger
        :alt: License

.. image:: https://img.shields.io/pypi/pyversions/scipion-em-cryotiger.svg
        :target: https://pypi.python.org/pypi/scipion-em-cryotiger
        :alt: Supported Python versions

.. image:: https://img.shields.io/sonar/quality_gate/scipion-em_scipion-em-cryotiger?server=https%3A%2F%2Fsonarcloud.io
        :target: https://sonarcloud.io/dashboard?id=scipion-em_scipion-em-cryotiger
        :alt: SonarCloud quality gate

.. image:: https://img.shields.io/pypi/dm/scipion-em-cryotiger
        :target: https://pypi.python.org/pypi/scipion-em-cryotiger
        :alt: Downloads

This plugin provide a wrapper around the program `CryoTIGER <https://github.com/turonova/cryoTIGER/>`_ to use it within 
`Scipion <https://scipion-em.github.io/docs/release-3.0.0/index.html>`_ framework.

Installation
------------

You will need to use `3.0 <https://scipion-em.github.io/docs/release-3.0.0/docs/scipion-modes/how-to-install.html>`_ 
version of Scipion to be able to run these protocols. To install the plugin, you have two options:


a) Stable version:

.. code-block::

    scipion3 installp -p scipion-em-cryotiger

b) Developer's version

    * download the repository from github:

    .. code-block::

        git clone -b devel https://github.com/scipion-em/scipion-em-cryotiger.git

    * install:

    .. code-block::

        scipion3 installp -p /path/to/scipion-em-cryotiger --devel

To check the installation you can run the plugin's tests:

``scipion3 test --grep cryotiger --run``

Configuration variables
-----------------------
**CONDA_ACTIVATION_CMD**: If undefined, it will rely on conda command being in the
PATH (not recommended), which can lead to execution problems mixing scipion
python with conda ones. One example of this could can be seen below but
depending on your conda version and shell you will need something different:

CONDA_ACTIVATION_CMD = eval "$(/extra/miniconda3/bin/conda shell.bash hook)"

**CRYOTIGER_ENV_ACTIVATION** (default = conda activate cryotiger-1.0.0):
Command to activate the CryoTIGER environment.

Downloaded crYOLO and JANNI general models can be found in the following locations:

* ``<SCIPION_HOME>/software/em/cryotiger_model-[model_version]``
* ``<SCIPION_HOME>/software/em/vimeo_model-[model_version]``

Licensing
---------

CryoTIGER software package is available under `GNU GPLv3 <https://opensource.org/license/gpl-3-0>`_

Protocols
---------

        * **Tilt-series interpolation.**: Takes dose-filtered tilt-series and outputs its interpolation using cryoTIGER.

Supported versions
---------

1.0.0

References
----------

        * Turonova, B. et al. cryoTIGER: Deep-Learning Based Tilt Interpolation Generator for Enhanced Reconstruction in Cryo Electron Tomography. BioRxiv, 2024.
