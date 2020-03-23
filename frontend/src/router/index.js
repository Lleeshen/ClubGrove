import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ClubSearch from '../views/ClubSearch.vue'
import ClubEvent from '../views/ClubEvents.vue'
import EventSearch from '../views/Events.vue'
import ClubPage from '../views/ClubPage.vue'
import ClubManageEvent from '../views/ClubManage.vue'
import Admin from '../views/Admin.vue'
import NotFound from '../views/NotFound.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/club',
    name: 'clubSearch',
    component: ClubSearch
  },
  {
    path: '/club/:name',
    name: 'clubPage',
    component: ClubPage
  },
  {
    path: '/club/:name/events',
    name: 'clubEvent',
    component: ClubEvent,
    props: true
  },
  {
    path: '/club/:name/events/manage',
    name: 'clubManage',
    component: ClubManageEvent,
    props: true
  },
  {
    path: '/events',
    name: 'eventSearch',
    component: EventSearch
  },
  {
    path: '/admin',
    name: 'admin',
    component: Admin
  },
  {
    path: '*',
    name: 'Not Found',
    component: NotFound
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
