# Copyright 2021 Ingeos
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import models, fields, api


class OpStudent(models.Model):
    _inherit = 'op.student'

    middle_name = fields.Char("Middle Name", size=128, required=True)
    last_name = fields.Char("Last Name", size=128)

    @api.onchange('first_name', 'middle_name', 'last_name')
    def _onchange_name(self):
        if not self.last_name:
            self.name = str(self.first_name) + " " + str(self.middle_name)
        else:
            self.name = str(self.first_name) + " " + str(
                self.middle_name) + " " + str(self.last_name)
