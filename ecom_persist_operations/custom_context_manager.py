


class MyContextManager:

    def __init__(self):
        print('inside init')

    def __enter__(self):
        print('inside enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('inside exit')

with MyContextManager() as mxt :
    print('inside with block')




