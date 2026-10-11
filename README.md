# py_test
pytest测试用例（一）

# 安装PYTEST
pip install pytest

# 1、创建以test开头的PY文件

# 2、创建以test开头的函数

# 3、在函数中编写测试代码

# 4、使用assert语句进行断言，判断测试结果是否符合预期    a、if    b、assert

# 5、运行测试文件，查看测试结果

~~~~
def test_addition():
    result = 2 + 3
    assert result == 5, f"Expected 5 but got {result}"

def test_subtraction():
    result = 5 - 3
    assert result == 2, f"Expected 2 but got {result}"
~~~~

## 运行结果

============================================================= test session starts   =============================================================   
platform win32 -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0   
rootdir: D:\claudecodelx\py_test   
plugins: anyio-4.10.0   
collected 2    items                                                                                                                              

test_jps.py                                                       [100%]  

============================================================== 2 passed in 0.04s   ==============================================================   

# 6、用例可以放在类中，类名字必须以Test开头

~~~~
class TestMathOperations:
    def test_multiplication(self):
        result = 4 * 3
        assert result == 12, f"Expected 12 but got {result}"

    def test_division(self):
        result = 10 / 2
        assert result == 5, f"Expected 5 but got {result}"
    def test_division_by_zero(self):
        try:
            result = 10 / 0
        except ZeroDivisionError:
            result = None
        assert result is None, "Expected None for division by zero"
        
~~~~
## 运行结果
PS D:\claudecodelx\py_test> pytest -vs
============================================================= test session starts =============================================================
platform win32 -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0 -- C:\ProgramData\anaconda3\python.exe
cachedir: .pytest_cache
rootdir: D:\claudecodelx\py_test
plugins: anyio-4.10.0
collected 5 items                                                                                                                              

test_jps.py::test_addition PASSED
test_jps.py::test_subtraction PASSED
test_jps.py::TestMathOperations::test_multiplication PASSED
test_jps.py::TestMathOperations::test_division PASSED
test_jps.py::TestMathOperations::test_division_by_zero PASSED

============================================================== 5 passed in 0.05s ==============================================================

# 7、测试文件可以放在任何项目中的目录下，pytest会自动查找test开头的文件

# 8、筛选用例

使用@pytest.mark.<筛选名字>进行标记装饰    

1.注册：在配置文件pytest.ini文件中  
2.使用：装饰器@pytest.mark.<筛选名字>  
3.筛选：命令行参数 -m <筛选名字>  

~~~~
import pytest

@pytest.mark.shuaixuan
def test_filter_cases():
    assert 1 == 1
~~~~

## 运行命令
 pytest -m shuaixuan  
## 运行结果
====================================================================== test session starts ======================================================================  
platform win32 -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0  
rootdir: D:\claudecodelx\py_test  
plugins: anyio-4.10.0  
collected 6 items / 5 deselected / 1   selected                                                                                                                    

test_sxyl.py                                                        [100%]  

======================================================================= warnings summary   ========================================================================  
test_sxyl.py:5
  D:\claudecodelx\py_test\test_sxyl.py:5: PytestUnknownMarkWarning: Unknown pytest.mark.shuaixuan - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @pytest.mark.shuaixuan  

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
========================================================== 1 passed, 5 deselected, 1 warning in 0.05s   ===========================================================

## 一个函数多次筛选标记
~~~~
@pytest.mark.shuaixuan
@pytest.mark.apitest
@pytest.mark.dbtest
def test_filter_cases():
    assert 1 == 1
~~~~

## 运行命令
pytest -m apitest      

## 运行结果
====================================================================== test session starts   ======================================================================  
platform win32 -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0  
rootdir: D:\claudecodelx\py_test  
configfile: pytest.ini  
plugins: anyio-4.10.0  
collected 6 items / 5 deselected / 1   selected                                                                                                                     

test_sxyl.py .                                                                   [100%]    

================================================================ 1 passed, 5 deselected in 0.05s    ================================================================   

## pytest.ini 文件结构

[pytest]
markers =
    shuaixuan: mark test cases for filtering  
    apitest: mark test cases for a specific category  
    dbtest: mark test cases for another category  
    protest: mark test cases for a third category  


## 9、内置标记

1、不需要注册
2、不仅用例筛选，还有特殊效果
3、不同的内置标记产生不同的效果

@pytest.mark.skip           无条件跳过  
@pytest.mark.skipif         有条件跳过（当判断为真时跳过）
@pytest.mark.xfail          预期失败
@pytest.mark.parametrize    参数化测试，动态生成更多用例
@pytest.mark.usefixture     自动使用fixture 

## 10、fixture    夹具：实现用例前置、自动化后置操作

1、它是一个函数

2、装饰器  @pytest.fixture

3、使用yield区分前后置

4、fixture的共享的好处：A、复用fixture可以减少前置、后置操作；B、在用例之间互相传递参数；
            共享的坏处：fixture不会重复运行

5、fixture的作用范围

    A、Function：默认，在函数范围内进行共享
    B、Class：在同一个类范围内进行共享
    C、module：在同一个模块（文件）范围内进行共享
    D、package：在同一个包（目录）范围内进行共享
    E、seesion：在同一次执行的所有用例中进行共享

~~~~
import pytest

#创建一个fixture函数

@pytest.fixture(scope="session")
def sample_fixture():
    # Setup code for the fixture
    data = {"key": "value"}
    yield data
    # Teardown code for the fixture (if needed)
    data.clear()


# 在函数中使用 fixture 
@pytest.mark.myfirturetest
def test_using_fixture1(sample_fixture,doctest_namespace):     #doctest_namespace 参数传递
    name='test_fixture1'
    doctest_namespace['name'] = name
    assert sample_fixture["key"] == "value"

# 在函数中使用 fixture 
@pytest.mark.myfirturetest
def test_using_fixture2(sample_fixture,doctest_namespace):
    name=doctest_namespace['name'] 
    print(name)
    assert sample_fixture["key"] == "value"
~~~~

## 运行命令
 pytest -m myfirturetest -vs

## 运行结果
================================================================test session starts =================================  
platform win32 -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0 -- C:\ProgramData\anaconda3\python.exe  
cachedir: .pytest_cache   
rootdir: D:\claudecodelx\py_test   
configfile: pytest.ini   
plugins: anyio-4.10.0   
collected 8 items / 6 deselected /   2selected                                                                                                                       

test_fixture.py::test_using_fixture1 PASSED  
test_fixture.py::test_using_fixture2 test_fixture1  
PASSED  
 
=================================================== 2 passed, 6 deselected in 0.05s  =========================     


