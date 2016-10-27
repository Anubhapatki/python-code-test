from datetime import datetime
from django.core.management import BaseCommand
from shiptrader.models import Starship, Listing
from django.utils import timezone
import requests, json



# Given a path to
class Command(BaseCommand):


    def execute(self, *args, **options):

        resp = requests.get('https://swapi.co/api/starships')
        print(resp.status_code)
        star_ship_data = json.loads(resp.text)

       # starship = directory_name
        star_ships = Starship.objects.all().delete()
        for ship in star_ship_data["results"]:
            star_ship= Starship(
                name = ship["name"],
                model = ship["model"],
                starship_class = ship["starship_class"],
                manufacturer = ship["manufacturer"],
                cost_in_credits = ship["cost_in_credits"],
                length = ship["length"],
                hyperdrive_rating = ship["hyperdrive_rating"],
                cargo_capacity =  ship["cargo_capacity"],
                crew = ship["crew"],
                passengers =ship["passengers"],
                max_atmosphering_speed = ship["max_atmosphering_speed"],
                mglt = ship["MGLT"]
            )
            star_ship.save()
        star_ships = Starship.objects.all()
        for s in star_ships:
            print(s.starship_class, s.manufacturer, s.length, s.crew, s.passengers)

        print("\n")
