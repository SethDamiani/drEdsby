import random, re
import time
from collections import OrderedDict
from dateutil.parser import parse

from copy import deepcopy

import bleach
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from jinja2 import Environment, environment

from webapp.edsby_functions import EdsbyAccess


# Create your views here.
def index(request):
    for i in range(0, 10):
        try:
            edsby = EdsbyAccess()
            break
        except:
            if i == 9:
                return HttpResponseNotFound('<h1>Page not found</h1>')
            pass
    class_list = edsby.getCurrentClasses()
    class_feeds = {}
    # class_list = edsby.getCurrentClasses()
    class_colors = {}
    colors = ['red', 'pink', 'purple', 'deep-purple', 'indigo', 'blue', 'light-blue', 'cyan', 'teal', 'green',
              'light-green darken-2', 'lime darken-2', 'yellow darken-3', 'amber', 'orange', 'deep-orange', 'brown']
    temp_classes = deepcopy(class_list)
    # for key, value in temp_classes.items():
    #     class_feeds[key] = edsby.getClassFeed(key)
    #     if not isinstance(class_feeds[key], str):
    #         # print(class_feeds[key].keys())
    #         # print(class_feeds[key]['slices'][0]['data']['item'])
    #         class_feeds[key] = class_feeds[key]['slices'][0]['data']['item']
    #         # class_feeds[key] = OrderedDict(sorted(class_feeds[key].items(), key=lambda x: class_feeds[x]['footer'][
    #         #     'date']))
    #         # if 'slices' in class_feeds[key].keys():
    #         #     print('slices exists')
    #         #     print(str(key) + str(class_feeds[key].slices))
    #
    #     else:
    #         del class_feeds[key]
    #     class_colors[key] = random.choice(colors)
    #     colors.remove(class_colors[key])
    activity = edsby.getBaseActivity()['slices'][0]['data']['messages']['item']
    activity_colors = {}
    temp_activity = deepcopy(activity)
    all_classes = edsby.getAllClasses()
    schedule = edsby.getSchedule()
    temp_schedule = deepcopy(schedule)
    schedule_re = re.compile('^r\d$')
    for key, values in temp_activity.items():
        if isinstance(activity[key], str):
            del activity[key]
        activity_colors[key] = random.choice(colors)
        if not 'place' in values['right']['normal']['name'] and values['pnid'] in all_classes.keys():
            if 'human_name' in all_classes[activity[key]['pnid']]:
                activity[key]['right']['normal']['name']['place'] = all_classes[values['pnid']]['human_name']
        if 'filesPrep' in values.keys():
            for idx, val in enumerate(values['filesPrep']['init']['files']):
                activity[key]['filesPrep']['init']['files'][idx]['downloadURL'] = edsby.getAttachmentDownloadURL(
                    values['pnid'], values['nid'], values['rid'], val['nid'])
        activity[key]['left']['profpicURL'] = edsby.getProfilePic(values['left']['profpic'], 50)
    for key, values in temp_schedule.items():
        if not schedule_re.match(key):
            del schedule[key]
    activity_sorted = OrderedDict(sorted(activity.items(), key=lambda item: parse(item[1]['right']['footer']['date']),
                                         reverse=True))
    schedule_sorted = OrderedDict(sorted(schedule.items(), key=lambda item: parse(item[1]['sdate'])))
    # print(class_feeds)
    scrolling_news = edsby.getScrollingNews()
    # print(scrolling_news)
    temp_feeds = deepcopy(class_feeds)
    # for key, values in temp_feeds.items():
    #     try:
    #         values['slices'][0]
    #     except:
    #         class_feeds.pop(key, None)
    # print('new' + str(type(class_list)))
    # print('feeds: ' + str(class_feeds))
    to_pass = {'classes': class_list, 'feeds': class_feeds, 'colors': activity_colors, 'news': scrolling_news,
               'activity': activity_sorted, 'schedule': schedule_sorted}

    # def debug(text):
    #     print
    #     text
    #     return ''
    #
    # environment.filters['debug'] = debug
    return render(request, "webapp/index.jinja.html", to_pass)


def format_datetime(value, format='medium'):
    if format == 'full':
        format = "EEEE, d. MMMM y 'at' HH:mm"
    elif format == 'medium':
        format = "EE dd.MM.y HH:mm"
    return babel.dates.format_datetime(value, format)
