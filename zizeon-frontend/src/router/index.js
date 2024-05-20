import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import MapView from '@/views/MapView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import QuizView from '@/views/QuizView.vue'
import MyPageView from '@/views/MyPageView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ProductsView from '@/views/ProductsView.vue'
import RecommendView from '@/views/RecommendView.vue'
import QuizAnswerView from '@/views/QuizAnswerView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'

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
      path: '/article',
      name: 'article',
      component: ArticleView
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
    {
    path: '/articles/:id',
    name: 'ArticleDetail',
    component: ArticleDetailView
    },
    {
    path: '/create',
    name: 'ArticleCreate',
    component: ArticleCreateView
    },
  ]
})

export default router
