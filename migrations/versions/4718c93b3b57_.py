"""empty message

Revision ID: 4718c93b3b57
Revises: 007e594469bb
Create Date: 2024-03-21 16:39:10.156593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4718c93b3b57'
down_revision = '007e594469bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fav', schema=None) as batch_op:
        batch_op.add_column(sa.Column('character_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('planets_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'planets', ['planets_id'], ['id'])
        batch_op.create_foreign_key(None, 'character', ['character_id'], ['id'])
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])

    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.drop_constraint('planets_characters_fkey', type_='foreignkey')
        batch_op.drop_column('characters')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('characters', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('planets_characters_fkey', 'character', ['characters'], ['id'])

    with op.batch_alter_table('fav', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('planets_id')
        batch_op.drop_column('character_id')

    # ### end Alembic commands ###
