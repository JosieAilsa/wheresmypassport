# from wheresmypassport import models
# from wheresmypassport.views.default import my_view
# from wheresmypassport.views.notfound import notfound_view


# def test_my_view_failure(app_request):
#     info = my_view(app_request)
#     assert info.status_int == 500

# def test_my_view_success(app_request, dbsession):

#     info = my_view(app_request)
#     assert app_request.response.status_int == 200
#     assert info['one'].name == 'one'
#     assert info['project'] == 'wheresmypassport'

# def test_notfound_view(app_request):
#     info = notfound_view(app_request)
#     assert app_request.response.status_int == 404
#     assert info == {}
