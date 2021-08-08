#!/usr/bin/env python3

import setuptools
from convertor import __version__

setuptools.setup(
    name='leet-tools',
    version=__version__,
    description='This is a test leet task',
    zip_safe=False,
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'leet-test-task-decode = convertor.__main__:decode',
            'leet-test-task-encode = convertor.__main__:encode',
        ]
    },
)


