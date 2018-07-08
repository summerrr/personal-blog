from django import template
from ..models import Post,Category,Tag
from django.db.models.aggregates import Count


register = template.Library()

#获取最新文章
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
#按时间归档
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

#按分类归档	
@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    #使用 filter 方法把 num_posts 的值小于 1 的分类过滤掉。因为 num_posts 的值小于 1 表示该分类下没有文章
    #annotate 方法不局限于用于本文提到的统计分类下的文章数，你也可以举一反三，
    #只要是两个 model 类通过 ForeignKey 或者 ManyToMany 关联起来，那么就可以使用 annotate 方法来统计数量

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)