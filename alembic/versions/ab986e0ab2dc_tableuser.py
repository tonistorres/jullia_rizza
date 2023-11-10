"""tableuser

Revision ID: ab986e0ab2dc
Revises: 
Create Date: 2023-11-09 10:01:38.277908

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab986e0ab2dc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   op.create_table(
        'user',
        sa.Column('id', sa.Integer(),primary_key=True),
        sa.Column('username', sa.String(length=50), nullable=False),
        sa.Column('password', sa.String(length=10),nullable=False),
        sa.Column('name', sa.String(length=60),nullable=False),
        sa.Column('email', sa.String(length=100))
        
    )


def downgrade() -> None:
   op.drop_table(
        'user'
    )