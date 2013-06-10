from django.db import models

class PortfolioTag(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title
        
    @staticmethod
    def autocomplete_search_fields():
        return ("id__iexact", "title__icontains",)

class PortfolioItem(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    description = models.TextField()
    responsibilities = models.CharField(max_length=255)
    position = models.PositiveSmallIntegerField("Position")
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(PortfolioTag)
    
    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        model = self.__class__
        
        if self.position is None:
            # Append
            try:
                last = model.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                # First row
                self.position = 0
        
        return super(PortfolioItem, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ('position',)