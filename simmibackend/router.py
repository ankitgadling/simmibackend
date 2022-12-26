from donate.models import upi_tran
from donate.viewsets import DonateViewset, PaymentViewset,PaymentDetailViewset,Give_help_Viewset,Upi_viewset
from rest_framework import routers
from volunteer.views import excel_file_for_volunteer
from volunteer.viewsets import Volunteerviewsets
#from certifications.viewsets import CertificateViewset


router=routers.DefaultRouter()
router.register('donation2',DonateViewset)
router.register('payment_method',PaymentViewset)
# router.register('payment_details',PaymentDetailViewset)
router.register('Give_Your_Help',Give_help_Viewset)
router.register('Volunteer',Volunteerviewsets)
router.register('upi',Upi_viewset)
