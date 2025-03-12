from odoo import models,fields,api # type: ignore
from odoo.exceptions import UserError,ValidationError # type: ignore
from odoo.tools import float_utils # type: ignore

class EstateProperty(models.Model):
    _inherit = "estate.property"
    
    
    def action_sold(self):
        print("action_sold estate_account")
        return super(EstateProperty, self).action_sold()


    

 
        