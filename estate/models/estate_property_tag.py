from odoo import models,fields # type: ignore

class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description="Estate Property Tag"
    _order = "name"

    name=fields.Char(required=True,string="Tag")
    color=fields.Integer(string="Couleur")
    _sql_constraints = [
        ('name', 'unique(name)', "Le tag doit être unique"),
    ]
   
    