from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


import socket
import sys


def resolve(domain):
    host = domain
    port = 80
    if ':' in domain:
        host, port = domain.split(':')
        port = int(port)
    info = socket.getaddrinfo(host, port)
    return info[0][4][0]


class WhiteList(models.Model):
    ip = models.GenericIPAddressField(
        verbose_name="IP地址", blank=True, null=True)
    domain = models.CharField(verbose_name="域名", blank=True, max_length=255)

    def __str__(self):
        return self.ip

    def save(self, *args, **kwargs):
        if not self.ip and self.domain:
            try:
                self.ip = resolve(self.domain)
            except socket.gaierror:
                pass
        super(WhiteList, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "访问白名单"
        verbose_name_plural = "访问白名单"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_manager = models.BooleanField(
        verbose_name='管理员状态', help_text="管理员登陆不受ip限制", default=False)


def save_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)


post_save.connect(save_profile, sender=User)