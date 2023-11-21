"""follow

Revision ID: f24938036a97
Revises: 55df86962872
Create Date: 2023-11-16 10:25:53.369350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f24938036a97'
down_revision: Union[str, None] = '55df86962872'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'follow',
        sa.Column('id', sa.Integer(),primary_key=True),
        sa.Column('id_user', sa.Integer(), nullable=False),
        sa.Column('id_follower', sa.Integer(),nullable=False),
        
        
    )

def downgrade() -> None:
    op.drop_table(
        'follow'
    )
