from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.templatetags.static import static
from .utils import generate_ref_code


class Profile(models.Model):
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
    ]
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="profiles/avatars/", null=True, blank=True)
    id_number = models.CharField(max_length=32, null=True, blank=True)
    college = models.CharField(max_length=32, null=True, blank=True)
    semester = models.CharField(max_length=32, null=True, blank=True)
    hostel = models.CharField(max_length=32, null=True, blank=True)
    room_number = models.CharField(max_length=32, null=True, blank=True)
    year = models.CharField(max_length=32, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    phone = models.CharField(max_length=32, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=8,null=True,blank=True)
    number = models.CharField(max_length=32, null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # self.code = [generate_ref_code() if self.code == ""]
        if self.code == "":
            code = generate_ref_code()
            self.code = code
            # print(code, 'is the code')
        super(Profile,self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} is a {self.role}'
    
    def get_fullname(self):
        return f'{self.user.first_name} {self.user.last_name}'

    # # this is not needed if small_image is created at set_image
    # def save(self, *args, **kwargs):
    #     if getattr(self, '_image_changed', True):
    #         small=rescale_image(self.image,width=100,height=100)
    #         self.image_small=SimpleUploadedFile(name,small_pic)
    #     super(Model, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    @property
    def get_avatar(self):
        return self.avatar.url if self.avatar else static('assets/img/team/default-profile-picture.png')
    
