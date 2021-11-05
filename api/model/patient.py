from sqlalchemy import Column, Integer, String, Text, ForeignKey

from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

mapper_registry = registry()


@mapper_registry.mapped
class Patient:
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
