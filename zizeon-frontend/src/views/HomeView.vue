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
            src="@/assets/howl.jpg"
            class="absolute inset-0 h-full w-full object-cover"
          />
        </div>

        <div class="lg:py-24">
          <h2 class="text-3xl font-bold sm:text-4xl mb-4">
            당신을 위한 똑똑한 금융 온라인 플랫폼
          </h2>
          <h2 class="text-2xl font-bold sm:text-3xl mb-4">지전입니다 😉</h2>
          <h4 class="text-xl font-bold sm:text-1xl mb-4">
            지전(摯錢, 잡을 지 + 돈 전): 돈을 움켜쥐는
          </h4>
          <h4 class="text-xl font-bold sm:text-1xl mb-4">
            지전(祉田, 복 지 + 밭 전): 복이 넘치는 밭
          </h4>

          <div class="bg-white">
            <p class="mt-6 text-gray-600">
              '지전'은 돈을 관리하고 더 나은 미래를 위한 저축에 도움을 주는
              온라인 플랫폼입니다. <br />
              저축 정보, 환율 정보, 그리고 주변 은행 위치 정보를 쉽게 찾아볼 수
              있으며, <br />예적금 추천 및 가입 기능을 제공하여 효율적으로
              자산을 관리할 수 있도록 지원합니다. <br />'지전'은 안정적인 재정
              상태와 풍요로운 미래를 위한 파트너로서 여러분을 돕겠습니다.
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
            <p class="mt-6 text-gray-600 text-2xl font-bold">
              어서오세요, {{ store.loginUser.nickname }} 님 ! 🤩
            </p>
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
