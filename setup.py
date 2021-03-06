# Created on 2013.07.11
#
# @author: Giovanni Cannata
#
# Copyright 2015 Giovanni Cannata
#
# This file is part of ldap3.
#
# ldap3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ldap3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with ldap3 in the COPYING and COPYING.LESSER files.
# If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from os import path
from datetime import datetime
from platform import uname, python_version, python_build, python_compiler


version_file = open('_version.py')
exec_local = dict()
exec(version_file.read(), dict(), exec_local)
__version__ = exec_local['__version__']
__author__ = exec_local['__author__']
__email__ = exec_local['__email__']
__license__ = exec_local['__license__']
__url__ = exec_local['__url__']
__description__ = exec_local['__description__']
__long_description__ = exec_local['__long_description__']
__package_name__ = exec_local['__package_name__']
__package_folder__ = exec_local['__package_folder__']
__status__ = exec_local['__status__']

version_file.close()

project_version_file = open(path.join(__package_folder__, __package_name__, 'version.py'), 'w+')
project_version_file.write('\n'.join([
    '# version file for ' + __package_name__,
    '# generated on ' + datetime.now().__str__(),
    '# on system ' + str(uname()),
    '# with Python ' + python_version() + ' - ' + str(python_build()) + ' - ' + python_compiler(),
    '#',
    '__version__ = ' + "'" + __version__ + "'",
    '__author__ = ' + "'" + __author__ + "'",
    '__email__ = ' + "'" + __email__ + "'",
    '__url__ = ' + "'" + __url__ + "'",
    '__description__ = ' + "'" + __description__ + "'",
    '__status__ = ' + "'" + __status__ + "'",
    '__license__ = ' + "'" + __license__ + "'"]))

project_version_file.close()

setup(name=__package_name__,
      version=__version__,
      packages=['ldap3',
                'ldap3.core',
                'ldap3.abstract',
                'ldap3.operation',
                'ldap3.protocol',
                'ldap3.protocol.sasl',
                'ldap3.protocol.schemas',
                'ldap3.protocol.formatters',
                'ldap3.strategy',
                'ldap3.compat',
                'ldap3.utils',
                'ldap3.extend',
                'ldap3.extend.novell',
                'ldap3.extend.microsoft',
                'ldap3.extend.standard'],
      package_dir={'': __package_folder__},
      install_requires=['pyasn1 >= 0.1.7'],
      license=__license__,
      author=__author__,
      author_email=__email__,
      description=__description__,
      long_description=__long_description__,
      keywords='python3 python2 ldap',
      url=__url__,
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Intended Audience :: System Administrators',
                   'Operating System :: Microsoft :: Windows',
                   'Operating System :: POSIX :: Linux',
                   'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP']
      )
