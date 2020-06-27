#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:04:16 2019

@author: sambhav
"""

import uuid

from django.db import models
from django.utils.timezone import now

from apps.users.api.user.models import User


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    phone_number = models.CharField(max_length=10, unique=False, null=False, blank=False)
    date_of_birth = models.CharField(max_length=50, unique=False)
    # GENDER_CHOICES = (
    #     ('M', 'Male'),
    #     ('F', 'Female'),
    # )
    # gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    gender = models.CharField(max_length=10, unique=False)
    last_login_date_time = models.DateTimeField(default=now)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile"