from django_redis import get_redis_connection
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
redis_connect = get_redis_connection()
