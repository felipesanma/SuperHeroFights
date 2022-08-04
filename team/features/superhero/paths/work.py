from .base_api import BaseApi
from .superhero_api_dto import Work


class CharacterWork(BaseApi):
    def _build_url(self, endpoint):
        return self.base_url + endpoint

    def get(self):

        url = self._build_url(f"/work/{self.id}.json")
        return self.get_result(dto_class=Work, url=url)
