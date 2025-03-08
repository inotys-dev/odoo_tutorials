from odoo import models,fields # type: ignore

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description="Estate Property Type"
    name=fields.Char(required=True,string="Type")
   
    