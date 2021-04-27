# 导包
import unittest
import HTMLTestRunnerNew
import time

su = unittest.TestSuite()

# 搜索测试用例
findTests = unittest.defaultTestLoader.discover("./", pattern="dome6.py")
# 添加测试用例
su.addTest(findTests)
report_dir = './Reoprts/'
noe_time = time.strftime('%Y_%m_%d_%H_%M_%S')
fliename1 = "_testReport.HTML"
filename = report_dir + noe_time + fliename1
with open(filename, mode="wb",) as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="学生信息管理系统接口测试报告",
                                              description="对学术系统进行接口测试",
                                              tester="Gl"
                                              )
    runner.run(su)
