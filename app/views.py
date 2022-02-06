from django.views.generic import ListView
from .models import Post

class showpost(ListView):
    model=Post
    template_name="base.html"
    
