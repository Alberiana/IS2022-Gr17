import unittest
import HtmlTestRunner
import pagePenetration as pen
import webbrowser
import os
import time
from ddt import ddt, data, unpack


def get_html_file():
    arr = os.listdir()  # ne array po i vendos te gjitha direktoriumet qe gjenden ne OS
    for x in arr:  # po iteron neper array
        if '.html' in x:  # kushti qe ti ktheje vetem files qe jane html
            return x


#funksioni teston te gjithe path-at
def get_tests(path):
    tuples = []
    f = open(path, "r")  
    for x in f: 
        x = x.split(' ')  
        tuples.append((x[0], x[1]))  

    f.close()  # e mbyll file
    return tuples  # e kthen tuple

#funksioni e kthen nga string "True"/"False" ne variabel booleane True/False
def convert_to_bool(str):  
    if str == "True":
        return True
    return False


testing_data = get_tests('pages.txt')  # kemi inicializuar variablen testing_data me tuple qe kthehet nga funksioni get_tests


@ddt
class TestName(unittest.TestCase):

    @data(*testing_data)
    @unpack
    def test_website(self, website_url, is_vulnerable):
        self.assertEqual(pen.scan_sql_injection(website_url), convert_to_bool(is_vulnerable))


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='.'))
    filename = 'file:///' + os.getcwd() + '/' + 'TestResults___main__.TestName_2022-01-8_15-42-33'  
    webbrowser.open_new_tab(filename)
