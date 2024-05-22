<template>
  <div>
    <div>
      <div>
        <nav>
          <RouterLink
            :to="'/'"
            class="nav-link"
            :class="{ 'active-link': $route.path === '/' }"
          >
            홈
          </RouterLink>
          |
          <RouterLink
            :to="'/quiz'"
            class="nav-link"
            :class="{ 'active-link': $route.path === '/quiz' }"
          >
            금융 퀴즈
          </RouterLink>
          |
          <RouterLink
            :to="'/products'"
            class="nav-link"
            :class="{ 'active-link': $route.path === '/products' }"
          >
            전체 상품 조회
          </RouterLink>
          |
          <RouterLink
            :to="'/recommend'"
            class="nav-link"
            :class="{ 'active-link': $route.path === '/recommend' }"
          >
            추천 상품 조회
          </RouterLink>
          |
          <RouterLink
            :to="'/map'"
            class="nav-link"
            :class="{ 'active-link': $route.path === '/map' }"
          >
            근처 은행
          </RouterLink>
          |
          <RouterLink
            :to="'/exchange'"
            class="nav-link"
            :class="{ 'active-link': $route.path === '/exchange' }"
          >
            환율 정보
          </RouterLink>
          |
          <RouterLink
            :to="'/article'"
            class="nav-link"
            :class="{ 'active-link': $route.path === '/article' }"
          >
            커뮤니티
          </RouterLink>
          |
          <RouterLink
            :to="'/mypage'"
            class="nav-link"
            :class="{ 'active-link': $route.path === '/mypage' }"
            @click="checkLogin"
          >
            마이페이지
          </RouterLink>
        </nav>
        <hr />
      </div>
      <div>
        <RouterView />
      </div>
    </div>
  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";

const store = useUserStore();
const router = useRouter();

const checkLogin = () => {
  if (!store.isLogin) {
    alert("로그인이 필요합니당");
    router.push("/");
  } else {
    router.push("mypage");
  }
};
</script>

<style scoped>
.nav-link {
  color: #444444;
  text-decoration: none;
}
.active-link {
  color: rgb(33, 168, 15);
}
</style>
