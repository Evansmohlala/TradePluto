from flask import Blueprint, render_template
from .signal_engine import get_signals

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def dashboard():

    signals = get_signals()

    return render_template(
        "dashboard.html",
        signals=signals
    )
