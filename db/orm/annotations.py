from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import (
    TEXT,
    TIMESTAMP,
    NUMERIC,
    BIGINT,
    DOUBLE_PRECISION,
    BOOLEAN,
    INTEGER,
    ARRAY,
    SMALLINT,
    VARCHAR,
    DATE,
    MONEY,
    JSONB
)
from typing import Annotated
import datetime


IntegerPrimaryKey = Annotated[
    int,
    mapped_column(
        INTEGER,
        primary_key=True,
        nullable=False,
        index=True,
    ),
]

BigintPrimaryKey = Annotated[
    int,
    mapped_column(
        BIGINT,
        primary_key=True,
        nullable=False,
        index=True,
    ),
]

TextPrimaryKey = Annotated[
    str,
    mapped_column(
        TEXT,
        primary_key=True,
        nullable=False,
        index=True,
    ),
]

BigintColumn = Annotated[
    int,
    mapped_column(BIGINT),
]

SmallintColumn = Annotated[
    int,
    mapped_column(SMALLINT),
]

IntegerColumn = Annotated[
    int,
    mapped_column(INTEGER),
]

MoneyColumn = Annotated[
    float,
    mapped_column(MONEY),
]

IntegerColumnNN = Annotated[
    int,
    mapped_column(
        INTEGER,
        nullable=False,
    ),
]

TextColumn = Annotated[
    str,
    mapped_column(TEXT),
]

TextColumnNN = Annotated[
    str,
    mapped_column(
        TEXT,
        nullable=False,
    ),
]

BoolColumn = Annotated[
    bool,
    mapped_column(BOOLEAN),
]

BoolColumnNN = Annotated[
    bool,
    mapped_column(
        BOOLEAN,
        nullable=False,
    ),
]

DoubleColumn = Annotated[
    float,
    mapped_column(DOUBLE_PRECISION),
]

NumericColumn = Annotated[
    int,
    mapped_column(NUMERIC),
]

VarcharColumn = Annotated[
    str,
    mapped_column(VARCHAR),
]

TimestampColumn = Annotated[
    datetime.datetime,
    mapped_column(TIMESTAMP),
]

TimestampWTColumn = Annotated[
    datetime.datetime,
    mapped_column(
        TIMESTAMP(timezone=False),
    ),
]

DateColumn = Annotated[
    datetime.datetime,
    mapped_column(DATE),
]

ListIntegerColumn = Annotated[
    list[int],
    mapped_column(ARRAY(INTEGER)),
]

ListTextColumn = Annotated[
    list[str],
    mapped_column(ARRAY(TEXT)),
]

ListSmallintColumn = Annotated[
    list[int],
    mapped_column(SMALLINT),
]

ListJsonbColumn = Annotated[
    list[dict],
    mapped_column(ARRAY(JSONB))
]