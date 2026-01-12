from database import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Book(db.Model):
    # __tablename__ = "books" # Valfri
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(
        String(50)
    )  # String(50) importeras from sqlalchemy
    page_count = mapped_column(db.Integer)
