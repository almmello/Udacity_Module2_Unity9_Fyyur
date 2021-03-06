"""empty message

Revision ID: 28f696c0ef88
Revises: 93f1e0b27a28
Create Date: 2022-06-22 20:44:33.853185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28f696c0ef88'
down_revision = '93f1e0b27a28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.alter_column('Artist', 'genres',
    #           existing_type=sa.VARCHAR(length=120),
    #           nullable=False)
    # ### end Alembic commands ###
    # Forced drop column genres
    op.drop_column('Artist', 'genres')

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###
