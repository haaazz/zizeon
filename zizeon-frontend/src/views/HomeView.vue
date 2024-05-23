<template>
  <section>
    <div
      class="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8 lg:py-16"
    >
      <div class="grid grid-cols-1 gap-8 lg:grid-cols-2 lg:gap-16">
        <div
          class="relative h-64 overflow-hidden rounded-lg sm:h-80 lg:order-last lg:h-full"
        >
          <img
            alt=""
            src="@/assets/nonbat.jpg"
            class="absolute inset-0 h-full w-full object-cover"
          />
        </div>

        <div class="lg:py-24">
          <h2 class="text-3xl font-bold sm:text-4xl mb-4">저희는말입니다</h2>
          <h2 class="text-3xl font-bold sm:text-4xl mb-4">지전입니다</h2>

          <div class="bg-white">
            <p class="mt-6 text-gray-600">
              이러쿵저러쿵하는서비스입니다 짱멋지져
            </p>
            <p class="mt-4 text-gray-600">
              이러쿵저러쿵하는서비스입니다 짱멋지져
            </p>
            <p class="mt-4 text-gray-600">
              이러쿵저러쿵하는서비스입니다 짱멋지져
            </p>
            <p class="mt-4 text-gray-600">
              이러쿵저러쿵하는서비스입니다 짱멋지져
            </p>
          </div>

          <div v-if="!store.isLogin">
            <RouterLink
              :to="{ name: 'LogInView' }"
              class="mt-8 mr-8 inline-block rounded bg-green-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-green-700 focus:outline-none focus:ring focus:ring-yellow-400"
              :class="{ 'active-link': $route.path === '/login' }"
            >
              로그인
            </RouterLink>
            <RouterLink
              :to="{ name: 'SignUpView' }"
              class="mt-8 mr-8 inline-block rounded bg-green-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-green-700 focus:outline-none focus:ring focus:ring-yellow-400"
              :class="{ 'active-link': $route.path === '/signup' }"
              >회원가입</RouterLink
            >
          </div>
          <div v-else>
            <p class="mt-6 text-gray-600">어서 와, {{ store.loginUser.nickname }} !</p>
            <button
              class="mt-8 mr-8 inline-block rounded bg-green-600 px-12 py-3 text-sm font-medium text-white transition hover:bg-green-700 focus:outline-none focus:ring focus:ring-yellow-400"
              @click="logout"
            >
              로그아웃
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue";
import { RouterLink } from "vue-router";
import { useUserStore } from "@/stores/user";

const store = useUserStore();

const logout = () => {
  store.logout();
};
</script>

<style scoped>
.nav-link {
  text-decoration: none;
  margin: 10px 0;
  display: inline-block;
}

.button {
  display: inline-block;
  padding: 10px 20px;
  font-size: 16px;
  color: rgb(255, 255, 255);
  background-color: #468ddf;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #0056b3;
}

.active-link {
  background-color: #0056b3;
}
</style>
