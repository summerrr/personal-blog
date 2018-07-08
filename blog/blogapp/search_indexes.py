from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)#每个索引里面必须有且只能有一个字段为 document=True，
    #这代表 django haystack 和搜索引擎将使用此字段的内容作为索引进行检索(primary field)
    #haystack 提供了use_template=True 在 text 字段中，这样就允许我们使用数据模板去建立搜索引擎索引的文件，
    #数据模板就是那个txt文件
    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()