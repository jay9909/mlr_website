from flask import Blueprint, render_template
from ..models.team import Team
from ..models.player import Player


# Blueprint Configuration
index_bp = Blueprint(
    'index_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@index_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@index_bp.route('/teams', methods=['GET'])
def teams():
    team_records = Team.query.order_by(Team.leeg.desc()).all()

    mlr = {'leeg_name': 'Major League Redditball'}
    milr = {'leeg_name': 'Minor League Redditball'}
    leegs = (mlr, milr)

    for team_rec in team_records:
        if team_rec.leeg == 'MLR':
            mlr[team_rec.abb] = team_rec
        else:
            milr[team_rec.abb] = team_rec

    return render_template('teams.html', leegs=leegs, teams=team_records)


@index_bp.route('/team/<team_abbr>', methods=['GET'])
def team(team_abbr):
    team_rec = Team.query.filter(
        Team.abb == team_abbr.upper()
    ).first()

    if team_rec is None:
        raise Exception("Team could not be fetched")

    park = team_rec.get_park()

    return render_template(
        'team.html',
        title="Major League Redditball: Fake Baseball, Real Community",
        team=team_rec,
        park=park
    )


@index_bp.route('/player/<player_id>/<player_name>', methods=['GET'])
@index_bp.route('/player/<player_id>/', methods=['GET'])
def player(player_id, player_name=None):
    player_rec = Player.query.filter(
        Player.playerID == player_id
    ).first()

    if player_rec is None:
        raise Exception("Player could no be fetched")

    return render_template(
        'player.html',
        title=player_rec.playerName,
        player=player_rec)
