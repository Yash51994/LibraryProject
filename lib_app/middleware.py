

# def my_middleware(get_response):
#     print("configurations..!")
#     def inner_mw(request):
#         print('before calling view')
#         response = get_response(request)
#         print('after calling view')

#         return response
#     return inner_mw


# class MyMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print("Hello")


#     def __call__(self, request):
#         print('before calling view')
#         response = self.get_response(request)
#         return response


# def my_middleware(get_response):
#     def inner(request):
#         resp = get_response(request)
#         return resp
#     return inner


# class middlewsre:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         resp = self.get_response(request)
#         return resp



# class CustomMiddleware:
#     def __init__(self, get_response):
#         print("Hii..!")
#         self.get_response = get_response

#     def __call__(self, request):
#         print("before calling view")
#         response = self.get_response(request)
#         print("after calling view")

#         return response


def custom_middleware(get_response):
    print("Bhai")
    def inner_mw(request):
        resp = get_response(request)
        print('Hello')
        print(resp.content)
        return resp
    return inner_mw


