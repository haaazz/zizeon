<template>
  <div>
    <h1>커뮤니티</h1>
    <div v-if="userStore.isLogin">
    <RouterLink :to="{name:'ArticleCreate'}">[게시글 작성]</RouterLink>
    </div>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>제목</th>
          <th>자세히</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in paginatedArticles" :key="article.id">
          <td>{{ article.id }}</td>
          <td>{{ article.title }}</td>
          <td><RouterLink :to="{ name: 'ArticleDetail', params: { id: article.id }}">[자세히]</RouterLink></td>
        </tr>
      </tbody>
    </table>
    <div>
      <button @click="prevPage" :disabled="currentPage === 1">이전</button>
      <span>{{ currentPage }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">다음</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useArticleStore } from '@/stores/articles'
import { RouterLink } from 'vue-router'
import { useUserStore } from '@/stores/user'

const store = useArticleStore()
const articles = ref([])
const currentPage = ref(1)
const articlesPerPage = 15
const userStore = useUserStore()

const paginatedArticles = computed(() => {
  const startIndex = (currentPage.value - 1) * articlesPerPage
  const endIndex = startIndex + articlesPerPage
  return store.articles.slice(startIndex, endIndex)
})

const totalPages = computed(() => Math.ceil(store.articles.length / articlesPerPage))

function nextPage() {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

function prevPage() {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}

  onMounted(async () => {
    await store.getArticles()
    articles.value = store.articles
  })

</script>

<style scoped>
/* 추가적인 스타일링을 원하면 여기에 추가하세요. */
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

th {
  background-color: #f2f2f2;
}
</style>