from flask import Blueprint, render_template
from flask import current_app as app
from web.models.team import Team


# Blueprint Configuration
index_bp = Blueprint(
    'index_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@index_bp.route('/', methods=['GET'])
def index():
    team = Team.query.filter(
        Team.abb == 'oak'.upper()
    ).first()

    if team is None:
        raise Exception("Team could not be fetched")

    return render_template(
        'index.html',
        title="Major League Redditball: Fake Baseball, Real Community",
        team=team
    )
