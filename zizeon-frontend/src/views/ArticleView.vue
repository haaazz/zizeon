<template>
  <div class="w-5/6 flex flex-col mx-auto">
    <h3 class="text-2xl font-bold sm:text-4xl mb-4 text-center mt-8">
      커뮤니티
    </h3>
    <div class="grid justify-items-end">
    <button v-if="userStore.isLogin" class="border border-gray-500 mb-2 rounded-lg p-1 bg-slate-50">
      <RouterLink :to="{ name: 'ArticleCreate' }">게시글 작성</RouterLink>
    </button>
  </div>
  <div class="rounded-lg border w-full border-gray-200 mx-auto">
    <div class="overflow-x-auto rounded-t-lg">
    <table class="min-w-full divide-y-2 divide-gray-200 bg-white text-sm">
      <thead class="ltr:text-left rtl:text-right">
        <tr>
          <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center">ID</th>
          <th class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center">제목</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-gray-200">
        <tr v-for="article in paginatedArticles" :key="article.id">
          <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center">{{ article.id }}</td>
          <td class="whitespace-nowrap px-4 py-2 font-medium text-gray-900 text-center">
            <RouterLink :to="{ name: 'ArticleDetail', params: { id: article.id } }">
              {{ article.title }}
            </RouterLink>
          </td>
        </tr>
      </tbody>
    </table>
    <hr class="border border-gray-200">
    <div class="text-center mt-2 mb-2">
      <button @click="prevPage" :disabled="currentPage === 1" class="mr-2">이전</button>
      <span>{{ currentPage }} / {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages" class="ml-2">
        다음
      </button>
    </div>
  </div>
</div>
</div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue";
import { useArticleStore } from "@/stores/articles";
import { RouterLink } from "vue-router";
import { useUserStore } from "@/stores/user";

const store = useArticleStore();
const articles = ref([]);
const currentPage = ref(1);
const articlesPerPage = 15;
const userStore = useUserStore();

const paginatedArticles = computed(() => {
  const startIndex = (currentPage.value - 1) * articlesPerPage;
  const endIndex = startIndex + articlesPerPage;
  return store.articles.slice(startIndex, endIndex);
});

const totalPages = computed(() =>
  Math.ceil(store.articles.length / articlesPerPage)
);

function nextPage() {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
  }
}

function prevPage() {
  if (currentPage.value > 1) {
    currentPage.value--;
  }
}

onMounted(async () => {
  await store.getArticles();
  articles.value = store.articles;
});
</script>

<style scoped>
</style>
