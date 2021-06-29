from django.shortcuts import render, redirect, HttpResponse
from .py import generations, Constants

def index(request):
    return render(request, 'index.html')
# Create your views here.

def process(request):
    try:
        post = request.POST 
    except:
        return redirect('')
    names, locs = [], []
    if post['series'] == 'ALL':
        for x in Constants.char_by_series:
            names += Constants.char_by_series[x]
            locs += Constants.loc_by_series[x]
    elif post['series'] == 'OLD':
        for x in ['TOS', 'TNG', 'DS9', 'VOY']:
            names += Constants.char_by_series[x]
            locs += Constants.loc_by_series[x]
    elif post['series'] == 'NEW':
        for x in ['ENT', 'DSC', 'PIC', 'LD']:
            names += Constants.char_by_series[x]
            locs += Constants.loc_by_series[x]
    else: 
        names = Constants.char_by_series[post['series']]
        locs = Constants.loc_by_series[post['series']]
    a, b = generations.inputs(
        post.get('names', False),
        post.get('locations', False),
        post.get('settings', ''),
        names, locs)
    result = generations.generate(a, b,
                                    post['series'],
                                    post['length'])
    return HttpResponse(result)
   