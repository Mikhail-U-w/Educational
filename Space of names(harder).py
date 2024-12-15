def test_function():
    string = "Я в области видимости функции test_function"
    def inner_function():
        print(string)
    inner_function()
inner_function()
test_function()