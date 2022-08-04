from .base_api import BaseApi
from .superhero_api_dto import ImageSize


class CharacterImages(BaseApi):
    def _build_url(self, endpoint):
        return self.base_url + endpoint

    def get_url_by_size(self, *, size: ImageSize):

        url = self._build_url(f"/images/{size}/1-a-bomb.jpg")
        return url
