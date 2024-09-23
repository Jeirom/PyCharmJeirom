from src.decorators import *


def test_log_without_file(capsys):
    @log(None)
    def test_func(x, y):
        return x + y

    test_func(2, 3)
    captured = capsys.readouterr()
    assert captured.out == "test_func ok\n"


def test_log_with_file(capsys):
    @log("test_log.txt")
    def test_func(x, y):
        return x / y

    test_func(2, 0)
    path_to_file = os.path.join(os.path.dirname(__file__), "../logs", "test_log.txt")
    with open(path_to_file, "r", encoding="utf-8") as file:
        assert file.read() == "test_func error: division by zero. Inputs: ((2, 0)), {}"


def test_log_exception_handling(capsys):
    @log(None)
    def test_func(x, y):
        raise ValueError("Something went wrong")

    test_func(2, 3)
    captured = capsys.readouterr()
    assert captured.out == "test_func error: Something went wrong. Inputs: ((2, 3)), {}\n"