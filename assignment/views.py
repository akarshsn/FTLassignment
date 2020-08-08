from django.shortcuts import redirect


def justRedirect(request):
    return redirect('/custom/api-activity/')

