def LastFiveMiddleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # request.last5 =(that list)

        print('>>>>>>>> middleware called')
        #pull last 5 list out of the session
        last5_list = request.session.get('last5')
        if last5_list is None:
            last5_list = []
        request.last5 = last5_list

        response = get_response(request)
        # print (request.last5.values())

        # Code to be executed for each request/response after
        # the view is called.
        request.session['last5'] = request.last5
        print(request.session['last5'])
        print('!!!!!! middleware called at end')
        return response

    return middleware
