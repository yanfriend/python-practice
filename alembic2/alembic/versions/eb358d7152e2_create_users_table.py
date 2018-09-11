"""Create users table

Revision ID: eb358d7152e2
Revises: 
Create Date: 2016-10-20 17:03:17.653776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb358d7152e2'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('chosen_decimal', sa.Numeric(16,8), nullable=False),
        sa.Column('dob', sa.DateTime, nullable=False),
    )

def downgrade():
    op.drop_table('users')
