from celery import shared_task


@shared_task()
def test(*args, **kwargs):
    print("Test task")
