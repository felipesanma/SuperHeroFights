from .base_api import BaseApi
from .dto import Connections


class CharacterConnections(BaseApi):
    def _build_url(self, endpoint):
        return self.base_url + endpoint

    def get(self):

        url = self._build_url(f"/connections/{self.id}.json")
        return self.get_result(dto_class=Connections, url=url)
