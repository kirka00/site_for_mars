from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from flask import jsonify
from data.users import User
from data.jobs import Jobs
from parser import parser

class UsersResource (Resource):
    def get(self):
        session = db_session.create_session()
        user = session.query(Jobs).all()
        return jsonify({'user': [item.to_dict(
            only=('title', 'content', 'user.name')) for item in user]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            is_published=args['is_published'],
            is_private=args['is_private']
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersResource (Resource):
    def get(self):
        session = db_session.create_session()
        user = session.query(Jobs).all()
        return jsonify({'user': [item.to_dict(
            only=('title', 'content', 'user.name')) for item in user]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            is_published=args['is_published'],
            is_private=args['is_private']
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})