import Vue from 'vue'
import VueRouter from 'vue-router'
import Landing_view from '../views/Landing_View.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: Landing_view,
    redirect: '/stories',
    meta: { title: 'Home' },
    children:[
      {
      path: '/stories',
      component: () => import(/* webpackChunkName: "demo" */ '../components/News/stories.vue'),
      meta: { title: 'Stories' }
      },
    ]
  },
]

const router = new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
