from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
import time
import asyncio
import functools
from env_reader import app_config


BOT_TOKEN = app_config.BOT_TOKEN.get_secret_value()

DB_LOGIN = app_config.DB_LOGIN.get_secret_value()
DB_PASSWORD = app_config.DB_PASSWORD.get_secret_value()
DB_IP = app_config.DB_IP.get_secret_value()
DB_NAME = app_config.DB_NAME.get_secret_value()


def batch_lengh_generator(step: int, data: list) -> list:
    return (data[x : x + step] for x in range(0, len(data), step))


def equal_split(list_to_split, n_parts) -> tuple:
    k, m = divmod(len(list_to_split), n_parts)
    return (
        list_to_split[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)]
        for i in range(n_parts)
    )


def retry_async(num_attempts):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            for try_index in range(num_attempts):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    print(
                        f"Exception occurred: {e}. Retrying... ({try_index}/{num_attempts})"
                    )
                    await asyncio.sleep(1)
            else:
                print(f"Failed after {num_attempts} attempts.")
        return wrapper
    return decorator


def do_retry_on_fail_async(func):
    async def wrapper(*args, **kwargs):
        reconnct_tries = 5
        for try_index in range(reconnct_tries):
            try:
                print(try_index, reconnct_tries)
                return await func(*args, **kwargs)
            except:
                print(f"Unable to execute: {func.__name__}")
                await asyncio.sleep(1)
    return wrapper


def do_retry_on_fail(func):
    def wrapper(*args, **kwargs):
        reconnct_tries = 5
        for try_index in range(reconnct_tries):
            try:
                print(try_index, reconnct_tries)
                return func(*args, **kwargs)
            except:
                print(f"Unable to execute: {func.__name__}")
                time.sleep(1)
    return wrapper


engine = create_engine(
    f"postgresql+psycopg2://{DB_LOGIN}:{DB_PASSWORD}@{DB_IP}/{DB_NAME}",
)

engine_async = create_async_engine(
    f"postgresql+asyncpg://{DB_LOGIN}:{DB_PASSWORD}@{DB_IP}/{DB_NAME}",
)
