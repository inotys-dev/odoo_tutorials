from odoo import models,fields,api # type: ignore



class EstateProperty(models.Model):
    _name = "estate.property.offer"
    _description="Estate Property Offer"
    _order = "price desc"

    price=fields.Float(string="Prix")
    
    status=fields.Selection(
        selection=[('accepted','Acceptée'),('refused','Refusée')],
         copy=False  ,string="Statut"
    )
    
    partner_id=fields.Many2one("res.partner", string="Acheteur potentiel",required=True)
    property_id=fields.Many2one("estate.property", string="Propriété",required=True)
    validity=fields.Integer(string="Validité de l'offre (jours)",default=7)
    date_deadline=fields.Date(string="Date limite",compute='_compute_date_deadline',inverse='_inverse_date_deadline')    
    property_type_id=fields.Many2one(related="property_id.property_type_id",string="Type de propriété",store=True)

    _sql_constraints = [
        ('price', 'CHECK(price > 0)',
         'Le prix de l\'offre doit être supérieur à 0'),
    ]

    
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

    def action_accept(self):
        if not self.status and self.property_id.state=='offer_received':
            self.write({'status': 'accepted'})
            self.property_id.write({'state': 'offer_accepted'})
            self.property_id.write({'partner_id': self.partner_id.id})
            self.property_id.write({'selling_price': self.price})    
            return True
        return False
        
    def action_refuse(self):
        if not self.status:
            self.write({'status': 'refused'})
            return True
        return False