<template>
    <div>
        <h1>커뮤니티</h1>
        <RouterLink :to="{name:'ArticleCreate'}">[게시글 작성]</RouterLink>
        <ArticleList/>
    </div>
</template>

<script setup>

import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/articles'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useArticleStore()

onMounted(() => {
    store.getArticles()
})

</script>

<style scoped>

</style>