from donate.viewsets import DonateViewset, PaymentViewset,PaymentDetailViewset,Give_help_Viewset
from rest_framework import routers


router=routers.DefaultRouter()
router.register('Donation',DonateViewset)
router.register('Payment_Method',PaymentViewset)
router.register('Payment_Details',PaymentDetailViewset)
router.register('Give_Your_Help',Give_help_Viewset)