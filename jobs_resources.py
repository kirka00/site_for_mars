from flask_restful import Resource
from data import db_session
from flask import jsonify
from data.jobs import Jobs
from parser_file import parser


class JobssResource(Resource):
    def get(self, job_id):
        session = db_session.create_session()
        job = session.query(Jobs).all()
        return jsonify({'job': [item.to_dict(
            only=('team_leader', 'job', 'work_size',
                  'collaborators', 'is_finished')) for item in job]})

    def add_job(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        job = session.query(Jobs).all()
        return jsonify({'job': [item.to_dict(
            only=('team_leader', 'job', 'work_size',
                  'collaborators', 'is_finished')) for item in job]})

    def add_job(self):
        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            is_finished=args['is_finished']

        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})
