<template>
    <div>
        <h1>무리무리</h1>
        <div v-if="article">
            <p>{{article.id}}</p>
            <p>{{article.title}}</p>
            <p>{{article.content}}</p>
        </div>
    </div>
</template>

<script setup>

import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { useArticleStore } from '@/stores/articles'

const store = useArticleStore()
const route = useRoute()
const article = ref(null)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    })
    .then((res) => {
        console.log(res.data)
        article.value = res.data
    })
    .catch(err => console.log(err))
})

</script>

<style scoped>

</style>