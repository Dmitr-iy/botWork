import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id, user_name):
        await self.connector.execute("CREATE TABLE IF NOT EXISTS users (user_id BIGINT PRIMARY KEY, user_name TEXT);")
        query = f"INSERT INTO users (user_id, user_name) VALUES ({user_id}, '{user_name}')" \
                f"ON CONFLICT (user_id) DO UPDATE SET user_name='{user_name}';"
        await self.connector.execute(query)


