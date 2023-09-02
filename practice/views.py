from django.shortcuts import render
from django.http import HttpResponse
from .forms import PracticeForm
from django.views.generic.edit import CreateView
from .models import PracticeModel
from django.views.generic import View

# Create your views here.


class PracticeView(View):
    def get(self, request):
        return render(request, "practice/index.html", {
            "form": PracticeForm()
        })

    def post(self, request):

        submitted_form = PracticeForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            submitted_form.save();
            # data = request.POST
            # model = PracticeModel(
            #     user_name=data['user_name'], user_age=data['user_age'], user_image=request.FILES["user_image"])
            # model.save()
            # print(PracticeModel.objects.all())

        return render(request, "practice/index.html", {
            "form": PracticeForm()
        })

# class PracticeView(CreateView):
#     model = PracticeModel
#     form_class = PracticeForm
#     template_name = "practice/index.html"
#     success_url = "/practice"

# def practice_view(request):
#     if(request.method == 'POST'):
#         data = request.POST
#         model = PracticeModel(user_name = data['user_name'], user_age = data['user_age'])
#         model.save()
#         print(data)


#     return render(request, "practice/index.html", {
#         "form": PracticeForm()
#     })
