from web import db
from web.models.range import BattingRange, PitchingRange, HandBonus
from web.models.team import Team


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
    batType = db.Column(db.VARCHAR(6))
    pitchType = db.Column(db.VARCHAR(6))
    pitchBonus = db.Column(db.VARCHAR(6))
    hand = db.Column(db.VARCHAR(6))
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
    FormatNum = db.Column('Format#', db.Integer())
    Status = db.Column(db.Integer())
    discordID = db.Column(db.Integer())

    def get_batting_ranges(self):
        bat_type = self.batType
        batting_ranges = BattingRange.query.filter(
            BattingRange.type == bat_type
        ).first()

        if batting_ranges is None:
            raise Exception("Player's batting ranges could not be fetched.")

        return [
            batting_ranges.rangeHR,
            batting_ranges.range3B,
            batting_ranges.range2B,
            batting_ranges.range1B,
            batting_ranges.rangeBB,
            batting_ranges.rangeFO,
            batting_ranges.rangeK,
            batting_ranges.rangePO,
            batting_ranges.rangeRGO,
            batting_ranges.rangeLGO
        ]

    def get_pitching_ranges(self):
        pitch_type = self.pitchType
        if pitch_type is None:
            return None

        pitching_ranges = PitchingRange.query.filter(
            PitchingRange.type == pitch_type
        ).first()

        if pitching_ranges is None:
            raise Exception("Player's pitching ranges could not be fetched.")

        hand_bonuses = self.get_hand_bonuses()

        combined_ranges = ([
                               pitching_ranges.rangeHR,
                               pitching_ranges.range3B,
                               pitching_ranges.range2B,
                               pitching_ranges.range1B,
                               pitching_ranges.rangeBB,
                               pitching_ranges.rangeFO,
                               pitching_ranges.rangeK,
                               pitching_ranges.rangePO,
                               pitching_ranges.rangeRGO,
                               pitching_ranges.rangeLGO
                           ],
                           [
                               pitching_ranges.rangeHR + hand_bonuses[0],
                               pitching_ranges.range3B + hand_bonuses[1],
                               pitching_ranges.range2B + hand_bonuses[2],
                               pitching_ranges.range1B + hand_bonuses[3],
                               pitching_ranges.rangeBB + hand_bonuses[4],
                               pitching_ranges.rangeFO + hand_bonuses[5],
                               pitching_ranges.rangeK + hand_bonuses[6],
                               pitching_ranges.rangePO + hand_bonuses[7],
                               pitching_ranges.rangeRGO + hand_bonuses[8],
                               pitching_ranges.rangeLGO + hand_bonuses[9]
                           ])

        return combined_ranges

    def get_hand_bonuses(self):
        hand_bonus = self.pitchBonus
        if hand_bonus is None:
            return None

        hand_bonuses = HandBonus.query.filter(
            HandBonus.type == hand_bonus
        ).first()

        if hand_bonuses is None:
            raise Exception("Player's hand bonuses could not be fetched.")

        return [
            hand_bonuses.rangeHR,
            hand_bonuses.range3B,
            hand_bonuses.range2B,
            hand_bonuses.range1B,
            hand_bonuses.rangeBB,
            hand_bonuses.rangeFO,
            hand_bonuses.rangeK,
            hand_bonuses.rangePO,
            hand_bonuses.rangeRGO,
            hand_bonuses.rangeLGO
        ]

    def get_team(self):
        if self.team is None:
            return None

        team_rec = Team.query.filter(
            Team.abb == self.team.upper()
        ).first()

        if team_rec is None:
            raise Exception(f"Player's team could not be fetched")

        return team_rec
