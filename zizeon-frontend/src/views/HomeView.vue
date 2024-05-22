<template>
    <div>
      <h1>zㅣ젼킹왕짱;;</h1>
    </div>
    <div v-if="!store.isLogin">
      <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink> | 
      <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink>
    </div>
    <div v-else>
      어서오시게나 {{ nickname }}
      <button @click="logout">잘가시게</button>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { RouterLink } from 'vue-router'
  import { useUserStore } from '@/stores/user'
  import axios from 'axios'
  
  const store = useUserStore()

  const nickname = ref('')

  axios({
    url: `${store.API_URL}/accounts/user`,
    method: 'get',
    headers: {
        Authorization: `Token ${store.token}`
      }
  }).then((res) => {
    nickname.value = res.data.nickname
  }).catch((err) => {
    console.log(err)
  })

  
  const logout = () => {
    store.logout()
  }
  </script>
  
  <style scoped>
  /* 스타일 추가 */
  </style>
  