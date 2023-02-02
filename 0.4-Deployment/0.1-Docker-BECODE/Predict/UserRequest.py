from typing import Dict

from pydantic import BaseModel


class UserRequest(BaseModel):
    city: str
    houseType: str
    number_of_rooms: int
    living_area: int
    furnished: bool
    garden: bool
    fully_equipped_kitchen: bool

    def toModelDict(self) -> Dict[str, int]:
        return {
            f"{self.city}": 1,
            f"{self.houseType}": 1,
            "number_of_rooms": self.number_of_rooms,
            "living_area": self.living_area,
            "furnished": int(self.furnished),
            "garden": int(self.garden),
            "fully_equipped_kitchen": int(self.fully_equipped_kitchen),
        }
