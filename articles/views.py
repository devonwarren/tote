from django.shortcuts import render, get_object_or_404
from articles.models import Contributor, Article
from django.db.models import Q


# view article listing from author
def author_view(request, slug):
    author = get_object_or_404(Contributor, slug=slug)

    articles = Article.objects.live().filter(
        Q(text_by=author) | Q(art_by=author))

    return render(request, "articles/author.html", {
        'author': author,
        'articles': articles
    })
