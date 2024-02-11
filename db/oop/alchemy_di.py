from config import do_retry_on_fail
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy import select, update


class DBWorker:
    def __init__(self, engine) -> None:
        self.engine = engine

    @do_retry_on_fail
    def select_execute(self, stmt):
        with Session(self.engine) as session:
            return session.execute(stmt).all()

    @do_retry_on_fail
    def session_scalars(self, stmt):
        with Session(self.engine) as session:
            return session.scalars(stmt).all()

    @do_retry_on_fail
    def session_execute_commit(self, stmt):
        with Session(self.engine) as session:
            session.execute(stmt)
            session.commit()

    def custom_orm_select(
        self,
        cls_from: list,
        where_params: list = None,
        sql_limit: int = None,
        join_on: list | dict = None,
    ):
        stmt = select(*cls_from) if isinstance(cls_from, list) else select(cls_from)

        if join_on:
            stmt = (
                stmt.join(*join_on)
                if isinstance(join_on, list)
                else stmt.join(**join_on)
            )

        if where_params:
            stmt = stmt.where(*where_params)

        if sql_limit:
            stmt = stmt.limit(sql_limit)

        if isinstance(cls_from, list):
            return self.select_execute(stmt)
        return self.session_scalars(stmt)

    @do_retry_on_fail
    def custom_orm_bulk_update(self, cls_to, data: list):
        with Session(self.engine) as session:
            session.execute(update(cls_to), data)
            session.commit()

    def custom_upsert(
        self,
        cls_to: list,
        index_elements: list,
        data: list[dict],
        update_set: list[str],
    ):
        stmt = insert(cls_to).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=index_elements,
            set_={x: getattr(stmt.excluded, x) for x in update_set},
        )
        self.session_execute_commit(stmt)
