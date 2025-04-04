import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignupView from '../views/SignupView.vue'
import LoginView from '../views/LoginView.vue'
import ProfileView from '../views/ProfileView.vue'
import FollowingsView from '../views/FollowingsView.vue'
import FollowersView from '../views/FollowersView.vue'
import SearchView from '../views/SearchView.vue'
import PostView from '../views/PostView.vue'
import EditProfileView from '../views/EditProfileView.vue'
import ChangePasswordView from '../views/ChangePasswordView.vue'
import NotificationsView from '../views/NotificationsView.vue'
import Page404 from '../components/Page404.vue'

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
    path: '/profile/edit',
    name: 'editprofile',
    component: EditProfileView
  },
  {
    path: '/profile/edit/password',
    name: 'changepassword',
    component: ChangePasswordView
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
    path: '/posts/:id',
    name: 'postview',
    component: PostView
  },
  {
    path: '/notifications',
    name: 'notifications',
    component: NotificationsView
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'page404',
    component: Page404
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router
