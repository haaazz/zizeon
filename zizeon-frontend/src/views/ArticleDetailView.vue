<template>
    <div v-if="article">
        <h1>무리무리</h1>
        <div v-if="article.user == currentUserPK">
            <button @click="editArticle">게시글 수정</button>
            <button @click="deleteArticle">게시글 삭제</button>
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

const deleteArticle = () => {
    if(article.value && confirm("게시글 진심 삭 제?")) {
        return axios({
            method: 'delete',
            url: `${store.API_URL}/articles/${article.value.id}/`,
            headers: {
                Authorization: `Token ${userStore.token}`
            }
        })
        .then(() => {
            console.log('게시글 잘 삭제됨 !!')
            router.push('/article')
        })
        .catch(err => {
            console.log('삭제도 못한대요 ㅋ')
            console.log(err)
        })
    }
}

const editArticle = () => {
    router.push({
        name: 'editArticle',
        query: {
            id: article.value.id,
            title: article.value.title,
            content: article.value.content,
        }
    });
}

onMounted(() => {
    axios({
        method: 'get',
        url: `${store.API_URL}/articles/${route.params.id}/`,
    })
    .then((res) => {
        article.value = res.data
    })
    .catch(err => {
        article.value = null
    })

    axios({
        method: 'get',
        url: `${store.API_URL}/accounts/user/`,
        headers: {
            Authorization: `Token ${userStore.token}`
        }
    })
    .then((res) => {
        currentUserPK.value = res.data.pk
    })
    .catch(err => {
        console.log(err)
    })

})
</script>
