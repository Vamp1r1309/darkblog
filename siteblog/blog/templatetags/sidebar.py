from django import template

from blog.models import Post, Tag, Category

register = template.Library()


@register.inclusion_tag('blog/categories.html',)
def show_category():
    categories = Category.objects.all()
    return {'categories': categories}



@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {"posts":posts}


@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {"tags":tags}

# @register.inclusion_tag('blog/search_tpl.html')
# def get_search():
    # pass