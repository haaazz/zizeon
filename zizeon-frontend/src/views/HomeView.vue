<template>
  <div v-if="!store.isLogin" class="navigation">
    <RouterLink
      :to="{ name: 'SignUpView' }"
      class="nav-link button"
      :class="{ 'active-link': $route.path === '/signup' }"
    >
      회원가입
    </RouterLink>
    <br />
    <RouterLink
      :to="{ name: 'LogInView' }"
      class="nav-link button"
      :class="{ 'active-link': $route.path === '/login' }"
    >
      로그인
    </RouterLink>
  </div>
  <div v-else>
    어서 와, {{ nickname }} !
    <button class="button" @click="logout">로그아웃</button>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { RouterLink } from "vue-router";
import { useUserStore } from "@/stores/user";
import axios from "axios";

const store = useUserStore();

const nickname = ref("");

axios({
  url: `${store.API_URL}/accounts/user`,
  method: "get",
  headers: {
    Authorization: `Token ${store.token}`,
  },
})
  .then((res) => {
    nickname.value = res.data.nickname;
  })
  .catch((err) => {
    console.log(err);
  });

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
