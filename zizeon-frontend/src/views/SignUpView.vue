<template>
    <div>
      <h1>회원가입</h1>
      <form @submit.prevent="signUp">
        <label for="username">성함:</label>
        <input type="text" id="username" v-model.trim="username"><br>
  
        <label for="password1">비밀번호:</label>
        <input type="password" id="password1" v-model.trim="password1"><br>
        
        <label for="password2">비밀번호 확인:</label>
        <input type="password" id="password2" v-model.trim="password2"><br>
  
        <label for="email">이메일:</label>
        <input type="email" id="email" v-model.trim="email"><br>
  
        <label for="nickname">닉네임:</label>
        <input type="text" id="nickname" v-model.trim="nickname"><br>
  
        <label> 성별 </label>
        <div>
        <label for="Male">남성</label>
        <input type="radio" id="Male" value="Male" v-model="gender"><br>

        <label for="Female">여성</label>
        <input type="radio" id="Female" value="Female" v-model="gender"><br>
        </div>

        <label for="age">나이:</label>
        <input type="text" id="age" v-model.trim="age"><br>
  
        <label for="job">직업:</label>
        <input type="text" id="job" v-model.trim="job"><br>
  
        <label for="income">연봉:</label>
        <input type="text" id="income" v-model.trim="income"><br>
  
        <input type="submit" value="회원가입 완료">
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useUserStore } from '@/stores/user'
  import { useRouter } from 'vue-router'
  
  const store = useUserStore()
  const router = useRouter()
  
  const username = ref('')
  const password1 = ref('')
  const password2 = ref('')
  const email = ref('')
  const age = ref('')
  const nickname = ref('')
  const job = ref('')
  const income = ref('')
  const gender = ref(null)
  
  const signUp = () => {
    const payload = {
      username: username.value,
      password1: password1.value,
      password2: password2.value,
      email: email.value,
      age: age.value,
      job: job.value,
      nickname: nickname.value,
      income: income.value,
      gender: gender.value
    }
  
    store.signUp(payload)
      .then(() => {
        router.push({ name: 'home' }) // 회원가입 성공 후 홈으로 이동
      })
      .catch(err => {
        console.error('회원가입 실패:', err)
      })
  }
  </script>
  
  <style scoped>
  /* 스타일 추가 */
  </style>
  