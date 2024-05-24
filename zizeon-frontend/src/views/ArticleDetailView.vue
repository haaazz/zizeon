<template>
  <div v-if="article" class="w-4/5 mx-auto">
    <button @click="goBack" class="mt-6 border pt-2 pb-2 pl-8 pr-8 rounded-lg">
      뒤로가기
    </button>
    <h1 class="text-2xl font-bold text-gray-700 sm:text-3xl mb-12 mt-6">
      게시글 상세 조회
    </h1>
    <div>
      <h3 class="text-lg font-bold sm:text-lg mb-4 mt-8">#{{ article.id }}</h3>
      <h3 class="text-2xl font-bold sm:text-2xl mb-4">
        {{ article.title }}
      </h3>
      <h3 class="text-xs sm:text-xs mb-4">
        작성 {{ article.user.username }} | 작성시각
        {{ article.created_at.slice(0, 10) }} | 최종 수정시각
        {{ article.updated_at.slice(0, 10) }}
      </h3>
      <div class="flex gap-x-8 border p-5 rounded-lg mt-6 h-60 bg-gray-50">
        <h3 class="text-m sm:text-m mb-4">
          {{ article.content }}
        </h3>
      </div>
    </div>
    <div class="flex justify-end">
      <div v-if="article.user.id == userStore.loginUser.pk">
        <button
          @click="editArticle"
          class="mt-2 border pt-2 pb-2 pl-8 pr-8 mb-2 rounded-lg"
        >
          게시글 수정
        </button>
        <button
          @click.prevent="deleteArticle"
          class="mt-2 ml-4 border pt-2 pb-2 pl-8 pr-8 mb-2 rounded-lg"
        >
          게시글 삭제
        </button>
      </div>
    </div>
    <hr />

    <div class="h-8">
      <p class="mt-2 ml-2 font-bold" v-if="userStore.isLogin">댓글 작성</p>
      <form
        v-if="userStore.isLogin"
        @submit="createComment"
        class="flex items-end flex-row justify-around"
      >
        <input
          type="text"
          v-model="commentContent"
          class="p-1 border rounded-lg mt-2 mb-2 w-4/5 h-20 ml-5"
        />
        <input
          type="submit"
          value="제출"
          class="mt-3 ml-12 mr-12 border pt-3 pb-3 pl-8 pr-8 mb-2 rounded-lg"
        />
      </form>

      <hr />
      <div>
        <div v-for="comment in comments" :key="comment.id">
          <p class="mt-2">{{ comment.user.username }}</p>
          <div>
            <div
              v-if="!comment.isEditing"
              class="p-3 border rounded-lg mb-3 bg-stone-50 ml-8 mr-8 mt-1"
            >
              {{ comment.content }}

              <form
                v-if="comment.user.id === userStore.loginUser.pk"
                class="flex justify-end"
              >
                <button
                  @click="startEditComment(comment)"
                  class="border rounded-lg pl-2 pr-2 mr-5"
                >
                  수정
                </button>

                <button
                  @click.prevent="deleteComment(comment.id)"
                  class="border rounded-lg pl-2 pr-2 mr-5"
                >
                  삭제
                </button>
              </form>
            </div>
            <div
              v-else
              class="p-3 border rounded-lg mb-3 bg-stone-50 ml-8 mr-8 mt-1"
            >
              <form
                @submit.prevent="editComment(comment)"
                class="flex justify-center"
              >
                <input
                  type="text"
                  v-model="comment.editContent"
                  class="w-full mr-2 border rounded-lg h-12"
                />
                <input
                  type="submit"
                  value="수정 완료"
                  class="border rounded-lg pl-2 pr-2 mr-3"
                />
                <button
                  @click="cancelEditComment(comment)"
                  class="border rounded-lg w-16"
                >
                  취소
                </button>
              </form>
            </div>
            <hr />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useArticleStore } from "@/stores/articles";
import { useUserStore } from "@/stores/user";

const store = useArticleStore();
const route = useRoute();
const router = useRouter();
const article = ref(null);
const userStore = useUserStore();
const comments = ref([]);
const commentContent = ref("");
const writer = ref("");
const commentWriter = ref({});

const deleteArticle = () => {
  if (article.value && confirm("게시글을 삭제하시겠습니까?")) {
    return axios({
      method: "delete",
      url: `${store.API_URL}/articles/${article.value.id}/`,
      headers: {
        Authorization: `Token ${userStore.loginUser.token}`,
      },
    })
      .then(() => {
        console.log("게시글 잘 삭제됨 !!");
        router.push("/article");
      })
      .catch((err) => {
        console.log("삭제도 못한대요 ㅋ");
        console.log(err);
      });
  }
};

const editArticle = () => {
  router.push({
    name: "editArticle",
    query: {
      id: article.value.id,
      title: article.value.title,
      content: article.value.content,
    },
  });
};

const goBack = () => {
  router.back();
};

const createComment = () => {
  console.log(commentContent.value);
  axios({
    method: "post",
    url: `${store.API_URL}/articles/${route.params.id}/comments/`,
    headers: {
      Authorization: `Token ${userStore.loginUser.token}`,
    },
    data: {
      content: commentContent.value,
    },
  })
    .then((res) => {
      comments.value.push(res.data);
      commentContent.value = "";
    })
    .catch((err) => {
      console.log(err);
    });
};

const startEditComment = (comment) => {
  comment.isEditing = true;
  comment.editContent = comment.content;
};

const cancelEditComment = (comment) => {
  comment.isEditing = false;
  comment.editContent = "";
};

const editComment = (comment) => {
  axios({
    method: "put",
    url: `${store.API_URL}/articles/${route.params.id}/comments/${comment.id}/`,
    headers: {
      Authorization: `Token ${userStore.loginUser.token}`,
    },
    data: {
      content: comment.editContent,
    },
  })
    .then((res) => {
      comment.content = comment.editContent;
      comment.isEditing = false;
      comment.editContent = "";
    })
    .catch((err) => {
      console.log(err);
    });
};

const deleteComment = (commentPk) => {
  axios({
    method: "delete",
    url: `${store.API_URL}/articles/${route.params.id}/comments/${commentPk}`,
    headers: {
      Authorization: `Token ${userStore.loginUser.token}`,
    },
  })
    .then(() => {
      comments.value = comments.value.filter(
        (comment) => comment.id !== commentPk
      );
    })
    .catch((err) => {
      console.log(err);
    });
};

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/articles/${route.params.id}/`,
  })
    .then((res) => {
      article.value = res.data;
    })
    .catch((err) => {
      article.value = null;
    });
  axios({
    method: "get",
    url: `${store.API_URL}/articles/${route.params.id}/comments/`,
  })
    .then((res) => {
      comments.value = res.data.map((comment) => ({
        ...comment,
        isEditing: false,
        editContent: "",
      }));
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>
