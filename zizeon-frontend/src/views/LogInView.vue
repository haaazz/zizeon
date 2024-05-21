<template>
    <div>
        <form @submit.prevent="logIn">
            <label for="username"> username: </label>
            <input type="text" id="username" v-model.trim="username"><br>

            <label for="password"> password: </label>
            <input type="password" id="password" v-model.trim="password"><br>

            <input type="submit" value="logIn">
        </form>
    </div>
</template>

<script setup>

import { ref } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router'

const store = useUserStore()
const router = useRouter()

const username = ref(null)
const password = ref(null)

const logIn = function() {
    const payload = {
        username: username.value,
        password: password.value
    }

    store.logIn(payload)
        .then(response => {
            // 로그인 성공 후 홈으로 이동
            router.push({ name: 'home' })
        })
        .catch(err => {
            console.error('로그인 실패:', err)
        })
}

</script>

<style scoped>

</style>