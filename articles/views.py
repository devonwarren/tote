from django.shortcuts import render, get_object_or_404, redirect
from articles.models import Contributor, Article
from django.db.models import Q
from django.contrib import messages
from django.conf import settings
import mailchimp


# view article listing from author
def author_view(request, slug):
    author = get_object_or_404(Contributor, slug=slug)

    articles = Article.objects.live().filter(
        Q(text_by=author) | Q(art_by=author))

    return render(request, "articles/author.html", {
        'author': author,
        'articles': articles
    })


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            api = mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)
            api.lists.subscribe('0c1c51c413', {'email': email})
            messages.add_message(
                request, messages.INFO,
                "Thanks for subscribing! You should have a confirmation email")
        except mailchimp.ListAlreadySubscribedError as detail:
            messages.add_message(request, messages.INFO,
                                 "You are already subscribed!")
        return redirect('/')
