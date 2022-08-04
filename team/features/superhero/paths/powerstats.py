from .base_api import BaseApi
from .superhero_api_dto import Powerstats


class CharacterPowerStats(BaseApi):
    def _build_url(self, endpoint):
        return self.base_url + endpoint

    def get(self):

        url = self._build_url(f"/powerstats/{self.id}.json")
        return self.get_result(dto_class=Powerstats, url=url)
