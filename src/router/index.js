import Vue from 'vue'
import VueRouter from 'vue-router'
import Landing_view from '../views/Landing_View.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: Landing_view,
    meta: { title: 'Home' },
    children: [
      {
        path: '/',
        component: () => import(/* webpackChunkName: "demo" */ '../views/Home.vue'),
        meta: { title: 'Home' }
      },
      {
        path: '/project/:id',
        component: () => import(/* webpackChunkName: "demo" */ '../components/Project/ProjectDetailView.vue'),
        meta: { title: 'Home' }
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
