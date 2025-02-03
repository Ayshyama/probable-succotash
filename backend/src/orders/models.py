from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', _('Ausstehend')),
        ('confirmed', _('Bestätigt')),
        ('shipped', _('Versandt')),
        ('delivered', _('Geliefert')),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')  # Optional

    billing_name = models.CharField(_("Rechnungsname"), max_length=255)
    billing_address = models.TextField(_("Rechnungsadresse"))
    billing_zip_city = models.CharField(_("PLZ / Ort"), max_length=255)
    billing_email = models.EmailField(_("E-Mail"), blank=True, null=True)
    billing_phone = models.CharField(_("Telefon"), max_length=20, blank=True, null=True)

    same_as_billing = models.BooleanField(_("Lieferadresse entspricht Rechnungsadresse"), default=True)
    shipping_name = models.CharField(_("Liefername"), max_length=255, blank=True, null=True)
    shipping_address = models.TextField(_("Lieferadresse"), blank=True, null=True)
    shipping_zip_city = models.CharField(_("PLZ / Ort (Lieferung)"), max_length=255, blank=True, null=True)

    parking_spot = models.CharField(_("Stellplatznummer"), max_length=50, blank=True, null=True)

    signature = models.TextField(_("Unterschrift"), blank=True, null=True)  # For basic Signature Pad JS
    order_date = models.DateField(_("Bestelldatum"), auto_now_add=True)
    status = models.CharField(_("Bestellstatus"), max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Bestellung {self.id} - {self.billing_name}"

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('station', _('Ladestation')),
        ('accessory', _('Ladezubehör')),
        ('rfid', _('RFID-Lösung')),
    ]

    name = models.CharField(_("Produktname"), max_length=255)
    description = models.TextField(_("Beschreibung"), blank=True)
    price = models.DecimalField(_("Preis"), max_digits=10, decimal_places=2)
    category = models.CharField(_("Kategorie"), max_length=20, choices=CATEGORY_CHOICES)
    # activity Flag - preserves data integrity and prevents accidental deletions
    is_active = models.BooleanField(_("Active"), default=True)  # Soft delete + PROTECT

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name=_("Bestellung"))
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name=_("Produkt"))
    quantity = models.PositiveIntegerField(_("Menge"), default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} (Bestellung {self.order.id})"
