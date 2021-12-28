from rest_framework.routers import DefaultRouter
from . import (Viewset)

router = DefaultRouter()
router.register('api/user', Viewset.UserAPI)
router.register('api/project', Viewset.ProjectAPI)
router.register('api/news', Viewset.NewsAPI)
