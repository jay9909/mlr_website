from web import db
from ..models.park import Park

class Team(db.Model):
    """Data model for an MLR Team"""

    __tablename__ = 'teamData'
    __table_args__ = {'extend_existing': True}
    name = db.Column(db.Text,
                     index=True,
                     unique=True,
                     nullable=False)
    abb = db.Column(db.VARCHAR(length=3),
                    primary_key=True,
                    index=True,
                    unique=True,
                    nullable=False)
    color = db.Column(db.Text,
                      index=False,
                      nullable=False)
    logo_url = db.Column(db.Text,
                         index=False,
                         nullable=False)
    webhook_url = db.Column(db.Text,
                            index=False,
                            nullable=False)
    league = db.Column(db.VARCHAR(4),
                     index=True,
                     nullable=False)

    roster = db.relationship('Player', backref='team_ref', lazy=True)

    def get_park(self):
        park = Park.query.filter(
            Park.team == self.abb
        ).first()

        if park is None:
            park = Park.query.filter(
                Park.team == 'NEU'
            ).first()

            if park is None:
                raise Exception(f"Could not fetch park details for team {self.abb} OR neutral park.")

        return park
