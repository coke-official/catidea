class SimpleMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response

        def __call__(self, request):
            response = self.get_response(request)

            ## 動作テスト用のログ
            print('---- middleware called ----')

            return response
