import os
from setuptools import setup, find_packages


def read(name):
    return open(os.path.join(os.path.dirname(__file__), name)).read()


setup(
    name='pyutils',
    version='0.0.1',
    author='Adriano Gil',
    author_email='adrianogil.san@gmail.com',
    url='https://github.com/adrianogil/pyutils',
    description='A set of utilities for python projects',
    long_description=read('README.md'),
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    platforms='any',
    packages=find_packages(),
    dependency_links=['http://github.com/adrianogil/pyutils/tarball/master#egg=pyutils-0.0.1'],
    include_package_data=True,
    # entry_points={
    #     'distutils.commands': [
    #         'upload_sphinx = sphinx_pypi_upload:UploadDoc',
    #     ],
    # },
)
