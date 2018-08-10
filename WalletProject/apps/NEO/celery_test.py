from django.http import HttpResponse

from celery_tasks.tasks import add


def celerytest():

    result = add.delay(4,6)
    print("ok")
    return HttpResponse(result)

