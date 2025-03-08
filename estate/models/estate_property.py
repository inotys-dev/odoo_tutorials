from odoo import models,fields,api # type: ignore
from odoo.exceptions import UserError # type: ignore

class EstateProperty(models.Model):
    _name = "estate.property"
    _description="Estate Property"
    name=fields.Char(required=True,string="Titre")
    description=fields.Text()
    postcode=fields.Char(string="Code Postal")
    date_availability=fields.Date(string="Disponible à partir du",copy=False, default=fields.Date.add(fields.Date.today(),months=3))
    expected_price=fields.Float(required=True,string="Prix attendu")
    selling_price=fields.Float(readonly=True, copy=False,string="Prix de vente")
    bedrooms=fields.Integer(default=2,string="Chambres")
    living_area=fields.Integer(string="Surface (m²)")
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean(string="Jardin")
    garden_area=fields.Integer(string="Surface du jardin (m²)")
    garden_orientation=fields.Selection(
        selection=[('north','Nord'),('south','Sud'),('east','Est'),('west','Ouest')]
        ,string="Orientation du jardin"
    )
    active=fields.Boolean(default=True, string="Active")
    state=fields.Selection(
        selection=[('new','Nouveau'),('offer_received','Offre reçue'),('offer_accepted','Offre acceptée'),('sold','Vendue'),('canceled','Annulée')],
        default='new', copy=False  ,string="Statut"
    )
    property_type_id = fields.Many2one("estate.property.type", string="Type")
    partner_id=fields.Many2one("res.partner", string="Acheteur")
    user_id = fields.Many2one('res.users', copy=False,string='Vendeur', index=True, tracking=True, default=lambda self: self.env.user)
    tag_ids=fields.Many2many("estate.property.tag", string="Tags")
    offer_ids=fields.One2many("estate.property.offer","property_id",string="Offres")
    total_area=fields.Float(compute='_compute_total_area',string="Surface totale (m²)")
    best_price=fields.Float(compute='_compute_best_price',string="Meilleure offre")

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for prop in self:
            prop.total_area = prop.living_area + prop.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for prop in self:
            prop.best_price = max(prop.offer_ids.mapped('price'))

    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = False

    def action_sold(self):
        if self.state=='canceled':
            raise UserError('Impossible de passer à l\'état vendue, car la propriété a été annulée')
        self.write({'state': 'sold'})
        return True


    def action_cancel(self):
        if self.state=='sold':
            raise UserError('Impossible d\'annuler une propriété vendue')
        self.write({'state': 'canceled'})
        return True

 
        