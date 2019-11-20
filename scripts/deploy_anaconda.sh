#!/bin/bash
set -e
conda convert --platform all $HOME/miniconda2/conda-bld/linux-64/kaggledatasets-*.tar.bz2 --output-dir conda-bld/
anaconda -t $ANACONDA_API_TOKEN upload --user kaggledatasets conda-bld/**/kaggledatasets-*.tar.bz2
echo "Successfully deployed to Anaconda.org."
exit 0