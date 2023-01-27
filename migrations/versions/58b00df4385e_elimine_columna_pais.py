"""elimine columna pais

Revision ID: 58b00df4385e
Revises: 651fb9655400
Create Date: 2023-01-27 11:16:14.595048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58b00df4385e'
down_revision = '651fb9655400'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'pais')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usuario', sa.Column('pais', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
