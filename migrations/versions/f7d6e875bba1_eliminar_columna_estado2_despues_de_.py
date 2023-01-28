"""eliminar columna estado2 despues de grabar datos

Revision ID: f7d6e875bba1
Revises: e382d5cae94e
Create Date: 2023-01-27 11:12:05.694819

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7d6e875bba1'
down_revision = 'e382d5cae94e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'estado2')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('estado2', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###