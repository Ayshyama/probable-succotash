from django.core.management.base import BaseCommand
from ...models import Product

class Command(BaseCommand):
    help = "Seeds the database with initial Products."

    def handle(self, *args, **options):
        products_data = [
            # Ladestation
            {
                "name": "Zaptec Pro MID mit Rückplatte",
                "description": "22 kW, RFID, MID-Zähler, Lastmanagement. Preis gemäß Angebot (zzgl. Installation)",
                "price": 900.00,
                "category": "station"
            },
            # Ladezubehör (Ladekabel)
            {
                "name": "Ladekabel Mode 3 Typ 2 (11 kW, 5m glatt)",
                "description": "Ladekabel mit 5 Meter Länge, glatt",
                "price": 199.95,
                "category": "cable"
            },
            {
                "name": "Ladekabel Mode 3 Typ 2 (11 kW, 7,5m glatt)",
                "description": "Ladekabel mit 7,5 Meter Länge, glatt",
                "price": 219.95,
                "category": "cable"
            },
            {
                "name": "Ladekabel Mode 3 Typ 2 (22 kW, 7,5m glatt)",
                "description": "Ladekabel mit 7,5 Meter Länge, glatt",
                "price": 239.95,
                "category": "cable"
            },
            # Weiteres Zubehör (treat as "cable" to avoid adding a new category)
            {
                "name": "Wandhalter für Typ 2 Ladekabel",
                "description": "Diebstahlsicherung für Kabel",
                "price": 29.95,
                "category": "cable"
            },
            {
                "name": "Typ 2 Schuko-Adapter",
                "description": "Typ 2 Schuko-Adapter mit 0,5 Meter Kabel bis 16 Ampere",
                "price": 65.95,
                "category": "cable"
            },
            # RFID-Lösung
            {
                "name": "RFID-Transponder",
                "description": "Chargetic RFID-Schlüssel in ansprechendem Design",
                "price": 8.00,
                "category": "rfid"
            },
        ]

        for product_info in products_data:
            obj, created = Product.objects.get_or_create(
                name=product_info["name"],
                defaults={
                    "description": product_info["description"],
                    "price": product_info["price"],
                    "category": product_info["category"],
                    "is_active": True,
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {obj.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Skipped (already exists): {obj.name}"))

        self.stdout.write(self.style.SUCCESS("Product seeding completed!"))
