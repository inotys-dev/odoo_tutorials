from odoo import models,fields,api # type: ignore

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description="Estate Property Type"
    _order = "sequence,name"

    name=fields.Char(required=True,string="Type")
    sequence = fields.Integer('Sequence', default=1, )
    property_ids=fields.One2many("estate.property","property_type_id",string="Propriétés")
    offer_ids=fields.One2many("estate.property.offer","property_type_id",string="Offres")
    offers_count=fields.Integer(compute='_compute_offer_count',string="Nombre d'offres")

    _sql_constraints = [
        ('name', 'unique(name)', "Le type doit être unique"),
    ]
    
    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for type in self:
            type.offers_count = len(type.offer_ids)


