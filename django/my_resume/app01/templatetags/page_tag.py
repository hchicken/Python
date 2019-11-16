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
"""


pagenator(page, max_page):
    return <li></li>

"""


# # 方法二
@register.simple_tag(name="short_page")
def short_page(page,sort_resumes,max_page):
    """

    :param page: 当前页
    :param sort_resumes: 排序标签
    :param max_page: 最大页
    :return:
    """
    page_star = 1
    page_end = max_page
    if page > 2:
        page_star = page-2
    if  page+2 < max_page:
        page_end = page+2
    html = ""
    for i in range(page_star, page_end+1):
        if i == page:
            html += f"<li class = 'active'><a href='?sort_resumes={sort_resumes}&page={i}'>{i}</a></li>"
        else:
            html += f"<li><a href='?sort_resumes={sort_resumes}&page={i}'>{i}</a></li>"
    return html
