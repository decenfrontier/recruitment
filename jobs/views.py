from django.shortcuts import render
from django.http import HttpResponse, Http404
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


def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city = job.Cities[job.city][1]
    except:
        raise Http404('Job does not exist')
    context = {'job': job}
    return render(request, 'job.html', context)