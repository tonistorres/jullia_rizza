"""primeira

Revision ID: 41244e6b200b
Revises: 
Create Date: 2023-11-04 08:51:40.598200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '41244e6b200b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

'''
Em nosso exemplo por meio da função upgrade 
estou criando uma tabela do tipo user
'''
def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.Integer(),primary_key=True),
        sa.Column('username', sa.String(length=50), nullable=False),
        sa.Column('password', sa.String(length=10),nullable=False),
        sa.Column('name', sa.String(length=60),nullable=False),
        sa.Column('email', sa.Integer(length=100))
        
    )

'''
Em nosso exemplo por meio da função downgrade estou 
dropando essa tabela
'''
def downgrade() -> None:
    op.drop_table(
        'user'
    )
