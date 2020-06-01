from flask import request, make_response, jsonify
from models import Report
from views import BaseView


class ReportView(BaseView):
    field_items = ('user.name', 'user.username', 'score', )

    def get_queryset(self):
        qs= Report.query.all()
        return qs


class UploadFileView(BaseView):

    def post(self):
        file = request.FILES.get('file')
        resp = {}
        response = make_response(jsonify(resp), 200)
        return response


def report_view():
    obj = ReportView(request)
    return obj.get_response()


def upload_file_view():
    obj = UploadFileView(request)
    return obj.get_response()