from web import db


class Player(db.Model):
    """Data model for an MLR Team"""

    __tablename__ = 'playerData'
    __table_args__ = {'extend_existing': True}
    playerID = db.Column(db.Integer,
                         primary_key=True,
                         index=True,
                         unique=True,
                         autoincrement=True,
                         nullable=False)
    playerName = db.Column(db.VARCHAR(length=60),
                           index=True,
                           unique=True,
                           nullable=False)
    team = db.Column(db.VARCHAR(3),
                     db.ForeignKey('teamData.abb'),
                     index=True,
                     nullable=True)
    batType = db.Column(db.Text)
    pitchType = db.Column(db.Text)
    pitchBonus = db.Column(db.Text)
    hand = db.Column(db.Text)
    priPos = db.Column(db.Text)
    secPos = db.Column(db.Text)
    tertPos = db.Column(db.Text)
    redditName = db.Column(db.Text,
                           unique=True,
                           index=True,
                           nullable=False)
    discordName = db.Column(db.Text,
                            unique=True,
                            nullable=True,
                            index=True)
    FormatNum = db.Column(db.Integer())
    Status = db.Column(db.Integer())
    discordID = db.Column(db.Integer())
