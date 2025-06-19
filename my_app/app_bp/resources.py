from flask_restful import Resource, reqparse
from my_app.models import Zametka
from my_app import db

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, required=True, help='Title cannot be blank')
parser.add_argument('content', type=str, requiresd=True, help='Content cannot be blank')

class ZametkaResource(Resource):
    def get(self, zametka_id):
        zametka = Zametka.query.get_or_404(zametka_id)
        return {
            'id': zametka.id,
            'title': zametka.title,
            'content': zametka.content
        }, 200
    
    def put(self, zametka_id):
        args = parser.parse_args()
        zametka = Zametka.query.get_or_404(zametka_id)
        
        if Zametka.query.filter_by(title=args['title']).first() and Zametka.query.filter_by(content=args['content']).first():
            return {'message': 'A zametka with that content already exists'}, 400
        
        zametka.title = args['title']
        zametka.content = args['content']

        db.session.commit()

        return {
            'id': zametka.id,
            'title': zametka.title,
            'content': zametka.content
        }, 200
    
    def delete(self, zametka_id):
        zametka = Zametka.query.get_or_404(zametka_id)
        db.session.delete(zametka)
        db.session.commit()

        return '', 204