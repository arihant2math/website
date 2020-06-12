from flask import (
    Blueprint, render_template
)

bp = Blueprint('home', __name__, url_prefix='/home')


@bp.route('/index')
def register():
    return render_template('home/index.html')
