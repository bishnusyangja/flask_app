from flask import request, make_response, jsonify
from sqlalchemy.orm import joinedload

from helpers import get_keywords_from_file
from models import Report
from views import BaseView
from sqlalchemy import desc


class ReportView(BaseView):
    field_items = ('user.name', 'keyword', 'result', )

    def get_queryset(self):
        qs = Report.query.options(joinedload(Report.user)).order_by(desc(Report.id)).all()
        return qs

    def get_count(self):
        print("at count", Report.query.count())
        return Report.query.count()


class UploadFileView(BaseView):

    def post(self):
        from task import load_search_task
        file = request.files.get('file')
        if not file:
            make_response(jsonify(dict(error="Please upload file")), 400)
        keywords = get_keywords_from_file(file)
        for item in keywords:
            if item:
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