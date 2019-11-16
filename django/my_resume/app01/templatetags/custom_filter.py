from django import template

register = template.Library()


"""
"abc"|upper   =>  upper("abc")
"abc"|cut:"a" =>  cut("abc", "a")



"""
# 方法一
# "abc" | shorttile:100

# def short_title(value, max_length):
#     max_length = int(max_length)
#     if len(value)<= max_length:
#         return value
#     else:
#         return value[:max_length-2]+">>"
#
#
# register.filter("short_title", short_title)


# 方法二
@register.filter(name="short_title")
def short_title(value, max_length):
    max_length = int(max_length)
    if len(value)<= max_length:
        return value
    else:
        return value[:max_length-2]+">>"