from enum import unique
import os
from uuid import uuid1
from flask import Blueprint, render_template
from jinja2 import TemplateNotFound
from werkzeug.exceptions import abort

from app import db, app, logging
from .models import TradeDocMaster

logger = logging.getLogger(__name__)

blueprint_aml = Blueprint("aml", __name__, template_folder="templates", static_folder="static", static_url_path="/static")

@blueprint_aml.route("/", methods=["GET"])
def index():
    try:
        return render_template("index.html")
    except TemplateNotFound:
        return abort(404)

@blueprint_aml.route("/network_files", methods=["GET"])
def network_files():
    try:
        folder_path = os.path.join(os.getcwd(), "shared")
        files = os.listdir(folder_path)
        unique_ids = [str(uuid1().int) for _ in files]

        db.create_all()
        db.session.add_all([TradeDocMaster(unique_id=i, file_name=file) for i, file in zip(unique_ids, files)])
        db.session.commit()

        return render_template("network_files.html", folder_path=folder_path, data=zip(unique_ids, files))
    except TemplateNotFound:
        return abort(404)

@blueprint_aml.route("/show_extraction/<unique_id>", methods=["GET"])
def show_extraction(unique_id):
    try:
        if unique_id:
            return render_template("show_extraction.html", unique_id=unique_id)
    except TemplateNotFound:
        return abort(404)