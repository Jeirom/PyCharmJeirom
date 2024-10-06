# # from time import strftime
# #
# # from dulwich.objectspec import parse_ref
# from win32ctypes.pywin32.pywintypes import datetime
# import datetime
# from news_prog.src.news import news_today
# from news_prog.src.file_to_save import save_file
#
#
# def main():
#     quers = "Russia"
#     article = news_today(quers, "twitter")
#     date_today = datetime.datetime.today()
#     date_str = date_today.strftime("%Y-%m-%d")
#     file_name = f'{date_str}_{quers.replace(" ", "_")}.json'
#     file_path = f"\news{file_name}"
#     save_file(article, file_path)
#
#
# if __name__ == "__main__":
#     main()
