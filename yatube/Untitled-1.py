class Group(models.Model):
    title = models.CharField(max_length = 250)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, blank=True, null=True, on_delete=models.SET_NULL,related_name='posts')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'        
    )

    admin.site.register(Group)

    from .models import Post, Group


    class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    list_editable = ('group',) 
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',) 
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date',) 
    empty_value_display = '-пусто-'
    

     group = models.ForeignKey(
        Group, 
        blank=True, 
        null=True, 
        on_delete=models.CASCADE, 
        related_name='posts'
    )