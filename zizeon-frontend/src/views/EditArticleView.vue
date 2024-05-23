<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle">
      <div>
        <label for="title">제목</label>
        <input id="title" v-model="title" type="text" />
      </div>
      <div>
        <label for="content">내용</label>
        <textarea id="content" v-model="content"></textarea>
      </div>
      <button type="submit">수정하기</button>
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
