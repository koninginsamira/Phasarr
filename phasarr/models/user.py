from datetime import datetime, timezone
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash, check_password_hash

from phasarr import db


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    
    username: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(nullable=True)

    libraries_created: Mapped[list["Library"]] = relationship( # type: ignore (prevents circular import)
        "Library", foreign_keys="Library.created_by_id", back_populates="created_by")
    libraries_updated: Mapped[list["Library"]] = relationship( # type: ignore (prevents circular import)
        "Library", foreign_keys="Library.updated_by_id", back_populates="updated_by")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)