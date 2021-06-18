from enum import unique
from app import db

class TradeDocMaster(db.Model):
    __tablename__ = "trade_doc_master"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    unique_id = db.Column(db.String, unique=True, nullable=False)
    file_name = db.Column(db.String, unique=False, nullable=True)
    port_of_loading = db.Column(db.String, unique=True, nullable=True)
    port_of_discharge = db.Column(db.String, unique=True, nullable=True)
    port_of_receipt = db.Column(db.String, unique=True, nullable=True)
    port_of_delivery = db.Column(db.String, unique=True, nullable=True)
    exporter_name = db.Column(db.String, unique=True, nullable=True)
    exporter_location = db.Column(db.String, unique=True, nullable=True)
    consignee_name = db.Column(db.String, unique=True, nullable=True)
    consignee_location = db.Column(db.String, unique=True, nullable=True)
    notify_name = db.Column(db.String, unique=True, nullable=True)
    notify_location = db.Column(db.String, unique=True, nullable=True)
    buyer_name = db.Column(db.String, unique=True, nullable=True)
    buyer_location = db.Column(db.String, unique=True, nullable=True)
    other_locations = db.Column(db.String, unique=True, nullable=True)
    other_org_names = db.Column(db.String, unique=True, nullable=True)
    product = db.Column(db.String, unique=True, nullable=True)
    person = db.Column(db.String, unique=True, nullable=True)
    vessel = db.Column(db.String, unique=True, nullable=True)
    email = db.Column(db.String, unique=True, nullable=True)
