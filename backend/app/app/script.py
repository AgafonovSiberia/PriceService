import time

from app.infrastructure.db.factory import create_pool
from app.logger import logger
from app.services.core import update_orders_to_database
from sqlalchemy.orm.session import sessionmaker

# Quota limits to GoogleSheets APi. Per minute per user per project - 60
GOOGLE_API_TIMEOUT = 3


def script_run():
    logger.info("Script started")
    pool: sessionmaker = create_pool()

    while True:
        update_orders_to_database(pool=pool)
        time.sleep(GOOGLE_API_TIMEOUT)


if __name__ == "__main__":
    script_run()
