from config import engine_async
from db.oop.alchemy_di_async import DBWorkerAsync
from db.orm.schema_public import UsersShtat, UsersSpu, UsersRoles, UsersTelegram, Roles
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


class UsersView:
    surname: str
    fio_doctor: str

    def __init__(self, user_spu: UsersSpu, user_shtat: UsersShtat) -> None:
        self.surname = user_shtat.surname
        self.fio_doctor = user_spu.fio_doctor


async def spu_join_shat():
    result = await db_worker.custom_orm_select(
        cls_from=[UsersSpu, UsersShtat],
        where_params=[
            UsersSpu.fio_doctor == UsersShtat.fio,
            UsersSpu.prikreplenie.like("%ГБУЗ ГП № 6 ДЗМ%"),
            UsersSpu.special_case_off.like("%Да%"),
        ],
        sql_limit=10,
    )
    for row in result:
        user_spu: UsersSpu = row[0]
        user_shtat: UsersShtat = row[1]
        user_view = UsersView(user_spu, user_shtat)
        print(f"{user_view.surname} \\\ {user_view.fio_doctor}")


asyncio.run(spu_join_shat())
