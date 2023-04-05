# import os
# import requests

# from typing import Any, Text, Dict, List
# from dotenv import load_dotenv
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher

# load_dotenv()


# class ActionProductDescriptionGenerator(Action):

#     def name(self) -> Text:
#         return "action_product_description"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         PRODUCT_DESCRIPTION_ENDPOINT = os.getenv(
#             'PRODUCT_DESCRIPTION_ENDPOINT')
#         UC_X_API_KEY = os.getenv('UC-X-API-KEY')

#         headers = {
#             'accept': 'application/json',
#             'UC-X-API-KEY': UC_X_API_KEY,
#         }

#         json_data = {
#             'keywords': [
#                 'ucraft',
#                 'website builder',
#                 'ecommerce'
#             ],
#             'content_type': 'description_highlight',
#             'count': 1
#         }

#         response = requests.post(PRODUCT_DESCRIPTION_ENDPOINT,
#                                  headers=headers, json=json_data)

#         generated_text = '\n'.join(response.json())
#         dispatcher.utter_message(text=generated_text)

#         return []




from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from googlesearch import search

class ActionGoogleSearch(Action):

    def name(self) -> Text:
        return "action_google_search"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # get the search query from the user input
        search_query = tracker.latest_message['text']

        # perform the google search and get the top 5 results
        search_results = search(search_query, num_results=5)

        # create a response message with the search results
        response = f"Here are the top 5 results for {search_query}: \n"
        for result in search_results:
            response += f"\n {result}"

        # send the response message to the user
        dispatcher.utter_message(text=response)

        return []
