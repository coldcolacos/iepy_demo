# iepy

## platform
ubuntu==16.04 (bit-64)

python==3.5.6

numpy==1.14.5 // or you will get a RuntimeWarning 'numpy.dtype changed, expected 96, got 88'.

## install virtualenvwrapper for python3
export WORKON_HOME=$HOME/.config/iepy/workon_home

export PROJECT_HOME=$HOME/.config/iepy/project_home

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3

source $HOME/.local/bin/virtualenvwrapper.sh

## install openjdk-8-jre for iepy
export JAVAHOME=/usr/bin/java    // This the path of executable file java*, not path of java files.

## Overview

### workon_home
ie_1

### project_home
test1_zh // Stanford CoreNLP (Chinese supported)
