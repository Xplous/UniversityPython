# Запуск через pytest test.py
from func_merge import merge_and_write
import pytest

@pytest.mark.parametrize(
    "file1_path, file2_path, output_file_path, result",
    [
        ("./ex1.txt","./ex2.txt","./out.txt","Hello World"),
        ("./ex1.txt","./ex2.txt","./out.txt","GoodBye World!")
    ]
)
def test_merge_and_write(file1_path, file2_path, output_file_path, result):
    assert merge_and_write(file1_path, file2_path, output_file_path) == result
@pytest.mark.parametrize(
        "file1, file2, output, result",
        [
            ("./3.txt","./12.txt","./out.txt","Один из файлов не найден"),
            ("./3.txt","./12.txt","./out.txt","ТУТ ЧТО ТО ЧТОБЫ ОШИБКУ ВЫДАЛО"),
        ]
)
def test_merge_and_write_missing_file(file1, file2, output, result):
    assert merge_and_write(file1, file2, output) == result