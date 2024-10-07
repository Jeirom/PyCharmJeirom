# from http.client import responses
# import logging
# import requests
#
#
# logging.getLogger("news")
#
#
# from news_prog.src.config import BASE_url, API_KEY
# import datetime
#
# date_now = datetime.datetime.now()
#
#
# def news_today(quers, ignore, api_key=API_KEY):
#     date_now = datetime.datetime.now()
#     params = {
#         "q": quers,
#         #'from': date_now.strftime('%Y-%m-%d'),
#         "sortBy": "publishedAt",
#         "apiKey": api_key,
#     }
#
#     try:
#         response = requests.get(
#             url=BASE_url,
#             params=params,
#         )
#         news_today = response.json()
#
#         if news_today["status"] != "ok":
#             return []
#         result_articles = news_today.get("articles", [])
#         list_articles = []
#
#         for article in result_articles:
#
#             content = f'{article.get("title")} {article.get("content")}'.lower()
#             flag = False
#
#             for word in ignore:
#                 if word.lower in content:
#                     flag = True
#
#             if flag:
#                 continue
#
#             list_articles.append(
#                 {
#                     "title": article.get("title"),
#                     "author": article.get("author"),
#                     "description": article.get("content"),
#                     "url": article.get("url"),
#                 }
#             )
#
#     except Exception:
#         return []
