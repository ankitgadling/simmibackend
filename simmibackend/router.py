from donate.viewsets import DonateViewset, PaymentViewset,PaymentDetailViewset,Give_help_Viewset
from rest_framework import routers
from volunteer.viewsets import Volunteerviewsets
#from certifications.viewsets import CertificateViewset


router=routers.DefaultRouter()
router.register('donation2',DonateViewset)
router.register('payment_method',PaymentViewset)
router.register('payment_details',PaymentDetailViewset)
router.register('Give_Your_Help',Give_help_Viewset)
router.register('Volunteer',Volunteerviewsets)
#router.register('Certification',CertificateViewset)
