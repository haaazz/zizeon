<template>

  <div v-if="article" class="w-5/6 text-center">
    <div>
      <h3 class="text-lg font-bold sm:text-lg mb-4 mt-8">
        {{ article.id }}번째 게시글
    </h3>
    <h3 class="text-lg font-bold sm:text-lg mb-4 ">
      제목 : {{ article.title }}
    </h3>
    <h3 class="text-lg font-bold sm:text-lg mb-4">
      내용 : {{ article.content }}
    </h3>
    <h3 class="text-lg font-bold sm:text-lg mb-4">
      작성자 : {{ article.user.username }}
    </h3>
    </div>
    <hr>
    <div v-if="article.user.id == userStore.loginUser.pk">
      <button @click="editArticle">게시글 수정</button>
      <button @click="deleteArticle">게시글 삭제</button>
    </div>
    <hr>
    <div>
      <form @submit="createComment">
        <input type="text" v-model="commentContent">
        <input type="submit" value="제출">
      </form>
    </div>
    <hr>
    <div>
      <div v-for="comment in comments" :key="comment.id">
        <span v-if="!comment.isEditing">
          {{ comment.content }}
          <p>작성자: {{ comment.user.username }}</p>
          <form v-if="comment.user.id === userStore.loginUser.pk">
            | <button @click="startEditComment(comment)">수정</button> | 
            <button @click="deleteComment(comment.id)">삭제</button> |
          </form>
        </span>
        <span v-else>
          <form @submit.prevent="editComment(comment)">
            <input type="text" v-model="comment.editContent">
            <input type="submit" value="수정 완료">
            <button @click="cancelEditComment(comment)">취소</button>
          </form>
        </span>
        <br>
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
const commentContent = ref('');
const writer = ref('')
const commentWriter = ref({})

const deleteArticle = () => {
  if (article.value && confirm("게시글 진심 삭 제?")) {
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

const createComment = () => {
  console.log(commentContent.value);
  axios({
    method: 'post',
    url: `${store.API_URL}/articles/${route.params.id}/comments/`,
    headers: {
      Authorization: `Token ${userStore.loginUser.token}`
    },
    data: {
      content: commentContent.value
    }
  }).then((res) => {
    comments.value.push(res.data);
    commentContent.value = '';
  }).catch((err) => {
    console.log(err);
  });
};

const startEditComment = (comment) => {
  comment.isEditing = true;
  comment.editContent = comment.content;
};

const cancelEditComment = (comment) => {
  comment.isEditing = false;
  comment.editContent = '';
};

const editComment = (comment) => {
  axios({
    method: 'put',
    url: `${store.API_URL}/articles/${route.params.id}/comments/${comment.id}/`,
    headers: {
      Authorization: `Token ${userStore.loginUser.token}`
    },
    data: {
      content: comment.editContent
    }
  }).then((res) => {
    comment.content = comment.editContent;
    comment.isEditing = false;
    comment.editContent = '';
  }).catch((err) => {
    console.log(err);
  });
};

const deleteComment = (commentPk) => {
  axios({
    method: 'delete',
    url: `${store.API_URL}/articles/${route.params.id}/comments/${commentPk}`,
    headers: {
      Authorization: `Token ${userStore.loginUser.token}`
    }
  }).then(() => {
    comments.value = comments.value.filter(comment => comment.id !== commentPk);
  }).catch((err) => {
    console.log(err);
  });
};

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/articles/${route.params.id}/`,
  })
    .then((res) => {
      article.value = res.data
    })
    .catch((err) => {
      article.value = null;
    });
  axios({
    method: "get",
    url: `${store.API_URL}/articles/${route.params.id}/comments/`,
  })
    .then((res) => {
      comments.value = res.data.map(comment => ({ ...comment, isEditing: false, editContent: '' }));
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>
