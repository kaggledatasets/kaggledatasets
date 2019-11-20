if [[ "$TRAVIS_OS_NAME" != "windows" ]]; then
  if [[ "$TRAVIS_OS_NAME" == "osx" ]]; then
    DOWNLOAD="MacOSX"
  elif [[ "$TRAVIS_OS_NAME" == "linux" ]]; then
    DOWNLOAD="Linux"
  fi
  export MINICONDA=$HOME/miniconda
  wget https://repo.continuum.io/miniconda/Miniconda3-latest-${DOWNLOAD}-x86_64.sh -O miniconda.sh
  bash miniconda.sh -b -p $MINICONDA
else
  export MINICONDA=/c/miniconda
  MINICONDA_WIN=$(cygpath --windows $MINICONDA)
  choco install openssl.light
  choco install miniconda3 --params="'/AddToPath:0 /D:$MINICONDA_WIN'"
  source $MINICONDA/Scripts/activate
fi
source $MINICONDA/etc/profile.d/conda.sh
hash -r
conda config --set always_yes yes
if [[ "$TRAVIS_OS_NAME" != "windows" ]]; then
  conda update -q conda
fi
conda info -a