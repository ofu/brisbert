import bottle

@bottle.get('/')
def test_view():
    """
    """
    return "<html><body>Hello World</body></html>"

if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, debug=True)
