<template>
  <div class="appbody">
    <div class="navdiv">
      <nav>
        <RouterLink :to="'/'" class="nav-link" :class="{ 'active-link': $route.path === '/' }"> 홈 </RouterLink> |
        <RouterLink :to="'/quiz'" class="nav-link" :class="{ 'active-link': $route.path === '/quiz' }"> 금융 퀴즈 </RouterLink> |
        <RouterLink :to="'/products'" class="nav-link" :class="{ 'active-link': $route.path === '/products' }"> 전체 상품 조회 </RouterLink> |
        <RouterLink :to="'/recommend'" class="nav-link" :class="{ 'active-link': $route.path === '/recommend' }"> 추천 상품 조회 </RouterLink> |
        <RouterLink :to="'/map'" class="nav-link" :class="{ 'active-link': $route.path === '/map' }"> 근처 은행 </RouterLink> |
        <RouterLink :to="'/exchange'" class="nav-link" :class="{ 'active-link': $route.path === '/exchange' }"> 환율 정보 </RouterLink> |
        <RouterLink :to="'/community'" class="nav-link" :class="{ 'active-link': $route.path === '/community' }"> 커뮤니티 </RouterLink> |
        <RouterLink :to="'/mypage'" class="nav-link" :class="{ 'active-link': $route.path === '/mypage' }"> 마이페이지 </RouterLink> |
      </nav>
      <hr>
    </div>
    <div>
      <RouterView/>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped>
.appbody {
  background-image: url("assets/22469205.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  height: 100vh;
  opacity: 0.8;
  font-family: 'YeongjuSeonbi';
}
.nav-link {
  color: black;
  text-decoration: none;
}
.active-link {
  color: #53813E;
}
nav {
  font-size: 1.5rem;
  text-align: center;
  color: #E8B05E;
}
.navdiv {
  padding-top: 30px;
}
hr {
  border: 1px solid #E8B05E;
}
</style>