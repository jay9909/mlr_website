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
    team_records = Team.query.all()

    return render_template('teams.html', teams=team_records)


@index_bp.route('/team/<team_abbr>', methods=['GET'])
def team(team_abbr):
    team_rec = Team.query.filter(
        Team.abb == team_abbr.upper()
    ).first()

    if team_rec is None:
        raise Exception("Team could not be fetched")

    return render_template(
        'team.html',
        title="Major League Redditball: Fake Baseball, Real Community",
        team=team_rec
    )
