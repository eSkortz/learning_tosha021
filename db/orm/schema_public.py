from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData, Sequence
from db.orm.annotations import (
    IntegerPrimaryKey,
    TextColumnNN,
    TextColumn,
    BoolColumn,
    TimestampWTColumn,
    IntegerColumnNN,
    BigintColumn,
    IntegerColumn,
    ListTextColumn,
)


metadata_obj = MetaData(schema="public")


class Base(DeclarativeBase):
    metadata = metadata_obj


class UsersShtat(Base):
    __tablename__ = "shtat"
    id: Mapped[IntegerPrimaryKey]
    surname: Mapped[TextColumn]
    lastname: Mapped[TextColumn]
    middle_name: Mapped[TextColumn]
    departament: Mapped[TextColumn]
    post: Mapped[TextColumn]
    category_post: Mapped[TextColumn]
    date_of_job: Mapped[TimestampWTColumn]
    snils: Mapped[TextColumn]
    email_personal: Mapped[TextColumn]
    phone_mobile: Mapped[BigintColumn]
    category_departamenta: Mapped[TextColumn]
    zdanie: Mapped[TextColumn]
    date_of_birth: Mapped[TimestampWTColumn]
    gender: Mapped[TextColumn]
    fio: Mapped[TextColumn]
    inn: Mapped[BigintColumn]
    job_is_active: Mapped[BoolColumn]


class UsersRoles(Base):
    __tablename__ = "users_roles"
    id: Mapped[IntegerPrimaryKey]
    user_id: Mapped[IntegerColumn]
    role_id: Mapped[IntegerColumn]
    is_active: Mapped[BoolColumn]


class Roles(Base):
    __tablename__ = "roles"
    id: Mapped[IntegerPrimaryKey]
    name: Mapped[TextColumn]
    is_admin: Mapped[BoolColumn]
    is_moder: Mapped[BoolColumn]
    is_helper: Mapped[BoolColumn]
    is_active: Mapped[BoolColumn]


class UsersTelegram(Base):
    __tablename__ = "users_telegram"
    id: Mapped[IntegerPrimaryKey]
    telegram_id: Mapped[BigintColumn]
    telegram_name: Mapped[TextColumn]
    user_id: Mapped[IntegerColumn]
    is_active: Mapped[BoolColumn]
