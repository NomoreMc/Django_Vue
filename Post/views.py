from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound

from django.utils import timezone

from .models import Post
from Account.models import DefaultUser
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# 用于列出所有tags，以及删除无用tags
from taggit.models import Tag
from django.db.models import Count

# 改写post create
# from .forms import PostCreateForm, TopicCreateForm
from .filters import PostFilter

from Comment.forms import CommentForm

# from django.template.defaulttags import register 没用到
import collections

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'mainTemplates/home.html', context)

# 主页为显示所有的Post以及tag, topic
class PostListView(ListView):
    # 要query的model
    model = Post
    # 使用的html模版
    template_name = 'mainTemplates/home.html'
    # ListView默认将query后的object放入一个object_list中
    context_object_name = 'posts'
    # 设定post的展示顺序
    ordering = ['-date_posted']
    # 分页，每页9个post
    paginate_by = 9

    # 给context添加tags
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 用于统计标签数目
        tags = Tag.objects.all()
        queryset = tags.annotate(num_times=Count('taggit_taggeditem_items'))
        # 统计每个tag的计数
        tag_count = {}
        for times_appear in queryset:
            tag_count[times_appear.name] = times_appear.num_times
        # 使用sorted后，输出的结果为list of tuple,而不是字典
        tag_count = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)
        # 使用collections.OerderedDict将其转换回字典再给context
        tag_count = collections.OrderedDict(tag_count)

        # search form
        posts_filter = PostFilter(self.request.GET)

        # 用于显示文章类别
        # topics = Topic.objects.all()

        # # 对topic进行排序输出
        # topic_count = {}
        # for topic in topics:
        #     topic_count[topic] = topic.post_set.all().count()
        # topic_count = sorted(topic_count.items(), key=lambda x: x[1], reverse=True)
        # topic_count = collections.OrderedDict(topic_count)

        # 传至前端的字典
        # context["topics"] = topics
        context["PostFilter_form"] = posts_filter
        context["each_tag_appear"] = tag_count
        # context["each_topic_appear"] = topic_count
        return context

    def get_queryset(self):
        # 将放在model中的Post作为filter的queryset
        qs = self.model.objects.all()
        posts_filtered_list = PostFilter(self.request.GET, queryset=qs)
        # paginator = Paginator(posts_filtered_list, 6)
        return posts_filtered_list.qs.order_by('-date_posted')

# 查看单个user的posts，只是查看
class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(DefaultUser, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# user自己的posts，带修改链接，所以要求用户通过登录和test_func
class MyPostListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(DefaultUser, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

    # 用于测试当前用户是否和url中请求的一致
    def test_func(self):
        user = get_object_or_404(DefaultUser, username=self.kwargs.get('username'))
        if user == self.request.user:
            return True
        return False

# 一个post的细节页面，只显示信息
class PostDetailView(DetailView):
    model = Post
    template_name = 'Post/post_detail.html'

    def get_object(self, queryset=None):
        obj = super(PostDetailView, self).get_object()
        obj.viewed()
        self.object = obj
        return obj

    def get_context_data(self, **kwargs):
        # 评论的表单
        comment_form = CommentForm()
        # 获取某个post所关联的评论集合
        post_comments = self.object.comment_list()
        # 筛选出所有一级评论（非子评论）作为父级评论
        parent_comments = post_comments.filter(parent_comment=None)

        # 对评论进行分页
        # 对一级评论进行分页，每页 10 个评论
        paginator = Paginator(parent_comments, 10)
        # 示例: query = request.GET.get('blabla', 1);  使用request.GET()时，当获取不到blabla时，会导致KeyError；
        #       但是使用request.GET.get会在获取不到时使用第二个参数代替。
        # 以下即为：如果没有获取到comment_page，那么就使用 1 代替
        page = self.request.GET.get('comment_page', 1)
        p_comments = paginator.page(page)
        next_page = p_comments.next_page_number() if p_comments.has_next() else None
        prev_page = p_comments.previous_page_number() if p_comments.has_previous() else None

        if next_page:
            kwargs['comment_next_page_url'] = self.object.get_absolute_url() + f'?comment_page={next_page}#commentlist-container'
        if prev_page:
            kwargs['comment_prev_page_url'] = self.object.get_absolute_url() + f'?comment_page={prev_page}#commentlist-container'

        # 检查更新日期是否与发布日期相同
        dateCreated = self.object.date_posted.replace(microsecond=0)
        dateModified = self.object.last_mod_time.replace(microsecond=0)
        kwargs['is_modified'] = (dateCreated != dateModified)

        # 前端参数：
        # 评论表单
        kwargs['form'] = comment_form
        # 当前post的所有评论，包含一级和二级评论
        kwargs['post_comments'] = post_comments
        # 评论分页，分页是按照一级评论进行分页的
        kwargs['p_comments'] = p_comments
        # 评论总数，若无评论则不展示
        kwargs['comment_count'] = len(parent_comments) if parent_comments else 0

        return super(PostDetailView, self).get_context_data(**kwargs)

# class TopicListView(ListView):
#     model = Post
#     # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     #ordering = ['-date_posted']
#     paginate_by = 5

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         topics = Topic.objects.all()

#         # 对topic进行排序输出
#         topic_count = {}
#         for topic in topics:
#             topic_count[topic] = topic.post_set.all().count()
#         topic_count = sorted(topic_count.items(), key=lambda x: x[1], reverse=True)
#         topic_count = collections.OrderedDict(topic_count)

#         context["each_topic_appear"] = topic_count
#         context["topics"] = topics
#         return context

#     def get_queryset(self):
#         topic_name = get_object_or_404(
#             Topic, name=self.kwargs.get('topic'))
#         return Post.objects.filter(topic=topic_name).order_by('-date_posted')

# 要点: 1.为post加author；
#       2.Post model中对image进行resize(去Post model那)；3.在html中的form中加入enctype="multipart/form-data"
@login_required
def PostCreate(request):
    if not request.user.has_perm('%s.%s' % ("Account", "create_post")):
        return HttpResponseNotFound('<h1>Sorry! You dont have the permission to create post!</h1>')
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        #form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('home')
    else:
        context = {'form': form}
    return render(request, 'Post/post_create.html', {'form': form})

# @login_required
# def TopicCreate(request):
#     if not request.user.has_perm('%s.%s' % ("Account", "create_series")):
#         return HttpResponseNotFound('<h1>Sorry! You dont have the permission to create series!</h1>')
#     form = TopicCreateForm()
#     if request.method == 'POST':
#         form = TopicCreateForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         context = {'form': form}
#     return render(request, 'Post/topic_create.html', {'form': form})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

    # post被删除时，如果对应的tag的总数为0了，则将对应的tag删除
    # 注意了，如果是在admin中删除掉post，那么并不会过滤掉数量为0的tag，因为并不会执行到下面这个delete函数
    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        finally:
            Tag.objects.annotate(
                ntag=Count('taggit_taggeditem_items')
            ).filter(ntag=0).delete()