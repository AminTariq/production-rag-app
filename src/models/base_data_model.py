from helpers.config import get_settings


class BaseDataModel:
    def __init__(self, dbclient: object):
        self.dbclient = dbclient
        self.app_settings = get_settings()