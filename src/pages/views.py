from django.shortcuts import render
from django.views import View
from pages.models import Sermon, Announcement, Gallery

# Create your views here.
class IndexView(View):
    template_name = "templates/pages/index.html"
    def get(self, request):
        lastest_sermon = Sermon.objects.filter().order_by('-date').first()
        sermon = Sermon.objects.filter().order_by('-date')[:1]
        context = {"sermon": lastest_sermon}
        return render(request, self.template_name, context)

class AboutView(View):
    template_name = "templates/pages/about.html"

    def get(self, request):
        return render(request, self.template_name)

class SermonView(View):

    template_name = "templates/pages/sermon.html"

    def get(self, request):
        return render(request, self.template_name)

class GivingView(View):
    template_name = "templates/pages/giving.html"

    def get(self, request):
        return render(request, self.template_name)

class OutreachView(View):
    template_name = "templates/pages/outreach.html"

    def get(self, request):
        return render(request, self.template_name)

        
class StoreView(View):
    template_name = "templates/pages/store.html"
    def get(self, request):
        return render(request, self.template_name)

class OrderView(View):
    template_name = "templates/pages/order.html"
    def get(self, request):
        return render(request, self.template_name)

class BranchesView(View):
    template_name = "templates/pages/branches.html"
    def get(self, request):
        return render(request, self.template_name)

