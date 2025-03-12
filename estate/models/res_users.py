from odoo import models,fields,api # type: ignore
from odoo.exceptions import UserError,ValidationError # type: ignore
from odoo.tools import float_utils # type: ignore

class ResUsers(models.Model):
    _inherit = 'res.users'

    property_ids=fields.One2many("estate.property","user_id",string="Propriétés",domain=['|',('state', '=', 'new'),('state', '=', 'offer_received')])

 
        