from datetime import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    model = Post
    show_content = 'content'
    template_name = 'posts.html'
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    # pk_url_kwarg = 'id'
    def post(self, request, *args, **kwargs):
        post = self.get_object()  # Получаем объект поста
        rating = request.POST.get('rating')  # Получаем значение рейтинга из POST-запроса

        if rating:
            post.rating = int(rating)  # Преобразуем значение рейтинга в целое число
            post.save()  # Сохраняем изменения в базе данных

        return render(request, self.template_name, {self.context_object_name: post})

""" {% block content %}
<h1>Все Посты</h1>
<ul>
  {% for post in object_list %}
    <li>
      <h2>{{ post.title }}</h2>
      <p>{{ post.content }}</p>
    </li>
  {% endfor %}
</ul>
{% endblock content %}"""