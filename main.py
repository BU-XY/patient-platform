import pandas as pd
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


def put():
    parser = reqparse.RequestParser()
    parser.add_argument('accessor_userId')
    parser.add_argument('accessor_access')
    parser.add_argument('data_userId')
    parser.add_argument('temp')
    parser.add_argument('pressure')
    parser.add_argument('pulse')
    parser.add_argument('oximeter')
    parser.add_argument('weight')
    parser.add_argument('glucometer')
    args = parser.parse_args()
    data = pd.read_csv('users.csv')

    if args['accessor_access'] != 'patient' or args['accessor_userId'] != args['data_userId']:
        return {'message': "Access denied."}, 401

    if int(args['data_userId']) in list(data['userId']):
        old_data = data.loc[int(args['data_userId']) - 1]
        new_data = pd.DataFrame({
            'userId': [old_data['userId']],
            'access': [old_data['access']],
            'name': [old_data['name']],
            'role': [old_data['role']],
            'temperature': [args['temp']],
            'blood_pressure': [args['pressure']],
            'pulse': [args['pulse']],
            'oximeter': [args['oximeter']],
            'weight': [args['weight']],
            'glucometer': [args['glucometer']]
        })
        data.loc[int(args['data_userId']) - 1] = list(new_data.loc[0])
        data.to_csv('users.csv')

        return {'data': data.to_dict()}, 200

    else:
        return {'message': "User ID does not exist."}, 409


def get():
    parser = reqparse.RequestParser()
    parser.add_argument('accessor_userId')
    parser.add_argument('data_userId')
    parser.add_argument('accessor_access')
    args = parser.parse_args()

    if args['accessor_access'] == 'admin' or args['accessor_userId'] != args['data_userId']:
        return {'message': "Access denied."}, 401
    else:
        data = pd.read_csv('users.csv')
        data = data.to_dict()
        return {'data': data}, 200


class Patients(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('userId')
        parser.add_argument('access')
        parser.add_argument('new_userId')
        parser.add_argument('new_name')
        parser.add_argument('new_access')
        parser.add_argument('new_role')

        args = parser.parse_args()
        data = pd.read_csv('users.csv')

        if args['access'] != 'admin':
            return {
                       'message': "Access denied."
                   }, 401
        elif args['new_name'] in list(data['name']) or args['new_userId'] in list(data['userId']):
            return {'message': "Name or User ID already exists."}, 409
        else:
            new_data = pd.DataFrame({
                'userId': [args['new_userId']],
                'access': [args['new_access']],
                'name': [args['new_name']],
                'role': [args['new_role']],
                'temperature': ['none'],
                'blood_pressure': ['none'],
                'pulse': ['none'],
                'oximeter': ['none'],
                'weight': ['none'],
                'glucometer': ['none']
            })
            data = data.append(new_data)
            data.to_csv('users.csv')
            return {'data': data.to_dict()}, 200


api.add_resource(Patients, '/patients')

if __name__ == '__main__':
    app.run()
