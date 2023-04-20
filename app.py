from . import app, db
from flask import request
import click
from .ingestion import ingest_wx_data, generate_stats
from flask import jsonify
from .models import Weather, Stats

@app.route("/weather/", methods=["GET"])
def weather():
    """
    This is Weather endpoint.
    ---
    parameters:
      - name: page
        in: query
        type: int
        required: false
        description: The ID of the resource to retrieve.
      - name: date
        in: query
        type: string
        required: false
        description: The ID of the resource to retrieve.
      - name: station
        in: query
        type: string
        required: false
        description: The ID of the resource to retrieve.
    responses:
      200:
        description: OK
    """
    page = request.args.get("page", type=int)
    date = request.args.get("date")
    station = request.args.get("station")
    result = Weather.query
    if date:
        result = result.filter(Weather.date == date)
    if station:
        result = result.filter(Weather.station == station)
    result = result.paginate(page=page, per_page=100).items
    return jsonify([r.serialize for r in result])

@app.route("/weather/stats", methods=["GET"])
def stats():
    """
    This is Weather Stats endpoint.
    ---
    parameters:
      - name: page
        in: query
        type: int
        required: false
        description: The ID of the resource to retrieve.
      - name: date
        in: query
        type: string
        required: false
        description: The ID of the resource to retrieve.
      - name: station
        in: query
        type: string
        required: false
        description: The ID of the resource to retrieve.
    responses:
      200:
        description: OK
    """
    page = request.args.get("page", type=int)
    date = request.args.get("date")
    station = request.args.get("station")
    result = Stats.query
    if date:
        result = result.filter(Stats.date == date)
    if station:
        result = result.filter(Stats.station == station)
    result = result.paginate(page=page, per_page=100).items
    return jsonify([r.serialize for r in result])

@click.command(name="create")
def create():
    with app.app_context():
        db.drop_all()
        db.create_all()
        ingest_wx_data()
        generate_stats()

app.cli.add_command(create)