from web import db


class BattingRange(db.Model):
    __tablename__ = 'battingTypes'
    __table_args__ = {'extend_existing': True}

    type = db.Column(db.VARCHAR(length=2),
                     primary_key=True,
                     index=True,
                     nullable=False)

    name = db.Column(db.Text,
                     index=False,
                     nullable=False)

    # valid_from = db.Column(db.Date, nullable=False)
    # valid_to = db.Column(db.Date, nullable=False)

    rangeHR = db.Column(db.Integer, nullable=False)
    range3B = db.Column(db.Integer, nullable=False)
    range2B = db.Column(db.Integer, nullable=False)
    range1B = db.Column(db.Integer, nullable=False)
    rangeBB = db.Column(db.Integer, nullable=False)
    rangeFO = db.Column(db.Integer, nullable=False)
    rangeK = db.Column(db.Integer, nullable=False)
    rangePO = db.Column(db.Integer, nullable=False)
    rangeRGO = db.Column(db.Integer, nullable=False)
    rangeLGO = db.Column(db.Integer, nullable=False)


class PitchingRange(db.Model):
    __tablename__ = 'pitchingTypes'
    __table_args__ = {'extend_existing': True}

    type = db.Column(db.VARCHAR(length=2),
                     primary_key=True,
                     index=True,
                     nullable=False)

    name = db.Column(db.Text,
                     index=False,
                     nullable=False)

    # valid_from = db.Column(db.Date, nullable=False)
    # valid_to = db.Column(db.Date, nullable=False)

    rangeHR = db.Column(db.Integer, nullable=False)
    range3B = db.Column(db.Integer, nullable=False)
    range2B = db.Column(db.Integer, nullable=False)
    range1B = db.Column(db.Integer, nullable=False)
    rangeBB = db.Column(db.Integer, nullable=False)
    rangeFO = db.Column(db.Integer, nullable=False)
    rangeK = db.Column(db.Integer, nullable=False)
    rangePO = db.Column(db.Integer, nullable=False)
    rangeRGO = db.Column(db.Integer, nullable=False)
    rangeLGO = db.Column(db.Integer, nullable=False)


class HandBonus(db.Model):
    __tablename__ = 'handBonuses'
    __table_args__ = {'extend_existing': True}

    type = db.Column(db.VARCHAR(length=2),
                     primary_key=True,
                     index=True,
                     nullable=False)

    name = db.Column(db.Text,
                     index=False,
                     nullable=False)

    # valid_from = db.Column(db.Date, nullable=False)
    # valid_to = db.Column(db.Date, nullable=False)

    rangeHR = db.Column(db.Integer, nullable=False)
    range3B = db.Column(db.Integer, nullable=False)
    range2B = db.Column(db.Integer, nullable=False)
    range1B = db.Column(db.Integer, nullable=False)
    rangeBB = db.Column(db.Integer, nullable=False)
    rangeFO = db.Column(db.Integer, nullable=False)
    rangeK = db.Column(db.Integer, nullable=False)
    rangePO = db.Column(db.Integer, nullable=False)
    rangeRGO = db.Column(db.Integer, nullable=False)
    rangeLGO = db.Column(db.Integer, nullable=False)
