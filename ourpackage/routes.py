from ourpackage import *
from ourpackage.models import *
from flask import render_template, jsonify, json



@app.route('/team/')
def user_index():
    all_teams = db.session.query(Team).all()
    all_teams_dicts = [team.to_dict() for team in all_teams]
    return jsonify(all_teams_dicts)
