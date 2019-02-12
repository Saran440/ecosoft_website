# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ThemeCustomize(models.Model):
    _name = 'theme.customize'

    name = fields.Char(
        string='Name',
    )
    biography = fields.Html()
