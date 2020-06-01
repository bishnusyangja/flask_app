from celery_app import celery
from celery.utils.log import get_task_logger
from models import db
from google_search import get_results
from models import Report

logger = get_task_logger(__name__)


@celery.task
def load_search_task(keyword, user_id):
    logger.info("searching google")
    count = get_results(keyword)
    Report.objects.create()
    data = dict(user_id=user_id, keyword=keyword, results=count)
    # db.session.expire_all()
    obj = Report(**data)
    db.session.add(obj)
    db.session.commit()
    return True

