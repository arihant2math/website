from flask import (
    Blueprint, render_template
)


bp = Blueprint('download', __name__, url_prefix='/download')


@bp.route('/index')
def register():
    return render_template('download/index.html')
