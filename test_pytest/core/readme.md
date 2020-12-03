##allure
1、安装allure-pytest插件，生成测试报告

2、利用allure指定存放路径，执行测试用例
pytest test_pytest/tests/test_calc.py --alluredir=./test_pytest/result

--clean-alluredir：清空执行结果，执行测试用例

3、在测试完成后使用Allure命令查看实际报告，将在默认浏览器中显示生成的报告
allure serve ./test_pytest/result


###附件
报告可以显示许多不同类型的提供的附件，这些附件可以补充测试、步骤或夹具的结果。可以通过以下方式创建附件
allure.attach(body, name, attachment_type, extension)：

body -要写入文件的原始内容。

name -带有文件名的字符串

attachment_type-allure.attachment_type值之一

extension -提供的-将用作创建文件的扩展名。

或
allure.attach.file(source, name, attachment_type, extension)：

source -包含文件路径的字符串。

##fixture（夹具，装置）
https://docs.pytest.org/en/stable/fixture.html