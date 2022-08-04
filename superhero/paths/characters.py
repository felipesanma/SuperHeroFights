from .base_api import BaseApi
from .dto import SuperHeroCompleteInformation


class Characters(BaseApi):
    def _build_url(self, endpoint):
        return self.base_url + endpoint

    def get_all(self):

        url = self._build_url(f"/all.json")
        return self.get_result(url=url)

    def get_complete_information(self):

        url = self._build_url(f"/id/{self.id}.json")
        return self.get_result(dto_class=SuperHeroCompleteInformation, url=url)
