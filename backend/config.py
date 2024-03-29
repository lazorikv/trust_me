import os

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DATABASE_CONNECT_OPTIONS = {}

    # Turn off Flask-SQLAlchemy event system
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Application threads. A common general assumption is
    # using 2 per available processor cores - to handle
    # incoming requests using one and performing background
    # operations using the other.
    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    WTF_CSRF_ENABLED = True

    # Use a secure, unique and absolutely secret key for
    # signing the data.
    CSRF_SESSION_KEY = os.getenv('CSRF_SESSION_KEY')

    # Secret key for signing cookies
    if os.environ.get('SECRET_KEY'):
        SECRET_KEY = os.environ.get('SECRET_KEY')
    else:
        SECRET_KEY = 'SECRET'

    # for email with sendgrid
    SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
    SENDGRID_DEFAULT_FROM = 'admin@yourdomain.com'

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')


class DevelopmentConfig(Config):
    """Statement for enabling the development environment"""
    # Define the database - we are working with
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5433/homie"
    DEBUG = True
    FLATCOKE = "development"
    S3_BUCKET = "lazoryktrust"
    S3_KEY = "AKIAQGAJE5MV4P22XF4O"
    S3_SECRET = "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"
    S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


class APIConfig(Config):
    """Statement for enabling the api environment"""
    # Define the database - we are working with
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'dev.db')
    WTF_CSRF_ENABLED = False


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'test.db')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'api': APIConfig,
}
