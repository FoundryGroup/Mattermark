################################################################################
# Setup file for the mattermark package.
#
# Author: Carl Cortright
# Date: 1/16/2017
#
################################################################################
from distutils.core import setup
setup(
  name = 'mattermark',
  packages = ['mattermark'],
  version = '0.2',
  description = 'Wrapper for the Mattermark API',
  author = 'Carl Cortright',
  author_email = 'carl@foundrygroup.com',
  url = 'https://github.com/FoundryGroup/Mattermark',
  download_url = 'https://github.com/FoundryGroup/Mattermark/tarball/0.2',
  keywords = ['mattermark', 'api'],
  classifiers = [],
  install_requires=[
        "requests",
        "PyYAML",
        "pprint",
    ],
)
