from django.views import View
from django.shortcuts import render

class LandingPageView(View):
    def get(self, request):
        return render(request, 'pages/landing_page.html')
        