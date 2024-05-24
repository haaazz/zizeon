<template>
  <header>
    <nav class="bg-white border-gray-200 dark:bg-gray-900">
      <div
        class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4"
      >
        <RouterLink
          :to="'/'"
          class="flex items-center space-x-3 rtl:space-x-reverse"
          :class="{ 'active-link': $route.path === '/' }"
        >
          <img src="@/assets/zz.png" class="h-8" alt="zizeon typo" />
        </RouterLink>

        <!-- 햄버거 버튼으로 바뀌는 부분 <button
          data-collapse-toggle="navbar-default"
          type="button"
          class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
          aria-controls="navbar-default"
          aria-expanded="false"
        >
          <span class="sr-only">Open main menu</span>
          <svg
            class="w-5 h-5"
            aria-hidden="true"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 17 14"
          >
            <path
              stroke="currentColor"
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M1 1h15M1 7h15M1 13h15"
            />
          </svg>
        </button> -->
        <div class="hidden w-full md:block md:w-auto" id="navbar-default">
          <ul
            class="font-medium flex flex-col p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700"
          >
            <li>
              <RouterLink
                :to="'/'"
                class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-white md:dark:hover:text-green-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
                :class="{ 'active-link': $route.path === '/' }"
              >
                홈
              </RouterLink>
            </li>
            <li>
              <RouterLink
                :to="'/quiz'"
                class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-white md:dark:hover:text-green-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
                :class="{ 'active-link': $route.path === '/quiz' }"
              >
                금융퀴즈
              </RouterLink>
            </li>
            <li>
              <RouterLink
                :to="'/products'"
                class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-white md:dark:hover:text-green-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
                :class="{ 'active-link': $route.path === '/products' }"
              >
                전체상품
              </RouterLink>
            </li>
            <li>
              <RouterLink
                :to="'/recommend'"
                class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-white md:dark:hover:text-green-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
                :class="{ 'active-link': $route.path === '/recommend' }"
              >
                추천상품
              </RouterLink>
            </li>
            <li>
              <RouterLink
                :to="'/map'"
                class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-white md:dark:hover:text-green-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
                :class="{ 'active-link': $route.path === '/map' }"
              >
                은행지도
              </RouterLink>
            </li>
            <li>
              <RouterLink
                :to="'/exchange'"
                class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-white md:dark:hover:text-green-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
                :class="{ 'active-link': $route.path === '/exchange' }"
              >
                환율계산
              </RouterLink>
            </li>
            <li>
              <RouterLink
                :to="'/article'"
                class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-white md:dark:hover:text-green-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
                :class="{ 'active-link': $route.path === '/article' }"
              >
                커뮤니티
              </RouterLink>
            </li>
            <li>
              <RouterLink
                :to="'/mypage'"
                class="block py-2 px-3 text-gray-900 rounded hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 md:p-0 dark:text-white md:dark:hover:text-green-500 dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent"
                :class="{ 'active-link': $route.path === '/mypage' }"
                @click="checkLogin"
              >
                마이페이지
              </RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>

  <div class="rouview">
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";

const store = useUserStore();
const router = useRouter();

const checkLogin = () => {
  if (!store.isLogin) {
    alert("로그인이 필요한 기능입니다.");
    router.push("/login");
  } else {
    router.push("/mypage");
  }
};
</script>

<style scoped>
.rouview {
  min-height: 100vh;
  min-width: 100vw;
  background-image: url("@/assets/bgc.png");
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
}
</style>
