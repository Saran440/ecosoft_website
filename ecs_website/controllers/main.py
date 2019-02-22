# -*- coding: utf-8 -*-
from odoo import http


class RouteWebsite(http.Controller):
    @http.route('/ecosoft/', auth='public', website=True)
    def index(self, **kw):
        print(kw)
        return http.request.render('ecs_website.index')

    @http.route('/ecosoft/<model("theme.customize"):teacher>/',
                auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('ecs_website.biography', {
            'person': teacher
        })
