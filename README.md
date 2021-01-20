Table of Contents
---------------------

* [Introduction](#introduction)
* [Requirements](#requirements)
* [Installation](#installation)
* [Maintainers](#maintainers)

INTRODUCTION
------------
Sym-Crypt is a CLI tool that uses symmetric encryption/decryption. You can use this
tool to encrypt multiple values under one deciphering key. If you would like to decrypt
the values later on, you may do so as well with this tool

REQUIREMENTS
------------
QTrader has been developed on Python 3.8. If you do not have Python installed
you may download it from their [home page](https://www.python.org/downloads/).

If you choose to run the docker container of Sym-Crypt, you will have to download
docker form their [home page](https://www.docker.com/products/docker-desktop)

INSTALLATION
------------
The following installations assumes you have met the requirements within
the [requirements section](#requirements).

###Python Install
Install the dependencies list found in the `[requirements.txt]`(requirements.txt) file.
* `pip install -r requirements.txt`

###Docker Install
Create the Docker image from the [Dockerfile](Dockerfile)
* `docker build -t sym-crypt:v1.0.0 .`

EXECUTION
---------
Depending on the what route you took in the [installation step](#INSTALLATION), follow the respected path here as well.

### Python
`python main.py`

### Docker
`docker run -it qtrader:1.0`

MAINTAINERS
-----------
[Jacob Bles](https://github.com/JakePember)