from odoo import models,fields,api # type: ignore

class EstateProperty(models.Model):
    _name = "estate.property.offer"
    _description="Estate Property Offer"
    

    price=fields.Float(string="Prix")
    
    status=fields.Selection(
        selection=[('accepted','Acceptée'),('refused','Refusée')],
         copy=False  ,string="Statut"
    )
    
    partner_id=fields.Many2one("res.partner", string="Acheteur potentiel",required=True)
    property_id=fields.Many2one("estate.property", string="Propriété",required=True)
    validity=fields.Integer(string="Validité de l'offre (jours)",default=7)
    date_deadline=fields.Date(string="Date limite",compute='_compute_date_deadline',inverse='_inverse_date_deadline')    
    

    @api.depends('validity') 
    def _compute_date_deadline(self):
        for offer in self:
            if offer.create_date:
                create_date=fields.Date.from_string(offer.create_date)
                offer.date_deadline=fields.Date.add(create_date,days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            if offer.date_deadline and offer.create_date:
                create_date=fields.Date.from_string(offer.create_date)
                offer.validity=(offer.date_deadline-create_date).days