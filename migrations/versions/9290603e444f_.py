"""empty message

Revision ID: 9290603e444f
Revises: 
Create Date: 2021-06-30 12:36:10.027935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9290603e444f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('salary', sa.Float(), nullable=True),
    sa.Column('position', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    # ### end Alembic commands ###