# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['markdown-it']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'markdown-it',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Orlando Diaz',
    'author_email': 'harushariel48@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7',
}


setup(**setup_kwargs)
