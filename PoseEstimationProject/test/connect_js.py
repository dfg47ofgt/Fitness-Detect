import PyV8

ctx = PyV8.JSContext()

ctx.enter()
js_file = open('./UI/test.js')
js_data = js_file.read()
if js_data:
    print("go")
js_file.close()



