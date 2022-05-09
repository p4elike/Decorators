from logger import loger_constructor_decor

@loger_constructor_decor('logs.txt')
def test_def(a, b):
    return a + b


if __name__ == '__main__':
    test_def(1000,5000)
    test_def(100002,2500000)
    test_def(22,1215)
    result_file_name = 'result_log.txt'
    result_dir = r'C:\Git Practic\Netology\SQLpost\Decorator\result'