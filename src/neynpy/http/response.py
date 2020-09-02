class Response:
    """
    An HTTP response base class
    more todo ...
    """
    def __init__(self, text, status_code=200, header=None):
        if header is None:
            header = {'Content-Type': 'text/html'}
        self.text = text
        self.status_code = status_code
        self.header = header

    def serialize_headers(self):
        pass

    def set_cookie(self):
        pass

    def delete_cookie(self):
        pass
