<template>
    <div>
        <h5>{{ article.id }}</h5>
        <p>{{ article.title }}</p>
        <p>{{ article.content }}</p>
        <RouterLink :to="{ name: 'ArticleDetail', params: { id: article.id }}"> [ 자세히 ]</RouterLink>
        <hr>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps ({
    article: Object
})
</script>

<style scoped>

</style>