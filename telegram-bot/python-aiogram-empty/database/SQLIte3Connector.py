from idlelib.debugobj_r import remote_object_tree_item

import config.Config as config
import aiosqlite

async def get_cursor():
    db = await aiosqlite.connect(config.Config().DB_FILE)
    cursor = await db.cursor()
    return cursor

async def create_tables():
    tables = [

    ]

    for table in tables:
        cursor = await get_cursor()
        await cursor.execute(table)

    print("[DB] Tables created or loaded!")