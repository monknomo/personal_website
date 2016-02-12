from bottle import get, run, static_file

@get('/')
def get_index():
    return static_file('index.html', root='./output')

@get('/<filename:path>')
def get_static(filename):
    return static_file(filename, root='./output')
    
if __name__ == "__main__":
    run(host='localhost', port=8080)