import re
from typing import Iterable, Union

from sync_identification_example import identify_plant


class PlantMatcher:
    """
        my_plants: all plants from my database
    """
    def __init__(self, my_plants: Iterable[str]):
        self._my_plants_dict = {self.prepare_name(i): i for i in my_plants}
        self._my_plants = set(self._my_plants_dict.keys())

    @staticmethod
    def prepare_name(plant_name: str) -> str:
        plant_name = re.sub(r"\b[xX]\b", "×", plant_name)  # replacing x by × in
        plant_name = plant_name.replace("×", " × ")  # making space around ×
        plant_name = re.sub(r"[\s]+", " ", plant_name.strip())  # removing duplicate spaces, tabulators etc.
        plant_name = plant_name.lower()  # all letters small
        plant_name = re.sub(r"^[^a-z]*[a-z]", lambda x: x.group().upper(), plant_name)  # first valid letter capital
        return plant_name

    def match_plant(self, plant_id_plants: Iterable) -> Union[str, None]:
        """
            plant_id_plants: Plant.id predictions - scientific_name plus synonyms

            returns plant from my_plants
        """
        for plant_id_plant in plant_id_plants:
            if plant_id_plant in self._my_plants:
                return self._my_plants_dict[plant_id_plant]

        return None

    def match_suggestion(self, suggestion: dict) -> Union[str, None]:
        """
            suggestion: suggestion from plant.id identification api
        """
        plant_details = suggestion["plant_details"]
        first_suggestion_names = [plant_details["scientific_name"]] + plant_details.get("synonyms", [])
        return self.match_plant(first_suggestion_names)


if __name__ == '__main__':
    my_plant_names = [
        'Pothos aureus',
    ]
    plant_matcher = PlantMatcher(my_plants=my_plant_names)

    result = identify_plant(["../img/photo3.jpg"])
    for suggestion in result['suggestions']:
        original_name = suggestion["plant_details"]["scientific_name"]
        matched_name = plant_matcher.match_suggestion(suggestion)
        print(f'{suggestion["probability"] * 100:>4.1f}% - {matched_name} (original name: {original_name})')
