# from django.contrib.auth.models import User
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from django.template.defaultfilters import slugify
# from .models import Blog
# from .utils import get_random_code


# @receiver(pre_save, sender=Blog)
# def pre_save_create_code(sender, instance, **kwargs):
#     if not instance.slug:
#         instance.slug = slugify(
#             instance.title + " " + get_random_code())