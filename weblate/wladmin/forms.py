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

from __future__ import unicode_literals

from crispy_forms.helper import FormHelper
from django import forms
from django.utils.translation import ugettext_lazy as _

from weblate.accounts.forms import EmailField


class ActivateForm(forms.Form):
    secret = forms.CharField(
        label=_("Activation token"),
        required=True,
        max_length=400,
        help_text=_(
            "Please enter activation token obtained when making the subscription."
        ),
    )


class SSHAddForm(forms.Form):
    host = forms.CharField(label=_("Hostname"), required=True, max_length=400)
    port = forms.IntegerField(
        label=_("Port"), required=False, min_value=1, max_value=65535
    )

    def __init__(self, *args, **kwargs):
        super(SSHAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_class = "form-inline"
        self.helper.field_template = "bootstrap3/layout/inline_field.html"


class TestMailForm(forms.Form):
    email = EmailField(
        required=True,
        label=_("Email"),
        help_text=_("The test email will be sent to this address."),
    )
