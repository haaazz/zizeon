<template>
  <div class="appbody">
    <div class="navdiv">
      <nav>
        <RouterLink :to="'/'" class="nav-link" :class="{ 'active-link': $route.path === '/' }"> 홈 </RouterLink> |
        <RouterLink :to="'/map'" class="nav-link" :class="{ 'active-link': $route.path === '/map' }"> 근처 은행 </RouterLink> |
        <RouterLink :to="'/exchange'" class="nav-link" :class="{ 'active-link': $route.path === '/exchange' }"> 환율 정보 </RouterLink> |
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