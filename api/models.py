from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, UniqueConstraint, ForeignKey
from flask_migrate import Migrate

metadata = MetaData(naming_convention={
    'fk':'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'
})

db = SQLAlchemy(metadata=metadata)