<template>
    <div>
      <h1>프로필 수정</h1>
      <form @submit.prevent="updateProfile">
        <label>이름:</label>
        <input v-model="editedProfile.name" type="text">
        <button type="submit">완료</button>
      </form>
    </div>
  </template>
  
  <script setup>
    import { ref } from 'vue'
    import axios from 'axios'
    import { useUserStore } from '@/stores/user'
    import router from '@/router'
  
    const userstore = useUserStore()
    const editedProfile = ref({
      name: userstore.username, 
    })
  
    const updateProfile = () => {
      axios.post('update_profile', editedProfile.value)
        .then(response => {
          router.push('/mypage')
        })
        .catch(error => {
          console.error(error)
        })
    }
  </script>
  