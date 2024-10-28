import sqlalchemy as sql
from sqlalchemy.sql._typing import _FromClauseArgument

def get_row_count_from(db, froms: _FromClauseArgument):
    return db.session.execute(
        sql.select(sql.func.count()).select_from(froms)
    ).scalar()