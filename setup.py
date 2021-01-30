import os
from setuptools import setup


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
    py_modules=['pyutils'],
    # entry_points={
    #     'distutils.commands': [
    #         'upload_sphinx = sphinx_pypi_upload:UploadDoc',
    #     ],
    # },
)
