import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/grade',
    name: 'Grade',
    component: () => import('../views/Grade.vue')
  },
  {
    path: '/volume',
    name: 'Volume',
    component: () => import('../views/Volume.vue')
  },
  {
    path: '/unit',
    name: 'Uint',
    component: () => import('../views/Unit.vue')
  },
  {
    path: '/word',
    name: 'Word',
    component: () => import('../views/Word.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
