# -*- encoding: utf-8 -*-

#**********************************************************************************************************************#
#                                        PYTOOLBOX - TOOLBOX FOR PYTHON SCRIPTS
#
#  Main Developer : David Fischer (david.fischer.ch@gmail.com)
#  Copyright      : Copyright (c) 2012-2015 David Fischer. All rights reserved.
#
#**********************************************************************************************************************#
#
# This file is part of David Fischer's pytoolbox Project.
#
# This project is free software: you can redistribute it and/or modify it under the terms of the EUPL v. 1.1 as provided
# by the European Commission. This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See the European Union Public License for more details.
#
# You should have received a copy of the EUPL General Public License along with this project.
# If not, see he EUPL licence v1.1 is available in 22 languages:
#     22-07-2013, <https://joinup.ec.europa.eu/software/page/eupl/licence-eupl>
#
# Retrieved from https://github.com/davidfischer-ch/pytoolbox.git

from __future__ import absolute_import, division, print_function, unicode_literals

import argparse, os

from pytoolbox import types
from pytoolbox.argparse import is_dir, is_file, FullPaths

from . import base


class TestArgparse(base.TestCase):

    tags = ('argparse', )

    def test_is_dir(self):
        self.equal(is_dir('/home'), '/home')
        with self.raises(argparse.ArgumentTypeError):
            is_dir('sjdsajkd')

    def test_is_file(self):
        self.equal(is_file('/etc/hosts'), '/etc/hosts')
        with self.raises(argparse.ArgumentTypeError):
            is_file('wdjiwdji')

    def test_full_paths(self):
        namespace = types.DummyObject()
        multi = FullPaths(None, 'multi')
        multi(None, namespace, ['a', 'b'])
        single = FullPaths(None, 'single')
        single(None, namespace, 'c')
        self.list_equal(namespace.multi, [os.path.abspath(e) for e in ('a', 'b')])
        self.equal(namespace.single, os.path.abspath('c'))
