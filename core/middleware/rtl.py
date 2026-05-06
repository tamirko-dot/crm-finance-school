class RTLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Content-Language"] = "he"
        return response

    def process_template_response(self, request, response):
        if hasattr(response, "context_data") and response.context_data is not None:
            response.context_data["direction"] = "rtl"
            response.context_data["lang"] = "he"
        return response
