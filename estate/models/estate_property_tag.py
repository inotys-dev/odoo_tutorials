from odoo import models,fields # type: ignore

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description="Estate Property Tag"
    name=fields.Char(required=True,string="Tag")
   
    