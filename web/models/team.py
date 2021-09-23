from web import db


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

    roster = db.relationship('Player', backref='team_ref', lazy=True)
