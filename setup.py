import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='fabistrano',
    version=__import__('fabistrano').__version__,
    author='Diego Lapiduz',
    author_email='diego@lapiduz.com',
    packages=find_packages(),
    include_package_data=True,
    url='http://github.com/dlapiduz/fabistrano',
    license='License :: OSI Approved :: BSD License',
    description="Capistrano style deployments with Fabric",
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'Programming Language :: Python',      
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.md'),
    zip_safe=False,
)