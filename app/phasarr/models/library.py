from datetime import datetime, timezone
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from phasarr import db
from phasarr.models.user import User


class Library(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(index=True)
    path: Mapped[str] = mapped_column(nullable=False)

    created_by_id: Mapped[int] = mapped_column(
        ForeignKey(User.id), index=True, nullable=False)
    created_by: Mapped[User] = relationship("User", back_populates='libraries_created')
    created_at: Mapped[datetime] = mapped_column(
        index=True, nullable=False, default=lambda: datetime.now(timezone.utc))