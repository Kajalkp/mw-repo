from django.http import HttpResponse
class SimpleMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print("pre processing the request")
        response=self.get_response(request)
        print(response)
        print("post processing the request")
        return response
    def process_exception(self,request,exception):
        return HttpResponse("sorry page not found")
