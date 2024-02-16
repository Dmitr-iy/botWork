import asyncpg


class Request:
    def __init__(self, connector: asyncpg.pool.Pool):
        self.connector = connector

    async def add_data(self, user_id, user_name):
        await self.connector.execute("CREATE TABLE IF NOT EXISTS users (user_id BIGINT PRIMARY KEY, user_name TEXT);")
        query = f"INSERT INTO users (user_id, user_name) VALUES ({user_id}, '{user_name}')" \
                f"ON CONFLICT (user_id) DO UPDATE SET user_name='{user_name}';"
        await self.connector.execute(query)

    async def get_existing_names(self):
        query = "SELECT name_work FROM object_work;"
        results = await self.connector.fetch(query)
        existing_names = [row['name_work'] for row in results]
        return existing_names

    async def save_object(self, name_work, work_price, data_start, data_finish):
        await self.connector.execute("CREATE TABLE IF NOT EXISTS object_work (id SERIAL PRIMARY KEY, "
                                     "name_work TEXT UNIQUE NOT NULL, work_price DECIMAL(10, 2),"
                                     " expenses_object DECIMAL(10, 2), petrol_object DECIMAL(10, 2), "
                                     "petrol_work DECIMAL(10, 2));")
        query = f"INSERT INTO object_work (name_work, work_price, data_start, data_finish) VALUES ('{name_work}'," \
                f" {work_price}, '{data_start}', '{data_finish}');"
        await self.connector.execute(query)

    async def save_object_not_finish_data(self, name_work, work_price, data_start):
        await self.connector.execute("CREATE TABLE IF NOT EXISTS object_work (id SERIAL PRIMARY KEY, "
                                     "name_work TEXT UNIQUE NOT NULL, work_price DECIMAL(10, 2),"
                                     " expenses_object DECIMAL(10, 2), petrol_object DECIMAL(10, 2), "
                                     "petrol_work DECIMAL(10, 2));")
        query = f"INSERT INTO object_work (name_work, work_price, data_start) VALUES ('{name_work}'," \
                f" {work_price}, '{data_start}');"
        await self.connector.execute(query)


