import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import ProfileView from '../views/ProfileView.vue'
import FollowingsView from '../views/FollowingsView.vue'
import FollowersView from '../views/FollowersView.vue'
import SearchView from '../views/SearchView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/profile/:id',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/profile/:id/following',
    name: 'following',
    component: FollowingsView
  },
  {
    path: '/profile/:id/followers',
    name: 'followers',
    component: FollowersView
  },
  {
    path: '/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
