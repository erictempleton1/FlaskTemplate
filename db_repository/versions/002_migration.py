from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user_location = Table('user_location', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('city', String),
    Column('state', String(length=2)),
    Column('country', String),
    Column('user_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String),
    Column('email', String),
    Column('nickname', String),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user_location'].create()
    post_meta.tables['user'].columns['nickname'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user_location'].drop()
    post_meta.tables['user'].columns['nickname'].drop()
