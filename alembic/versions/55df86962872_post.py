"""post

Revision ID: 55df86962872
Revises: ab986e0ab2dc
Create Date: 2023-11-16 10:05:44.625460

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55df86962872'
down_revision: Union[str, None] = 'ab986e0ab2dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'post',
        sa.Column('id', sa.Integer(),primary_key=True),
        sa.Column('content', sa.String(length=200), nullable=False),
        sa.Column('id_user',sa.Integer(), nullable=False)
)



def downgrade() -> None:
     op.drop_table(
        'post'
    )
