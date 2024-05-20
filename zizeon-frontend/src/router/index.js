import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import MapView from '@/views/MapView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import QuizView from '@/views/QuizView.vue'
import MyPageView from '@/views/MyPageView.vue'
import CommunityView from '@/views/CommunityView.vue'
import ProductsView from '@/views/ProductsView.vue'
import RecommendView from '@/views/RecommendView.vue'
import QuizAnswerView from '@/views/QuizAnswerView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeView
    },
    {
      path: '/mypage',
      name: 'mypage',
      component: MyPageView
    },
    {
      path: '/quiz',
      name: 'quiz',
      component: QuizView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/products',
      name: 'products',
      component: ProductsView
    },
    {
      path: '/recommend',
      name: 'recommend',
      component: RecommendView
    },
    {
        path: '/answer',
        name: 'answer',
        component: QuizAnswerView
      },
  ]
})

export default router
