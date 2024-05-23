<template>
  <div class="w-5/6 mx-auto">
    <h3 class="text-2xl font-bold sm:text-4xl mb-4 text-center mt-8">
      게시글 수정
    </h3>
    <form @submit.prevent="updateArticle" class="w-5/6 mx-auto">
      <div>
        <label
          for="title"
          class="block mb-2 text-m font-medium text-gray-900 dark:text-white"
          >제목</label
        >
        <input
          type="text"
          id="title"
          v-model.trim="title"
          class="block w-full p-2 text-gray-900 border border-gray-300 rounded-lg bg-gray-50 text-s focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        />
      </div>
      <div class="mb-5">
        <label
          for="content"
          class="block mb-2 mt-5 text-m font-medium text-gray-900 dark:text-white"
          >내용</label
        >
        <textarea
          type="text"
          id="content"
          v-model.trim="content"
          class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 h-60"
          placeholder="글을 입력해주세요"
        ></textarea>

        <input
          type="submit"
          class="mt-5 mr-0 p-2 pl-4 pr-4 rounded bg-green-600 px-2 py-1 text-s text-white transition hover:bg-green-700 focus:outline-none"
        />
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import { useUserStore } from "@/stores/user";
import { useArticleStore } from "@/stores/articles";

const route = useRoute();
const router = useRouter();
const userStore = useUserStore();
const articleStore = useArticleStore();

const title = ref("");
const content = ref("");
const articleId = ref(null);

onMounted(() => {
  articleId.value = route.query.id;
  title.value = route.query.title;
  content.value = route.query.content;
});

const updateArticle = () => {
  axios({
    method: "put",
    url: `${articleStore.API_URL}/articles/${articleId.value}/`,
    headers: {
      Authorization: `Token ${userStore.loginUser.token}`,
    },
    data: {
      title: title.value,
      content: content.value,
    },
  })
    .then(() => {
      console.log("게시글 수정 완료");
      router.push(`/articles/${articleId.value}`);
    })
    .catch((err) => {
      console.log("수정에 실패했습니다.");
      console.log(err);
    });
};
</script>
