from re import S
import sys
from pymongo import MongoClient
import pymongo


def setup(db_name: str, collection_name: str, *, domain: str = None, port: int = None):
    """Setup connection to db and handle any exception that occurs"""
    domain_str = f"{domain}:{port}" if domain and port else "localhost:27017"
    try:
        conn = MongoClient(host=[domain_str], serverSelectionTimeoutMS=3000)
        conn.server_info()  # raises an exception if the connection to the host was not successfull
    except pymongo.errors.ServerSelectionTimeoutError as err:
        sys.exit("pymongo ERROR: Connection Refused")

    try:
        db = conn[db_name]
        collection = db[collection_name]
        return collection
    except pymongo.errors.PyMongoError as err:
        raise err


if __name__ == "__main__":
    setup(db_name="s", collection_name="d")
