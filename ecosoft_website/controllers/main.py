# -*- coding: utf-8 -*-
from odoo import http


class RouteWebsite(http.Controller):
    @http.route('/ecosoft/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('ecosoft_website.index')

    @http.route('/ecosoft/<model("theme.customize"):teacher>/',
                auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('ecosoft_website.biography', {
            'person': teacher
        })
