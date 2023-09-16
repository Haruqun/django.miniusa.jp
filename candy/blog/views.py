# views.py

from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# ブログの記事一覧ページ
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

# ブログの記事詳細ページ
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

# カテゴリによる絞り込み
def posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'posts_by_category.html', {'posts': posts, 'category': category})
