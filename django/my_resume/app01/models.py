from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from libs.images import make_thumb
from django.db.models.fields.files import ImageFieldFile
import os
from my_resume.settings import MEDIA_ROOT, THUMB_W, THUMB_H


# Create your models here.



class Type(models.Model):
    type_name = models.CharField(verbose_name="类型名字", max_length=64, )

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = "简历类型"
        verbose_name_plural = verbose_name


class Resume(models.Model):
    # 简历名字c
    resume_name = models.CharField(verbose_name="简历名字", max_length=64)
    # 类型：单页简历，封面，还有多页模板
    resume_type = models.ForeignKey(Type, verbose_name='简历类型', related_name='resume_set')
    # 简历的封面，可以直接存在数据库
    resume_cover_lg = models.ImageField("简历封面", upload_to="cover/")
    # 封面缩略图
    resume_cover = models.ImageField(verbose_name="简历封面缩略图", upload_to='cover/', default='cover/defult.jpg',
                                     editable=False)
    # 上线时间
    resume_onlinetime = models.DateTimeField(verbose_name="上线时间")
    # 浏览次数
    resume_browse = models.CharField(verbose_name="浏览次数", max_length=128, default='0')
    # 下载次数
    resume_down = models.CharField(verbose_name="下载次数", max_length=128, default='0')
    # 下载地址
    resume_url = models.FileField(verbose_name="下载地址", upload_to='templates/')

    def save(self, *args, **kwargs):
        # 将上传的图片先保存
        super().save()

        base, ext = os.path.splitext(self.resume_cover_lg.name)
        # 从头像中生成缩略图
        thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, self.resume_cover_lg.name), THUMB_W, THUMB_H)
        # 缩略图的保存文件全路径
        thumb_path = os.path.join(MEDIA_ROOT, base + f'.{THUMB_W}x{THUMB_H}' + ext)
        # 缩略图相对路径
        relate_thumb_path = os.path.join('../cover'.join(self.resume_cover_lg.name.split('/')[:-1]),
                                         os.path.basename(thumb_path))
        relate_thumb_path = base + f'.{THUMB_W}x{THUMB_H}' + ext
        # 保存缩略图
        thumb_pixbuf.save(thumb_path)
        # 保存字段值
        self.resume_cover = ImageFieldFile(self, self.resume_cover_lg, relate_thumb_path)
        super().save()  # 再保存一下，包括缩略图等

    def __str__(self):
        return self.resume_name

    class Meta():
        verbose_name = "简历"
        verbose_name_plural = verbose_name
        ordering = ['-resume_onlinetime']


class Username(models.Model):
    username = models.CharField(verbose_name="用户账号", max_length=64)
    email = models.CharField(verbose_name="邮箱", max_length=128)
    passwd = models.CharField(verbose_name="密码", max_length=128)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户列表"
        verbose_name_plural = verbose_name


class Collect(models.Model):
    collect_user=models.ForeignKey(Username,verbose_name="用户名")
    collect_resume = models.ForeignKey(Resume,verbose_name="收藏简历")


    class Meta:
        verbose_name = "收列表"
        verbose_name_plural = verbose_name