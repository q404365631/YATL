class Request:
    def __init__(self, url, method, headers, data, timeout):
        self.url = url
        self.method = method
        self.headers = headers
        self.data = data
        self.timeout = timeout
