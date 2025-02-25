# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2019 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

"""
Tests for unicode sorting.
"""

from __future__ import unicode_literals

from unittest import SkipTest

from django.test import TestCase

import weblate.trans.util


class SortTest(TestCase):
    def test_sort(self):
        if not weblate.trans.util.LOCALE_SETUP:
            raise SkipTest("Failed to setup locales")
        result = weblate.trans.util.sort_choices(
            ((2, "zkouška"), (3, "zkouzka"), (1, "zkouaka"))
        )
        self.assertEqual([1, 2, 3], [x[0] for x in result])
