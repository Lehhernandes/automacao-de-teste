from tests.fixtures.driver import driver_func
from tests.config.settings import Settings


def before_all(context):
    context.settings = Settings()


def before_scenario(context, scenario):
    context.driver = driver_func()


def after_scenario(context, scenario):
    if hasattr(context, "driver"):
        context.driver.quit()
