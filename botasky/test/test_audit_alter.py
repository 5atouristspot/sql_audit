import unittest
import requests
import json



class AlterExample(unittest.TestCase):

    def test_audit_alter_ok(self):
        ok_request = requests.get(url='http://192.168.74.95:3621/api/v1000/audit/alter',
                                  params={'port': '4450', 'database': 'inception_test', 'sql_statment': "alter TABLE user_dept_relation add content_html12 longtext COMMENT 'H5';"})
        print(ok_request.url)
        print(ok_request.status_code)
        text_info = eval(ok_request.text)
        print(text_info)

        self.assertEqual(200, ok_request.status_code)
        self.assertEqual(0, text_info[0]['errlevel'])
        self.assertEqual(0, text_info[1]['errlevel'])


    '''
    def test_audit_alter_port_fail(self):
        fail_request = requests.get(url='http://192.168.74.95:3621/api/v1000/audit/alter',
                                    params={'port': '4451', 'database': 'inception_test', 'sql_statment': "alter TABLE user_dept_relation add content_html6 longtext COMMENT 'H5';"})
        #print(fail_request.url)
        print(fail_request.status_code)

        text_info = eval(json.dumps(fail_request.text))
        print(text_info)

        self.assertEqual(200, fail_request.status_code)
    '''

    '''
    def test_audit_alter_database_fail(self):
        fail_request = requests.get(url='http://192.168.74.95:3621/api/v1000/audit/alter',
                                    params={'port': '4450', 'database': 'inception_test1', 'sql_statment': "alter TABLE user_dept_relation add content_html6 longtext COMMENT 'H5';"})
        #print(fail_request.url)
        print(fail_request.status_code)

        text_info = eval(json.dumps(fail_request.text))
        print(text_info)

        self.assertEqual(200, fail_request.status_code)
    '''
    '''
    def test_audit_alter_sql_statment_fail(self):
        fail_request = requests.get(url='http://192.168.74.95:3621/api/v1000/audit/alter',
                                    params={'port': '4450', 'database': 'inception_test', 'sql_statment': "alter TABLExxxx user_dept_relation add content_html6 longtext COMMENT 'H5';"})
        #print(fail_request.url)
        print(fail_request.status_code)

        text_info = eval(json.dumps(fail_request.text))
        print(text_info)

        self.assertEqual(200, fail_request.status_code)
    '''
if __name__ == '__main__':
    unittest.main()