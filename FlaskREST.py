#!/usr/bin/env python

import hashlib
import json
import logging
import types
from datetime import datetime
from flask import Flask, Response, abort, redirect, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

SHORT_HASH_LEN_DEFAULT = 4


def make_json_app():
    def make_json_error(ex):
        response = jsonify(message=str(ex))
        response.status_code = (ex.code
                                if isinstance(ex, HTTPException)
                                else 500)
        return response

    for code in default_exceptions.iterkeys():
        app.register_error_handler(code, make_json_error)


class SerializableModel(object):
    def to_dict(self):
        value = {}
        for column in self.__table__.columns:
            attribute = getattr(self, column.name)
            if isinstance(attribute, datetime):
                attribute = str(attribute)
            value[column.name] = attribute
        return value


class Links(db.Model, SerializableModel):
    __tablename__ = 'Links'

    Id = db.Column(db.String, primary_key=True)
    Link = db.Column(db.String)
    ApiKey = db.Column(db.String)
    DateCreated = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, Id, Link, ApiKey):
        self.Id = Id
        self.Link = Link
        self.ApiKey = ApiKey


class Shorten(Resource):
    def post(self):
        api_key = request.values.get('api_key', None)
        link = request.values.get('link', None)

        if api_key in app.config['API_KEY_CSV'].split(','):
            if link:
                new_link = Links.query.filter(Links.Link==link).first()
                if not new_link:
                    short_hash_len = SHORT_HASH_LEN_DEFAULT
                    full_hash = hashlib.sha1(link).hexdigest()

                    while Links.query.filter(Links.Id==full_hash[:short_hash_len]).first():
                        short_hash_len += 1

                    new_link = Links(full_hash[:short_hash_len], link, api_key)
                    db.session.add(new_link)
                    db.session.commit()

                return Response(json.dumps(new_link.to_dict()),
                                status=200,
                                mimetype='application/json')
            abort(400)
        abort(401)


class Goto(Resource):
    def get(self, short_hash):
        redirect_link = Links.query.filter(Links.Id==short_hash).first()
        if redirect_link:
            return redirect(redirect_link.Link, 301)
        abort(404)


if __name__ == "__main__":
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['API_KEY_CSV'] = 'your,keys,here'

    api.add_resource(Shorten, '/shorten')
    api.add_resource(Goto, '/<short_hash>')

    logging.basicConfig(filename='app.log', level=logging.INFO)
    make_json_app()

    app.run(host='0.0.0.0', port=80, debug=True, threaded=False)