# coding: utf-8

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse as r
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.translation import ugettext as _
from django.template import RequestContext

from parsifal.reviews.models import *
from parsifal.reviews.decorators import author_required, author_or_visitor_required, visitor_required

@author_or_visitor_required
@login_required
def comments(request, username, review_name):
    review = get_object_or_404(Review, name=review_name, author__username__iexact=username)
    comments = review.get_visitors_comments(request.user)
    return render(request, 'comments/comments.html', { 'review': review, 'comments': comments })

@author_or_visitor_required
@login_required
def comment_detailed(request, username, review_name, comment_id):
    review = get_object_or_404(Review, name=review_name, author__username__iexact=username)
    comment = VisitorComment.objects.get(pk=comment_id)
    return render(request, 'comments/comment_detailed.html', { 'review': review, 'comment': comment })

@login_required
def save_visitor_comment(request):
    try:
        print 'save'
        review_id = request.POST['review-id']
        comment = request.POST['comment']
        about = request.POST['about']
        parent_id = request.POST['parent']
        user = request.user
        to = request.POST['to']

        review = Review.objects.get(pk=review_id)
        parent_comment = VisitorComment.objects.get(pk=parent_id)

        comment = VisitorComment(
                    review=review,
                    comment=comment,
                    about=about,
                    to=to,
                    user=user,
                    parent=parent_comment)
        comment.save()

        if parent_id:
            context = RequestContext(request, {'answer': comment})
            return render_to_response('comments/partial_children_comment.html', context)

        return HttpResponse(_('Your comment have been sended successfully!'))
    except Exception as e:
        print e
        return HttpResponseBadRequest()
