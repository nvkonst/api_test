from model.jstesttask import JsTestTask
import requests


class API:
    def __init__(self, base_url):
        self.base_url = base_url

    @staticmethod
    def get_instance(dictionary):
        o = JsTestTask()
        for k, v in dictionary.items():
            setattr(o, k, v)
        return o

    @staticmethod
    def check_text_in_list_attributes(l, text):
        for i in l:
            if text in i.name:
                continue
            else:
                return False
        return True

    def get_response(self, endpoint, search=None, sort_field=None):
        req_line = self.base_url + endpoint
        if search is not None:
            req_line = req_line + f"/?search={search}"
        if sort_field is not None:
            if "search" in req_line:
                req_line = req_line + f"&sort_field={sort_field}"
            else:
                req_line = req_line + f"/?sort_field={sort_field}"
        response = requests.get(req_line)
        return response
