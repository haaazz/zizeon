<template>
    <div>
        <h1>zㅣ젼킹왕짱;;</h1>
    </div>
    <div>
        <RouterLink :to="{ name: 'SignUpView' }"> 회원가입 </RouterLink>
        <RouterLink :to="{ name: 'LogInView' }"> 로그인 </RouterLink>

    </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>

</style>