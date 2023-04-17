from functools import cached_property
from typing import Dict, List, Optional
from urllib.parse import ParseResult, parse_qs, urlparse

import logging
import os

from pydantic import BaseModel
from zzz.yyy import load
from ldclient.config import Config as LDConfig
from ldclient.client import LDClient
from ldclient.integrations import Files as LDFiles

from django.db import models
from django.utils.translation import ugettext_lazy as _

class SocialApp(models.Model):
    member1 = "1"

class SocialAccount(models.Model):
    member2 = "2"

class SocialToken(models.Model):
    app = models.ForeignKey(SocialApp, on_delete=models.CASCADE)
    account = models.ForeignKey(SocialAccount, on_delete=models.CASCADE)
    token = models.TextField(verbose_name=_('token'), help_text=_('help'))
    expires_at = models.DateTimeField(blank=True, null=True, verbose_name=_('expires at'))
    def getToken(self):
        return self.token
    def getExpiry(self):
        return self.expires_at


class DatabaseConfiguration(BaseModel):
    url: str
    connect_timeout: int = 5000  # ms
    statement_timeout: int = 500  # ms

    @property
    def host(self) -> str:
        return self._parsed_url.hostname

    @property
    def port(self) -> int:
        return self._parsed_url.port

    @property
    def username(self) -> str:
        return self._parsed_url.username

    @property
    def password(self) -> str:
        return self._parsed_url.password

    @property
    def database(self) -> str:
        return self._parsed_url.path.strip("/")

    @property
    def use_ssl(self) -> bool:
        ssl = self._parsed_query.get("ssl", [])
        return "true" in [s.lower() for s in ssl]

    @cached_property
    def _parsed_url(self) -> ParseResult:
        return urlparse(configuration.db.url)

    @cached_property
    def _parsed_query(self) -> Dict[str, List[str]]:
        return parse_qs(self._parsed_url.query)


class DjangoConfiguration(BaseModel):
    secret_key: str
    allowed_hosts: str
    debug: bool = False
    launchdarkly_key: str = ""
    aws_storage_bucket_name: str
    aws_static_storage_bucket_name: str


class GoogleConfiguration(BaseModel):
    client_id: Optional[str] = None


class SentryConfiguration(BaseModel):
    dsn: str


class LaunchDarklyConfiguration(BaseModel):
    sdk_key: Optional[str] = None
    config_file: Optional[str] = None  # for local development only

    def client_config(self) -> LDConfig:
        if self.sdk_key:
            return self.__online_config()
        if self.config_file:
            return self.__file_config()
        return self.__offline_config()

    def __online_config(self) -> LDConfig:
        logger.info("LaunchDarkly configured in online mode")
        return LDConfig(self.sdk_key)

    def __file_config(self) -> LDConfig:
        config_file = os.path.abspath(self.config_file)
        logger.info("LaunchDarkly configured from file %s", config_file)
        data_source = LDFiles.new_data_source(paths=[config_file], auto_update=True)
        return LDConfig("fake-sdk-key", update_processor_class=data_source, send_events=False)

    # noinspection PyMethodMayBeStatic
    def __offline_config(self) -> LDConfig:
        logger.info("LaunchDarkly configured in offline mode; flags will use default values")
        return LDConfig("fake-sdk-key", offline=True, send_events=False)


class LoggingConfiguration(BaseModel):
    default_level: str = "INFO"
    django_level: str = "INFO"


class Configuration(BaseModel):
    environment: str
    django: DjangoConfiguration
    google: GoogleConfiguration
    sentry: Optional[SentryConfiguration] = None
    launchdarkly: LaunchDarklyConfiguration = LaunchDarklyConfiguration()
    log: LoggingConfiguration = LoggingConfiguration()


configuration = Configuration.parse_obj(load("finance", key_separator="__"))
launchdarkly = LDClient(configuration.launchdarkly.client_config())