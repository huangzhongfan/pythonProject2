import unittest
import requests
import ddt
from 测试.post import datalist


@ddt.ddt()
class Testpost(unittest.TestCase):
    def setUp(self) -> None:
        # 定义地址
        self.myurl = "http://127.0.0.1:8000/api/departments/"
        # 定义请求头
        self.myheader = {"Content-Type": "application/json"}

    def tearDown(self) -> None:
        pass

    @ddt.data(*datalist)
    def testPost01(self, pdata):
        # csv转为python list时，为空的值会转换为一个空对象，不符合我们的预期的空字符串
        # 此时我们进行一个条件判断，如果是空对象，则重新赋值为空字符串
        if pdata['dep_id'] == None:
            pdata['dep_id'] = ''
        if pdata['dep_name'] == None:
            pdata['dep_name'] = ''
        if pdata['master_name'] == None:
            pdata['master_name'] = ''
        if pdata['slogan'] == None:
            pdata['slogan'] = ''
        print("获取到的pdata值为：", pdata)
        print("获取到的dep_id为：", pdata['dep_id'])
        print("获取到的dep_name为：", pdata['dep_name'])
        print("获取到的mastername为：", pdata['master_name'])
        print("获取到的slogan为：", pdata['slogan'])
        print("获取到的预期为：", pdata['预期'])

        mydata = r'{"data":[{"dep_id":"' + \
                 pdata['dep_id'] + \
                 '","dep_name":"' + \
                 pdata['dep_name'] + \
                 '","master_name":"' + \
                 pdata['master_name'] + \
                 '","slogan":"' + \
                 pdata['slogan'] + \
                 '"}]}'
        print(mydata)
        res01 = requests.post(url=self.myurl, data=mydata.encode("UTF-8"), headers=self.myheader)
        # 构建预期结果
        code_expect = str(pdata['预期'])
        # 获取实际结果
        code_actual = str(res01.status_code)
        # 判断实际与预期是否相符，相符则成功，不符则失败
        try:
            self.assertEqual(code_actual, code_expect)
        except AssertionError as e:
            # 如果实际、预期不符，将获取异常，并打印测试失败
            print("测试失败，与实际不符")
            print("实际代码为：", code_actual)
            # 如果有异常，则抛出，这样测试报告中能看到失败后的提示信息
            raise e
        else:
            # 实际与预期相符，则成功，通过测试
            print("测试成功")
        finally:
            # 无论成功还是失败，都将打印测试执行完毕
            print("测试执行完毕")


if __name__ == '__main__':
    unittest.main()
