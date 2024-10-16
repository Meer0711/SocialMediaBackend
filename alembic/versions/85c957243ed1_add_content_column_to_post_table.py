"""add content column to post table

Revision ID: 85c957243ed1
Revises: 6ea2e9517222
Create Date: 2024-10-15 23:13:00.628133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '85c957243ed1'
down_revision: Union[str, None] = '6ea2e9517222'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
