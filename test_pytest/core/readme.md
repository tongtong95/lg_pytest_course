1、安装allure-pytest插件，生成测试报告

2、利用allure指定存放路径，执行测试用例
pytest test_pytest/tests/test_calc.py --alluredir=./test_pytest/result

--clean-alluredir：清空执行结果，执行测试用例

3、在测试完成后使用Allure命令查看实际报告，将在默认浏览器中显示生成的报告
allure serve ./test_pytest/result
