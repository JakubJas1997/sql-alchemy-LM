from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:qwerty@localhost:3306/champ_league")

Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)


class GroupTable(Base):
    __tablename__ = "Group_H"
    team_id = (Column(Integer, primary_key=True, autoincrement=True))
    team_name = (Column(String(50), nullable=False))
    team_country = (Column(String(50), nullable=False))
    points = (Column(Integer, default=0))

    def __repr__(self):
        return f"Team {self.team_name} from {self.team_country} with {self.points} points."

Base.metadata.create_all()
