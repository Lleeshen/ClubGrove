import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ClubSearch from '../views/ClubSearch.vue'
import EventSearch from '../views/ClubEvents.vue'
import NotFound from '../views/NotFound.vue'
import ClubPage from '../views/ClubPage.vue'

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
    path: '/events',
    name: 'eventSearch',
    component: EventSearch
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
