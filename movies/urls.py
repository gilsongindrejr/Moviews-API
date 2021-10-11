from rest_framework.routers import SimpleRouter

from .views import MoviesViewSet, RatingsViewSet

router = SimpleRouter()
router.register('movies', MoviesViewSet)
router.register('ratings', RatingsViewSet)
