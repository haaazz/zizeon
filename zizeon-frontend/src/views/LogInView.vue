<template>
    <div class="w-5/6 flex flex-col mx-auto">
    <h1
      class="text-center text-2xl font-bold text-green-600 sm:text-3xl mt-12"
    >로그인</h1>
  <form @submit.prevent="logIn" class="max-w-sm mx-auto mt-20">
    <div class="mb-5">
      <label
        for="username"
        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >아이디</label
      >
      <input
        type="text"
        id="username"
        v-model.trim="username"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-green-500 dark:focus:border-green-500"
        required
      />
    </div>
    <div class="mb-5">
      <label
        for="password"
        class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
        >비밀번호</label
      >
      <input
        type="password"
        id="password"
        v-model.trim="password"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-green-500 focus:border-green-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-green-500 dark:focus:border-green-500"
        required
      />
    </div>
    <button
      type="submit"
      value="logIn"
      class="w-full text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >
      로그인
    </button>
      <div>
        <div class="mt-9 text-xs text-end">
  <RouterLink :to="{ name:'SignUpView'}"><p>혹시 아직 계정이 없으신가요? 회원가입은 <strong class="text-green-600">이쪽</strong>으로 모시겠습니다!</p></RouterLink></div>
</div>  
</form>
</div>
</template>

<script setup>
import { ref } from "vue";
import { useUserStore } from "@/stores/user";
import { useRouter } from "vue-router";
import { RouterLink } from 'vue-router'

const store = useUserStore();
const router = useRouter();

const username = ref("");
const password = ref("");

const logIn = () => {
  const payload = {
    username: username.value,
    password: password.value,
  };

  store
    .logIn(payload)
    .then(() => {
      router.push({ name: "home" }); // 로그인 성공 후 홈으로 이동
    })
    .catch((err) => {
      console.error("로그인 실패:", err);
    });
};
</script>

<style scoped></style>
