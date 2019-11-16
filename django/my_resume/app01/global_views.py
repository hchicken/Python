
from .models import Type

def guid_tag(request):
    tags = Type.objects.all()
    # print(templatetags)
    # print("111111")
    return {"tags":tags}