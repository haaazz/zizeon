<template>
  <div>
    <h1>디테일</h1>
  </div>

  <div>
    <div v-if="saving">
      <h3>금융상품명: {{ saving.fin_prdt_nm }}</h3>
      <h3>금융회사명: {{ saving.kor_co_nm }}</h3>
    </div>

    <form v-if="userstore.isLogin">
      <label for="balance">예치금: </label>
      <input type="number" id="balance" v-model="balance" />
      <button @click.prevent="open">가입</button>
    </form>

    <div v-for="option in options" :key="option.id">
      <hr />
      <p>적립유형: {{ option.rsrv_type_nm }}</p>
      <p>저축기간: {{ option.save_trm }}</p>
      <p>저축금리: {{ option.intr_rate }}</p>
      <p>최고우대금리: {{ option.intr_rate2 }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useSavingStore } from "@/stores/saving";
import { useUserStore } from "@/stores/user";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";

const store = useSavingStore();
const route = useRoute();
const router = useRouter();
const userstore = useUserStore();

const saving = ref(null);
const options = ref(null);
const balance = ref(0);

const open = function () {
  axios({
    method: "post",
    url: `${store.API_URL}/products/saving/${route.params.id}/open/`,
    data: {
      balance: balance.value,
    },
    headers: {
      Authorization: `Token ${userstore.loginUser.value.token}`,
    },
  })
    .then((response) => {
      userstore.getUserOpenedProducts()
      router.push({ name: "mypage" });
    })
    .catch((error) => {
      console.log(balance.value);
    });
};

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/products/saving/${route.params.id}/`,
  })
    .then((response) => {
      saving.value = response.data.saving;
      options.value = response.data.option;
    })
    .catch((error) => {
      console.log(error);
    });
});
</script>

<style scoped></style>
