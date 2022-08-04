from collections import namedtuple

import requests

from .paths import (
    CharacterAppearance,
    CharacterBiography,
    CharacterConnections,
    CharacterImages,
    CharacterPowerStats,
    Characters,
    CharacterWork,
)

DEFAULT_TIMEOUT = 5


class SuperHero:
    """
    Cliente de superhero API
    Reference: https://akabab.github.io/superhero-api/api/
    """

    def __init__(self, *, id: int = None, session=None, timeout=None):
        session = self._init_session(session)
        timeout = timeout or DEFAULT_TIMEOUT
        config = namedtuple("config", ["id", "session", "timeout"])

        cfg = config(id, session, timeout)
        self.characters = Characters(cfg)
        self.powerstats = CharacterPowerStats(cfg)
        self.appearance = CharacterAppearance(cfg)
        self.biography = CharacterBiography(cfg)
        self.connections = CharacterConnections(cfg)
        self.work = CharacterWork(cfg)
        self.images = CharacterImages(cfg)

    def _init_session(self, session):
        """
        Inicializa la sesión
        :param session:
        :return: a requests Session object
        """
        if not session:
            session = requests.Session()

        return session
