# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

import noseapp


if __name__ == '__main__':
    setup(
        name='noseapp',
        version=noseapp.__version__,
        url='https://github.com/trifonovmixail/noseapp',
        packages=find_packages(),
        author='Mikhail Trifonov',
        author_email='mikhail.trifonov@corp.mail.ru',
        license='GNU LGPL',
        description='Framework for test development',
        keywords='test unittest framework nose application',
        long_description=open('README.rst').read(),
        include_package_data=True,
        zip_safe=False,
        platforms='any',
        install_requires=[
            'nose==1.3.4',
        ],
        test_suite='tests',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Topic :: Software Development :: Testing',
        ],
    )
