from rest_framework import routers
from .viewsets import jugadorViewsets

router = routers.SimpleRouter()
router.register('jugadores', jugadorViewsets)

urlpatterns = router.urls 