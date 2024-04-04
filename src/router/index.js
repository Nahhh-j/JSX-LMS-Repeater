import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'; 
import MainView from '@/views/MainView.vue'
import CommunityView from '@/views/Community.vue'
import CommunityContent from '@/views/CommunityContent.vue'
import ManageView from '@/views/ManageView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: AboutView
    },
    {
      path: '/main',
      name: 'main',
      component: MainView
    },
    {

      path: '/community',
      name: 'community',
      component: CommunityView,
      redirect: '/community/content',
      children : [
        {
          path: '/community/content',
          name: 'community-content',
          component: CommunityContent,
        }
      ]
    },
    {
      path: '/manage',
      name: 'manage',
      component: ManageView
    },
  ]
})

export default router
