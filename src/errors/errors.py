from flask import jsonify

def handle_400(e):
    return jsonify(e.to_dict()), 400

class InvalidCall(Exception):
    def __init__(self, error):
        super().__init__()
        self.error = error

    def to_dict(self):
        dict_format = {'error': self.error}
        return dict_format
