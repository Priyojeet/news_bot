from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core_sdk import Action
import requests
from rasa_core_sdk.events import SlotSet
import json


class ActionGetNewst(Action):

    def name(self):
        return 'action_get_news'

    def run(self, dispatcher, tracker, domain):
        category = tracker.get_slot('category')
        print(category)
        url = 'https://api.nytimes.com/svc/news/v3/content/all/{category}.json'.format(category=category)
        params = {'api-key': "your api key", 'limit': 5}
        response = requests.get(url, params).text
        json_data = json.loads(response)['results']
        i = 0
        for results in json_data:
            i = i+1
            message = str(i) + "." + results['abstract']
            dispatcher.utter_message(message)
        return[]
