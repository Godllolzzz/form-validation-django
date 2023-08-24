from django.shortcuts import render, HttpResponseRedirect
from .forms import ReviewForm

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect("/thank-you")
    

    form = ReviewForm()
    return render(request, "reviews/review.html", {
        "form": form,
    })

def thank_you(request):
    return render(request, "reviews/thank_you.html")