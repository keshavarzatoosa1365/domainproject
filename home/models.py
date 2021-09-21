from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = "دسته بندی "
        verbose_name_plural = "دسته بندی"

    name = models.CharField("نام دسته بندی", max_length=50)

    def __str__(self):
        return self.name


class Suffix(models.Model):
    class Meta:
        verbose_name = "پسوند دامنه"
        verbose_name_plural = "پسوند دامنه"

    name = models.CharField("نام دسته بندی دامنه", max_length=50)

    def __str__(self):
        return self.name


class Domain(models.Model):
    class Meta:
        verbose_name = "دامنه"
        verbose_name_plural = "دامنه"

    persian_name = models.CharField("نام دامنه به فارسی", max_length=50)
    english_name = models.CharField("نام دامنه به انگلیسی", max_length=50)
    category = models.ManyToManyField(Category, verbose_name="نام دسته بندی")
    suffix_name = models.ForeignKey(Suffix, on_delete=models.CASCADE, verbose_name="نام پسوند دامنه")
    content = models.BooleanField("محتوا", default=False)
    description = models.TextField("توضیحات دامنه")
    price = models.CharField("قیمت دامنه", null=True, blank=True, max_length=50)
    agreement_price = models.BooleanField("قیمت توافقی", default=False)
    top_domains = models.BooleanField("برترین دامنه ها", default=False)

    def length_of_domain(self):
        m = len(self.english_name)
        return m

    def complete_name(self):
        m = str(self.english_name) + "." + str(self.suffix_name)
        return m

    def __str__(self):
        return self.english_name
