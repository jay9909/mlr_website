from web import db


class Park(db.Model):
    __tablename__ = 'parks'
    __table_args__ = {'extend_existing': True}

    team = db.Column(db.VARCHAR(3),
                     primary_key=True,
                     unique=True,
                     index=True,
                     nullable=False)

    parkName = db.Column(db.Text,
                         unique=True,
                         index=False,
                         nullable=False)

    rangeHR = db.Column(db.Float,
                        unique=False,
                        index=False,
                        nullable=False,
                        default=0.0)

    range3B = db.Column(db.Float,
                        unique=False,
                        index=False,
                        nullable=False,
                        default=0.0)

    range2B = db.Column(db.Float,
                        unique=False,
                        index=False,
                        nullable=False,
                        default=0.0)

    range1B = db.Column(db.Float,
                        unique=False,
                        index=False,
                        nullable=False,
                        default=0.0)

    rangeBB = db.Column(db.Float,
                        unique=False,
                        index=False,
                        nullable=False,
                        default=0.0)
