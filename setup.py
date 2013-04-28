#!/usr/bin/env python
# Encoding: utf-8
# See: <http://docs.python.org/distutils/introduction.html>
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = eval(filter(lambda _:_.startswith("VERSION"),
    file("src/fabistrano.py").readlines())[0].split("=")[1])

setup(
    name             = "fabistrano",
    version          = VERSION,
    description      = "Capistrano style deployments with Fabric",
    author           = "Diego Lapiduz",
    author_email     = "diego@lapiduz.com",
    url              = "http://github.com/dlapiduz/fabistrano",
    download_url     = "https://github.com/dlapiduz/fabistrano/tarball/%s" % (VERSION),
    keywords         = ["fabric", "dlapiduz", "capistrano",],
    install_requires = ["fabric",],
    package_dir      = {"":"src"},
    py_modules       = ["fabistrano"],
    license          = "License :: OSI Approved :: BSD License",
    classifiers      = [
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
    ],
)
