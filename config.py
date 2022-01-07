class Config(object):
    """
    Common configurations
    """

    #Put any configurations here that are common across all the environments

class DevelopmentConfig(Config):
    """Development configurations"""

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production Configurations
    """

    DEBUG = False

app_config = {
    "development" : DevelopmentConfig,
    "production" : ProductionConfig
              }
