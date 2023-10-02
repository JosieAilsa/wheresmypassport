from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models.meta import DBSession, Base


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""
    # Set up SQLAlchemy engine
    engine = engine_from_config(settings, "sqlalchemy.")
    # Bind session factory (DBSession) to the engine
    DBSession.configure(bind=engine)
    # Create tables when they don't exist yet
    Base.metadata.create_all(bind=engine)
    with Configurator(settings=settings) as config:
        config.include("pyramid_jinja2")
        config.include(".routes")
        config.include(".models")
        config.include("pyramid_tm")
        config.scan()
    return config.make_wsgi_app()
