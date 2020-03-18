from flask import (
    request, jsonify, redirect, Blueprint
)
from werkzeug.exceptions import HTTPException
from typing import List
from hashlib import blake2b
from models import SQLHelper


link_bp = Blueprint(
    'link_bp', __name__, url_prefix='/link', template_folder='templates'
)


class MissingFieldsException(HTTPException):
    def __init__(self, missing_fields: List[str], message_template='{field} is missing'):
        self.missing_fields = missing_fields
        missing_fields_text = ', '.join(missing_fields)
        exception_message = message_template.replace('{field}', missing_fields_text)
        super().__init__(exception_message)


@link_bp.app_errorhandler(MissingFieldsException)
def handle_missing_fields(e: MissingFieldsException):
    return jsonify({
        'message': e.message
    }), 400


@link_bp.app_errorhandler(404)
def page_not_found(error):
    return jsonify(message="not found"), 404


@link_bp.route('/400check')
def check_error_400():
    raise MissingFieldsException(['field1', 'field2'])


@link_bp.route('/', methods=['POST'])
def shorten_url():
    origin_url = request.form['origin_url']
    h = blake2b(digest_size=3)
    h.update(bytes(origin_url, encoding='utf-8'))
    shortend_url = h.hexdigest()
    try:
        add_url = "INSERT INTO urls (origin_url, shortend_url, visit_cnt) VALUES (%s, %s, %s)"
        SQLHelper.add_one(add_url, (origin_url, shortend_url, 0))
        return jsonify(shortend_url=f'{request.url}{shortend_url}')
    except Exception as e:
        return jsonify(message="the url is already shortened")


@link_bp.route('/<link_name>', methods=['GET', 'DELETE'])
def check_link(link_name):
    if request.method == 'GET':
        sql = "UPDATE urls SET visit_cnt = visit_cnt + 1 WHERE shortend_url = %s"
        SQLHelper.update_one(sql, link_name)
        sql = "SELECT * FROM urls WHERE shortend_url = %s"
        selected = SQLHelper.fetch_one(sql, link_name)[1]
        return redirect(selected)
    elif request.method == 'DELETE':
        sql = "DELETE FROM urls WHERE shortend_url = %s"
        SQLHelper.delete_one(sql, link_name)
        return '', 204


@link_bp.route('/<link_name>/status', methods=['GET'])
def status(link_name):
    sql = "SELECT * FROM urls WHERE shortend_url = %s"
    selected = SQLHelper.fetch_one(sql, link_name)[3]
    return jsonify(visit_count=selected)
