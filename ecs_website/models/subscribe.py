# -*- coding: utf-8 -*-
from odoo import models, fields, api


class EmailSubscribe(models.Model):
    _name = 'subscribe.post'

    contact_email = fields.Char(
        string='Email',
    )

    @api.model
    def create(self, vals):
        res = super(EmailSubscribe, self).create(vals)
        return res
