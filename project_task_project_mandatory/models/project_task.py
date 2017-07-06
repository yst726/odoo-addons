# -*- coding: utf-8 -*-
# © 2015-2017 Elico corp (https://www.elico-corp.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class ProjectTask(models.Model):
    _inherit = 'project.task'

    project_id = fields.Many2one(required=True)
