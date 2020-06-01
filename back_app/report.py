from flask import request, make_response, jsonify
from sqlalchemy.orm import joinedload

from helpers import get_keywords_from_file
from models import Report
from task import load_search_task
from views import BaseView


class ReportView(BaseView):
    field_items = ('user.name', 'keyword', 'results', )

    def get_queryset(self):
        qs = Report.query.options(joinedload(Report.user)).all()
        return qs


class UploadFileView(BaseView):

    def post(self):
        file = request.files.get('file')
        keywords = get_keywords_from_file(file)
        for item in keywords:
            load_search_task.delay(item, self.user.id)
        resp = {"success": "success"}
        response = make_response(jsonify(resp), 200)
        return response


def report_view():
    obj = ReportView(request)
    return obj.get_response()


def upload_file_view():
    obj = UploadFileView(request)
    return obj.get_response()