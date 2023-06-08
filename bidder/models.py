from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Company(models.Model):
    """
    Simply contains company details, referenced by Placement model
    """

    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_description = models.TextField(default="There is currently no description available for this company.")

    company_created = models.DateTimeField(auto_now_add=True)
    company_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
class Placement(models.Model):
    """
    A placement allows investors to bid on company capital raise
    """

    placement_title = models.CharField(max_length=255)
    placement_slug = models.SlugField()
    placement_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    placement_created = models.DateTimeField(auto_now_add=True)
    placement_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.placement_title


class Bid(models.Model):
    """
    The bid, synonmous with 'order'
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_status = models.BooleanField(default=False)

    bid_created = models.DateTimeField(auto_now_add=True)
    bid_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} -{}'.format(self.user, self.bid_status)


class PlacementBid(models.Model):
    """
    The junction table for placement and bid models/tables. Contains every instance of a bid for a placement
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    placement = models.ForeignKey(Placement, on_delete=models.CASCADE)
    bid  = models.ForeignKey(Bid, on_delete=models.CASCADE)
    offer = models.IntegerField()
    shares = models.IntegerField()
    confirmed = models.BooleanField(default=False)
    
    placementbid_created = models.DateTimeField(auto_now_add=True)
    placementbid_modified = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['-placementbid_modified'] 

    def __str__(self):
        return '{} - {} - {}'.format(self.shares, self.offer, self.user)
    
    
class Auction(models.Model):
    ABSTRACT = 'AB'
    MODERN = 'MN'
    ILLUSTRATION = 'IN'

    select_category = [
        ('ABSTRACT', 'Abstract'),
        ('MODERN', 'Modern'),
        ('ILLUSTRATION', 'Illustration')
    ]

    title = models.CharField(max_length=25)
    description = models.TextField()
    current_bid = models.IntegerField(null=False, blank=False)
    image_url = models.URLField(verbose_name="URL", max_length=255, unique=True, null=True, blank=True)
    category = models.CharField(
        choices=select_category,
        max_length=12,
        default=MODERN,
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']

# class Bids(models.Model):
#     auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bidding')
#     user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='bidding')
#     new_bid = models.DecimalField(max_digits=8, decimal_places=2)
#     # new_bid = MoneyField(max_digits=10, decimal_places=2, null=False, blank=False, default_currency='USD', default=0)
#     done_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['auction', '-new_bid']
#     def __str__(self):
#         return self.auction