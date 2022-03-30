from flask_restful import Resource
from data import db_session
from flask import jsonify
from data.users import User
from parser_file import parser


class UsersResource(Resource):
    def get(self, user_id):
        session = db_session.create_session()
        user = session.query(User).all()
        return jsonify({'user': [item.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address',
                  'email', 'hashed_password')) for item in user]})

    def add_user(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=args['hashed_password']
        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        user = session.query(User).all()
        return jsonify({'user': [item.to_dict(
            only=('surname', 'name', 'age', 'position', 'speciality', 'address',
                  'email', 'hashed_password')) for item in user]})

    def add_user(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email'],
            hashed_password=args['hashed_password']

        )
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})
