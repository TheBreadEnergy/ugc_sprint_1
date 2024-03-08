import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    APISPEC_SPEC = APISpec(
        title="UGC Service",
        description="API для отправки событий о пользовательских действиях",
        version="0.1.0",
        plugins=[MarshmallowPlugin()],
        openapi_version="2.0.0",
    )
    APISPEC_SWAGGER_URL = "/swagger/"
    APISPEC_SWAGGER_UI_URL = "/api/ucg/"
    DEBUG = os.environ.get("DEBUG", "True") == "True"
    REQUEST_ID_UNIQUE_VALUE_PREFIX = os.environ.get(
        "REQUEST_ID_UNIQUE_VALUE_PREFIX", ""
    )
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", default="secret")
    JWT_ACCESS_TOKEN_EXPIRES = int(
        os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", default=3600)
    )
    JWT_REFRESH_TOKEN_EXPIRES = int(
        os.environ.get("JWT_REFRESH_TOKEN_EXPIRES", default=3600)
    )
    BOOTSTRAP_SERVERS = os.environ.get(
        "BOOTSTRAP_SERVERS", default="158.160.24.130:9094"
    )
    AUTO_OFFSET_RESET = os.environ.get("AUTO_OFFSET_RESET", default="earliest")
    ENABLE_AUTO_COMMIT = bool(os.environ.get("ENABLE_AUTO_COMMIT", default="False"))
    RETRY_BACKOFF_MS = int(os.environ.get("RETRY_BACKOFF_MS", default=500))
    KAFKA_CLICK_TOPIC = os.environ.get("KAFKA_CLICK_TOPIC", default="click")
    KAFKA_SEEN_TOPIC = os.environ.get("KAFKA_SEEN_TOPIC", default="seen")
    KAFKA_VIDEO_TOPIC = os.environ.get("KAFKA_VIDEO_TOPIC", default="video-quality")
    KAFKA_FILM_TOPIC = os.environ.get("KAFKA_FILM_TOPIC", default="film-view")
    KAFKA_FILTER_TOPIC = os.environ.get("KAFKA_FILTER_TOPIC", default="filter")
    JAEGER_HOST = os.environ.get("JAEGER_HOST", default="localhost")
    JAEGER_PORT = int(os.environ.get("JAEGER_PORT", default=4317))