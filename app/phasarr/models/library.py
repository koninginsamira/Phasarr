from datetime import datetime, timezone
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from phasarr import db
from phasarr.models.user import User


class Library(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(index=True)
    path: Mapped[str] = mapped_column(unique=True, nullable=False)

    created_by_id: Mapped[int] = mapped_column(
        ForeignKey(User.id), index=True, nullable=False)
    created_by: Mapped[User] = relationship(
        "User", foreign_keys=created_by_id, back_populates='libraries_created')
    created_at: Mapped[datetime] = mapped_column(
        index=True, nullable=False, default=lambda: datetime.now(timezone.utc))
    
    updated_by_id: Mapped[int] = mapped_column(
        ForeignKey(User.id), index=True, nullable=True)
    updated_by: Mapped[User] = relationship(
        "User", foreign_keys=updated_by_id, back_populates='libraries_updated')
    updated_at: Mapped[datetime] = mapped_column(
        index=True, nullable=True)