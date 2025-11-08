from typing import List,Optional
import math

class Point:
    def _init_(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    def _repr_(self):
        return f"Point({self.lat}, {self.lon})"

class Infrastructure:
    def _init_(self, index: int=0, km_jud: int = 0, km_nat: int = 0, km_euro: int = 0, km_auto: int = 0):
        self.index = index
        self.km_jud = km_jud
        self.km_nat = km_nat
        self.km_euro = km_euro
        self.km_auto = km_auto

    def _repr_(self):
        return (f"Infrastructure(index={self.index}, km_jud={self.km_jud}, "
                f"km_nat={self.km_nat}, km_euro={self.km_euro}, km_auto={self.km_auto})")


class EnergyStorage:
    def _init_(self, name: str, coordinates: Point):
        self.name = name
        self.coordinates = coordinates

    def _repr_(self):
        return f"EnergyStorage(name={self.name}, coordinates={self.coordinates})"

class Zone:
    def _init_(self,
                 A: Point,
                 B: Point,
                 C: Point,
                 D: Point,
                 min_alt: int = 0,
                 max_alt: int = 0,
                 roughness: int = 0,
                 air_density: float = 0.0,
                 avg_wind_speed: float = 0.0,
                 power_avg: float = 0.0,
                 land_type: str = "",
                 potential: float = 0.0,
                 infrastructure: Optional[Infrastructure] = None):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.min_alt = min_alt
        self.max_alt = max_alt
        self.roughness = roughness
        self.air_density = air_density
        self.avg_wind_speed = avg_wind_speed
        self.power_avg = power_avg
        self.land_type = land_type
        self.potential = potential
        self.infrastructure = infrastructure or Infrastructure()

    def _repr_(self):
        return f"{self.A}, {self.B}, {self.C}"

class Region:
    def _init_(self,
                 center: Point,
                 A: Point,
                 B: Point,
                 C: Point,
                 D: Point,
                 avg_temperature: float = 0.0,
                 wind_rose: Optional[List[float]] = None,
                 rating: int = 0,
                 max_potential: Optional[Zone] = None,
                 avg_potential: float = 0.0,
                 closest_storage: Optional[EnergyStorage] = None,
                 infrastructure_rating: int = 0,
                 index_average: float = 0.0):
        self.center = center
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.avg_temperature = avg_temperature
        self.wind_rose = wind_rose
        self.rating = rating
        self.max_potential = max_potential
        self.avg_potential = avg_potential
        self.closest_storage = closest_storage
        self.infrastructure_rating = infrastructure_rating
        self.index_average = index_average
        self.zones: List[List[Zone]] = []

    def _repr_(self):
        return (f"{self.center}, {self.A}, {self.B}, {self.C}")