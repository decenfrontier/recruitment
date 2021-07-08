from django.http import HttpResponse
from django.template import loader

from jobs.models import Job

def joblist(request):
    job_list = Job.objects.order_by('type')
    template = loader.get_template('joblist.html')
    context = {'job_list': job_list}

    for job in job_list:
        job.city = Job.Cities[job.city][1]
        job.type = Job.Types[job.type][1]

    return HttpResponse(template.render(context))