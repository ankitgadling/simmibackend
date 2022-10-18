from donate.viewsets import DonateViewset, PaymentViewset,PaymentDetailViewset
from rest_framework import routers


router=routers.DefaultRouter()
router.register('donation',DonateViewset)
router.register('payment_method',PaymentViewset)
router.register('payment_details',PaymentDetailViewset)