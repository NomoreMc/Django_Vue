from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from Post.models import Post
from .models import Comment
from .forms import CommentForm
# Create your views here.

class CommentPostView(FormView):
    form_class = CommentForm
    template_name = 'Post/post_detail.html'

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(CommentPostView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        post_id = self.kwargs['post_id']

        post = Post.objects.get(pk=post_id)
        url = post.get_absolute_url()
        return HttpResponseRedirect(url + "#comments")

    def form_invalid(self, form):
        post_id = self.kwargs['id']
        post = Post.objects.get(pk=post_id)

        return self.render_to_response({
            'form': form,
            'post': post
        })

    def form_valid(self, form):
        """提交的数据验证合法后的逻辑"""
        user = self.request.user
        # 提交评论时检查user是否又权限进行评论
        if not user.has_perm('%s.%s' % ("Account", "create_comment")):
            return HttpResponseNotFound('<h1>Sorry! You dont have the permission to comment!</h1>')

        post_id = self.kwargs['post_id']
        post = Post.objects.get(pk=post_id)

        comment = form.save(False)
        comment.post = post
        comment.author = user

        if form.cleaned_data['parent_comment_id']:
            parent_comment = Comment.objects.get(pk=form.cleaned_data['parent_comment_id'])
            comment.parent_comment = parent_comment

        comment.save(True)
        # return HttpResponseRedirect(post.get_absolute_url())
        return HttpResponseRedirect("%s#div-comment-%d" % (post.get_absolute_url(), comment.pk))