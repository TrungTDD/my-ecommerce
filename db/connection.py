import logging
from typing import Annotated

from fastapi import Depends
from fastapi.exceptions import HTTPException
from mongoengine import connect, disconnect
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

logger = logging.getLogger(__name__)


def get_shop_db():
    try:
        yield connect(alias="shop-db-alias", host="mongodb://localhost:27017/shop_dev")
    except ServerSelectionTimeoutError as e:
        logger.error("Connection failure: %s", e)
        raise HTTPException("Could not connect to Database")
    finally:
        logger.debug("Database connection closed")
        disconnect(alias="shop-db-alias")


ShopConnectionDepend = Annotated[MongoClient, Depends(get_shop_db)]
