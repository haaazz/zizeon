<template>
    <div v-if="article">
        <h1>무리무리</h1>
        <div v-if="article.user == currentUserPK">
            <button>게시글 수정</button>
            <button>게시글 삭제</button>
        </div>
        <div>
            <p>{{ article.id }}</p>
            <p>{{ article.title }}</p>
            <p>{{ article.content }}</p>
        </div>
    </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/articles'
import { useUserStore } from '@/stores/user'

const store = useArticleStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const userStore = useUserStore()
const currentUserPK = ref(0)

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/articles/${route.params.id}/`,
    })
    .then((res) => {
        console.log(res.data)
        article.value = res.data
    })
    .catch(err => {
        console.log(err)
        article.value = null
    })

    console.log('axios 시작')
    axios({
        method: 'get',
        url: `${store.API_URL}/accounts/user/`,
        headers: {
            Authorization: `Token ${userStore.token}`
        }
    })
    .then((res) => {
        console.log('성공!')
        console.log(res.data.pk)
        currentUserPK.value = res.data.pk
    })
    .catch(err => {
        console.log('실패!')
        console.log(err)
    })

})

console.log(store.articles)

</script>
