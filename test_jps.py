# 1、创建以test开头的PY文件

# 2、创建以test开头的函数

# 3、在函数中编写测试代码

# 4、使用assert语句进行断言，判断测试结果是否符合预期

# 5、运行测试文件，查看测试结果

def test_addition():
    result = 2 + 3
    assert result == 5, f"Expected 5 but got {result}"

def test_subtraction():
    result = 5 - 3
    assert result == 2, f"Expected 2 but got {result}"

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
        