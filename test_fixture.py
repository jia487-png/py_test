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
