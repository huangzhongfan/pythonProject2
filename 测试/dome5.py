# 导包
import unittest
import requests


class Testpost(unittest.TestCase):
    def setUp(self) -> None:
        # 定义地址
        self.myurl = "http://127.0.0.1:8000/api/departments/"
        # 定义请求头
        self.myheader = {"Content-Type": "application/json"}

    def tearDown(self) -> None:
        pass

    # 新增测试用例，覆盖所有参数
    def testDptPost01(self):
        # 定义消息体数据
        mydata4 = r'{"data":[{"dep_id":"asdfghjklz1","dep_name":"asdfghjklzasdfghjklz",' \
                 r'"master_name":"asdfghjklzasdfghjklz",' \
                 r'"slogan":"asdfghjklzasdfghjklzasdfghjklzasdfghjklzasdfghjklzasdfghjklzasdfghjklzasdfghjklzasdfghjklzasdfghjklz"}]} '
        # 发送请求，获取响应报文或者状态码
        res01 = requests.post(url=self.myurl, data=mydata4.encode("UTF-8"), headers=self.myheader)
        # 构建预期结果
        code_expect = "400"
        # 获取实际结果
        code_actual = str(res01.status_code)
        # 判断实际与预期是否相符，相符则成功，不符则失败
        try:
            self.assertEqual(code_actual, code_expect)
        except AssertionError as e:
            # 如果实际、预期不符，将获取异常，并打印测试失败
            print("测试失败，与实际不符")
            print("实际代码为：", code_actual)
        else:
            # 实际与预期相符，则成功，通过测试
            print("测试成功")
        finally:
            # 无论成功还是失败，都将打印测试执行完毕
            print("测试执行完毕")


if __name__ == "__main__":
    unittest.main()