

-- Requirement

Need Cython , numpy, versioneer, pandas

``
pip3 install Cython, numpy, versioneer, pandas
``

issue
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-s79ngknd/pandas/

need to upgrade pip
python -m pip install -U pip

pip3 install setuptools
pip3 install ez_setup


issue 
configparser.NoSectionError: No section: 'versioneer'

pip install "versioneer[toml]"