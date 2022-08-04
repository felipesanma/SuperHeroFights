import logging
from collections import namedtuple

from .dto import DTO

dto_result = namedtuple("result", ["dto_class", "status_code"])
json_result = namedtuple("result", ["json_response", "status_code"])

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class BaseApi:
    """
    Clase base para todos los demás módulos de collections
    """

    def __init__(self, config):
        self.base_url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api"
        self.session = config.session
        self.timeout = config.timeout
        self.id = config.id

    def call_api(self, endpoint):
        url = self._build_url(endpoint)
        return self.get_result(url)

    def build_url(self, endpoint):
        raise NotImplementedError

    def get_result(
        self, *, dto_class: DTO = None, url: str
    ) -> dto_result or json_result:
        """
        Dada una URL, realiza un get request y obtiene el resultado json con su código de estado
        :param url: superhero endpoint
        :return: a namedtuple
        """
        response = self.session.get(url, timeout=self.timeout)
        if response.status_code == 200:
            if "application/json" in response.headers.get("Content-Type"):
                json_response = response.json()
                class_object = (
                    dto_class(**json_response) if dto_class else json_response
                )
                output = dto_result(class_object, response.status_code)
            else:

                json_response = response.text
                output = json_result(json_response, response.status_code)
        else:
            json_response = response.content
            output = json_result(json_response, response.status_code)
        logger.debug("## GET RESPONSE FROM SUPERHERO ")
        logger.debug(output)
        return output
