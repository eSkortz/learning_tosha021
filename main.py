from config import engine_async
from db.oop.alchemy_di_async import DBWorkerAsync
from db.orm.schema_public import UsersShtat, UsersRoles, Roles, UsersTelegram
import asyncio
import datetime
from aiogram.types import Message


db_worker = DBWorkerAsync(engine_async)


async def check_user_exist(message: Message):
    is_user_exist = await db_worker.custom_orm_select(
        cls_from=UsersTelegram,
        where_params=[UsersTelegram.telegram_id == message.chat.id],
    )
    if is_user_exist == []:
        return "на регистрацию"

    user_in_db: UsersTelegram = is_user_exist[0]
    if user_in_db.is_active == False:
        return "вам бан"

    user_in_shtat = await db_worker.custom_orm_select(
        cls_from=UsersShtat, where_params=[UsersShtat.id == user_in_db.user_id]
    )
    user_in_shtat: UsersShtat = user_in_shtat[0]

    user_roles_id = await db_worker.custom_orm_select(
        cls_from=UsersRoles.role_id,
        where_params=[UsersRoles.user_id == user_in_shtat.id],
    )
    user_roles = []
    for id in user_roles_id:
        role = await db_worker.custom_orm_select(
            cls_from=Roles, where_params=[Roles.id == id]
        )
        user_roles.append(role)

    user_data = {"info": user_in_shtat, "roles": user_roles}
    return user_data


async def create_role_for_user(user_id: int, role_id: int) -> None:
    data_for_db = {
        'user_id': user_id,
        'role_id': role_id,
        'is_active': True
    }
    await db_worker.custom_upsert(cls_to=UsersRoles, index_elements=['user_id', 'role_id'], data=data_for_db, update_set=['is_active'])


async def main():
    user_data = await check_user_exist(Message)
    info: UsersShtat = user_data["info"]
    roles: Roles = user_data["roles"]

    if roles == []:
        await bot.send_message(chat_id=uu, text=f'Такой то пользователь {info.id} {info.fio} не имеет ролей, ему нужно их назначить')