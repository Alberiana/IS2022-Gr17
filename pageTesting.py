import unittest
import HtmlTestRunner
import pagePenetration as pen
import webbrowser
import os
import time
from ddt import ddt, data, unpack


def get_html_file():
    #Ne array vendosen te gjitha direktoriumet qe gjenden ne OS
    arr = os.listdir()  
    #Iterimi i x-it neper array te shenuar si arr
    for x in arr:  
        #Kushti qe ti ktheje vetem files qe jane html
        if '.html' in x:  
            return x


#Funksioni teston te gjithe path-at
def get_tests(path):
    tuples = []
    f = open(path, "r")  
    for x in f: 
        x = x.split(' ')  
        tuples.append((x[0], x[1]))  
    #Mbyllet fajlli
    f.close()
    #Kthen tuples  
    return tuples  

#Funksioni e kthen vleren hyrese nga string "True"/"False" ne variabel booleane True/False(1/0)
def convert_to_bool(str):  
    if str == "True":
        return True
    return False

#Inicializimi i variables testing_data me tuples qe kthehen nga funksioni get_tests
testing_data = get_tests('pages.txt')  

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
