import re

from flask import Blueprint, render_template

from ..models.team import Team
from ..models.player import Player
from flask import request
from auth_serivce import auth_service as auth
from discord_service import discord
import urllib

# Blueprint Configuration
index_bp = Blueprint(
    'index_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@index_bp.route('/', methods=['GET'])
@auth.get_user()
def index():
    login_url = discord.make_login_url(request.base_url)

    return render_template('index.html', login_url=login_url)


@index_bp.route('/oauth/redirect', methods=['GET'])
def auth_redirect():
    code = request.args['code']
    print(code)

    token = discord.get_access_token(code, request.base_url)
    return token


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


@index_bp.route('/player/<player_reference>/', methods=['GET'])
def player(player_reference):
    # Was the parameter an ID (number)
    id_regex = '[0-9]{1,5}'  # Match a number with 1 to 5 digits
    if re.fullmatch(id_regex, player_reference) is not None:
        # Reference was a numeric ID.  Query by that.
        player_record = Player.query.filter(
            Player.playerID == player_reference
        ).first()
    else:
        # player_reference is a player's name.  Query by that
        player_reference = urllib.parse.unquote_plus(player_reference)
        player_record = Player.query.filter(
            Player.playerName == player_reference
        ).first()

    # We should have a record by now, one way or the other.
    if player_record is None:
        raise Exception("Player could no be fetched.")

    return render_template(
        'player.html',
        title=player_record.playerName,
        player=player_record)
